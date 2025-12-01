from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from models.models import Patient, User, Appointment, UserType
from schemas.schemas import PatientCreate, Patient as PatientSchema, PatientUpdate
from services.auth_service import get_current_user
from utils import calculate_age

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/", response_model=List[PatientSchema])
async def get_patients(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem acessar lista de pacientes"
        )
    
    patients = db.query(Patient).filter(
        Patient.psychologist_id == current_user.id
    ).all()
    
    # Calcula total de sessões para cada paciente
    for patient in patients:
        total_sessions = db.query(Appointment).filter(
            Appointment.patient_id == patient.id,
            Appointment.psychologist_id == current_user.id
        ).count()
        patient.total_sessions = total_sessions
    
    return patients

@router.get("/{patient_id}", response_model=PatientSchema)
async def get_patient_details(
    patient_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado"
        )
    
    # Verifica permissões
    if current_user.type == UserType.PSICOLOGO:
        if patient.psychologist_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você não tem acesso a este paciente"
            )
    elif current_user.type == UserType.PACIENTE:
        if patient.email != current_user.email:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você só pode acessar seus próprios dados"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso não autorizado"
        )
    
    # Adiciona estatísticas
    total_sessions = db.query(Appointment).filter(
        Appointment.patient_id == patient.id
    ).count()
    
    last_appointment = db.query(Appointment).filter(
        Appointment.patient_id == patient.id
    ).order_by(Appointment.created_at.desc()).first()
    
    patient.total_sessions = total_sessions
    patient.last_session = last_appointment.created_at if last_appointment else None
    
    return patient

@router.post("/", response_model=PatientSchema)
async def create_patient(
    patient_data: PatientCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem cadastrar pacientes"
        )
    
    # Verifica se paciente já existe para este psicólogo
    existing_patient = db.query(Patient).filter(
        Patient.email == patient_data.email,
        Patient.psychologist_id == patient_data.psychologist_id
    ).first()
    
    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Paciente com este email já está cadastrado"
        )
    
    age = calculate_age(patient_data.birth_date)
    
    db_patient = Patient(
        name=patient_data.name,
        email=patient_data.email,
        phone=patient_data.phone,
        birth_date=patient_data.birth_date,
        age=age,
        status="Ativo",
        psychologist_id=patient_data.psychologist_id
    )
    
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    
    return db_patient

@router.get("/{patient_id}/sessions")
async def get_patient_sessions(
    patient_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem acessar sessões de pacientes"
        )
    
    sessions = db.query(Appointment).filter(
        Appointment.patient_id == patient_id,
        Appointment.psychologist_id == current_user.id
    ).all()
    
    return sessions

@router.post("/{patient_id}/notes")
async def add_patient_note(
    patient_id: int,
    note_data: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem adicionar anotações"
        )
    
    # Verifica se paciente pertence ao psicólogo
    patient = db.query(Patient).filter(
        Patient.id == patient_id,
        Patient.psychologist_id == current_user.id
    ).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado"
        )
    
    note = note_data.get("note", "")
    if not note.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Anotação não pode estar vazia"
        )
    
    # Atualiza as anotações do paciente
    from datetime import datetime
    current_notes = patient.notes or ""
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    new_note = f"[{timestamp}] {note}"
    
    if current_notes:
        patient.notes = f"{current_notes}\n\n{new_note}"
    else:
        patient.notes = new_note
    
    db.commit()
    db.refresh(patient)
    
    return {
        "id": patient_id, 
        "message": "Anotação adicionada com sucesso",
        "note": new_note
    }
    
    
@router.put("/{patient_id}", response_model=PatientSchema)
async def update_patient(
    patient_id: int,
    update_data: PatientUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verifica se paciente existe
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado"
        )

    # Permissões
    if current_user.type == UserType.PSICOLOGO:
        if patient.psychologist_id not in [None, current_user.id]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você não tem permissão para editar este paciente"
            )

    # Atualiza somente os campos enviados
    update_fields = update_data.dict(exclude_unset=True)

    for field, value in update_fields.items():
        setattr(patient, field, value)

    db.commit()
    db.refresh(patient)

    return patient