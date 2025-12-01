from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from models.models import Appointment, User, Patient, AppointmentStatus, UserType
from schemas.schemas import AppointmentCreate, AppointmentUpdate, Appointment as AppointmentSchema
from services.auth_service import get_current_user
from services.email_service import (
    send_email_appointment,
    send_email_appointment_rescheduled,
    send_email_appointment_canceled
)

router = APIRouter(prefix="/appointments", tags=["appointments"])


# ================================
# LISTAR AGENDAMENTOS
# ================================
@router.get("/", response_model=List[AppointmentSchema])
async def get_appointments(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type == UserType.PSICOLOGO:
        return db.query(Appointment).filter(
            Appointment.psychologist_id == current_user.id
        ).all()

    # Para pacientes → busca pelo e-mail do usuário
    patient = db.query(Patient).filter(Patient.email == current_user.email).first()
    if not patient:
        return []

    return db.query(Appointment).filter(
        Appointment.patient_id == patient.id
    ).all()


# ================================
# CRIAR AGENDAMENTO
# ================================
@router.post("/", response_model=AppointmentSchema)
async def create_appointment(
    appointment_data: AppointmentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # Verifica horário disponível
    existing = db.query(Appointment).filter(
        Appointment.psychologist_id == appointment_data.psychologist_id,
        Appointment.date == appointment_data.date,
        Appointment.time == appointment_data.time,
        Appointment.status == AppointmentStatus.AGENDADO
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Horário não disponível"
        )

    # Criar agendamento
    db_appointment = Appointment(
        **appointment_data.dict(),
        status=AppointmentStatus.AGENDADO
    )

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)

    # Buscar infos do paciente para enviar e-mail
    patient = db.query(Patient).filter(Patient.id == db_appointment.patient_id).first()

    if patient:
        send_email_appointment(
            client_email=patient.email,
            client_name=patient.name,
            date=db_appointment.date,
            time=db_appointment.time
        )

    return db_appointment


# ================================
# ATUALIZAR AGENDAMENTO (REAGENDAR)
# ================================
@router.put("/{appointment_id}", response_model=AppointmentSchema)
async def update_appointment(
    appointment_id: int,
    update_data: AppointmentUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )

    if current_user.type == UserType.PSICOLOGO and appointment.psychologist_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sem permissão para alterar este agendamento"
        )

    old_date = appointment.date
    old_time = appointment.time

    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(appointment, field, value)

    db.commit()
    db.refresh(appointment)

    # Se mudou data ou horário → enviar e-mail de REAGENDAMENTO
    if (appointment.date != old_date) or (appointment.time != old_time):
        patient = db.query(Patient).filter(Patient.id == appointment.patient_id).first()
        if patient:
            send_email_appointment_rescheduled(
                client_email=patient.email,
                client_name=patient.name,
                date=appointment.date,
                time=appointment.time
            )

    return appointment


# ================================
# CANCELAR AGENDAMENTO
# ================================
@router.delete("/{appointment_id}")
async def cancel_appointment(
    appointment_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )

    appointment.status = AppointmentStatus.CANCELADO
    db.commit()

    # Enviar e-mail de cancelamento
    patient = db.query(Patient).filter(Patient.id == appointment.patient_id).first()
    psychologist = db.query(User).filter(User.id == appointment.psychologist_id).first()

    if patient and psychologist:
        send_email_appointment_canceled(
            client_email=patient.email,
            client_name=patient.name,
            psychologist_name=psychologist.name
        )

    return {"message": "Agendamento cancelado com sucesso"}


# ================================
# HORÁRIOS DISPONÍVEIS
# ================================
@router.get("/available-slots")
async def get_available_slots(
    date: str,
    psychologist_id: int,
    db: Session = Depends(get_db)
):
    all_slots = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00', '17:00']

    occupied = db.query(Appointment.time).filter(
        Appointment.date == date,
        Appointment.psychologist_id == psychologist_id,
        Appointment.status == AppointmentStatus.AGENDADO
    ).all()

    occupied_times = [t[0] for t in occupied]
    available = [slot for slot in all_slots if slot not in occupied_times]

    return available
