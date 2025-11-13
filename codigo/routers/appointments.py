from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from models.models import Appointment, User, Patient, AppointmentStatus, UserType
from schemas.schemas import AppointmentCreate, AppointmentUpdate, Appointment as AppointmentSchema
from services.auth_service import get_current_user

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.get("/", response_model=List[AppointmentSchema])
async def get_appointments(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type == UserType.PSICOLOGO:
        appointments = db.query(Appointment).filter(
            Appointment.psychologist_id == current_user.id
        ).all()
    else:
        # Para pacientes, busca pelo ID do paciente
        patient = db.query(Patient).filter(Patient.email == current_user.email).first()
        if not patient:
            return []
        appointments = db.query(Appointment).filter(
            Appointment.patient_id == patient.id
        ).all()
    
    return appointments

@router.post("/", response_model=AppointmentSchema)
async def create_appointment(
    appointment_data: AppointmentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verifica se o horário está disponível
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
    
    db_appointment = Appointment(
        **appointment_data.dict(),
        status=AppointmentStatus.AGENDADO
    )
    
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    
    return db_appointment

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
    
    # Verifica permissão
    if current_user.type == UserType.PSICOLOGO and appointment.psychologist_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sem permissão para alterar este agendamento"
        )
    
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(appointment, field, value)
    
    db.commit()
    db.refresh(appointment)
    
    return appointment

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
    
    return {"message": "Agendamento cancelado com sucesso"}

@router.get("/available-slots")
async def get_available_slots(
    date: str,
    psychologist_id: int,
    db: Session = Depends(get_db)
):
    all_slots = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00', '17:00']
    
    occupied_slots = db.query(Appointment.time).filter(
        Appointment.date == date,
        Appointment.psychologist_id == psychologist_id,
        Appointment.status == AppointmentStatus.AGENDADO
    ).all()
    
    occupied_times = [slot[0] for slot in occupied_slots]
    available_slots = [slot for slot in all_slots if slot not in occupied_times]
    
    return available_slots