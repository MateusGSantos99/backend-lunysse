# Importações necessárias
from fastapi import APIRouter, Depends, HTTPException, status  # Importa classes do FastAPI para criar rotas, lidar com dependências e erros HTTP
from sqlalchemy.orm import Session  # Importa Session do SQLAlchemy para interação com o banco de dados
from typing import List  # Para tipagem de listas na resposta das rotas
from core.database import get_db  # Função que retorna uma sessão do banco de dados
from models.models import Patient, User, Appointment, UserType  # Importa os modelos do banco de dados
from schemas.schemas import PatientCreate, Patient as PatientSchema  # Importa schemas para validação e resposta
from services.auth_service import get_current_user  # Função que retorna o usuário autenticado
from Utils import calculate_age  # Função auxiliar para calcular idade a partir da data de nascimento

# Criação do roteador FastAPI para a entidade "patients"
router = APIRouter(prefix="/patients", tags=["patients"])

# ======================================
# Rota para listar pacientes do psicólogo
# ======================================
@router.get("/", response_model=List[PatientSchema])
async def get_patients(
    current_user: User = Depends(get_current_user),  # Recupera o usuário autenticado
    db: Session = Depends(get_db)  # Cria uma sessão com o banco de dados
):
    # Verifica se o usuário autenticado é um psicólogo
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem acessar lista de pacientes"
        )
    
    # Consulta todos os pacientes que pertencem ao psicólogo autenticado
    patients = db.query(Patient).filter(
        Patient.psychologist_id == current_user.id
    ).all()
    
    # Calcula o total de sessões para cada paciente
    for patient in patients:
        total_sessions = db.query(Appointment).filter(
            Appointment.patient_id == patient.id,
            Appointment.psychologist_id == current_user.id
        ).count()
        # Adiciona atributo "total_sessions" dinamicamente ao paciente
        patient.total_sessions = total_sessions
    
    # Retorna a lista de pacientes com o total de sessões
    return patients

# ======================================
# Rota para criar um novo paciente
# ======================================
@router.post("/", response_model=PatientSchema)
async def create_patient(
    patient_data: PatientCreate,  # Recebe os dados do paciente via schema
    current_user: User = Depends(get_current_user),  # Usuário autenticado
    db: Session = Depends(get_db)  # Sessão do banco
):
    # Verifica se o usuário é psicólogo
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem cadastrar pacientes"
        )
    
    # Verifica se já existe um paciente com o mesmo email para este psicólogo
    existing_patient = db.query(Patient).filter(
        Patient.email == patient_data.email,
        Patient.psychologist_id == patient_data.psychologist_id
    ).first()
    
    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Paciente com este email já está cadastrado"
        )
    
    # Calcula a idade do paciente usando a função utilitária
    age = calculate_age(patient_data.birth_date)
    
    # Cria o objeto paciente para adicionar ao banco
    db_patient = Patient(
        name=patient_data.name,
        email=patient_data.email,
        phone=patient_data.phone,
        birth_date=patient_data.birth_date,
        age=age,
        status="Ativo",  # Define status padrão
        psychologist_id=patient_data.psychologist_id
    )
    
    # Adiciona o paciente no banco e confirma a transação
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)  # Atualiza o objeto com dados do banco (ex: id gerado)
    
    return db_patient

# ======================================
# Rota para listar sessões de um paciente
# ======================================
@router.get("/{patient_id}/sessions")
async def get_patient_sessions(
    patient_id: int,  # Recebe o id do paciente
    current_user: User = Depends(get_current_user),  # Usuário autenticado
    db: Session = Depends(get_db)  # Sessão do banco
):
    # Somente psicólogos podem acessar
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem acessar sessões de pacientes"
        )
    
    # Consulta todas as sessões do paciente específico para o psicólogo
    sessions = db.query(Appointment).filter(
        Appointment.patient_id == patient_id,
        Appointment.psychologist_id == current_user.id
    ).all()
    
    return sessions

# ======================================
# Rota para adicionar uma anotação a um paciente
# ======================================
@router.post("/{patient_id}/notes")
async def add_patient_note(
    patient_id: int,  # Recebe o id do paciente
    note_data: dict,  # Recebe os dados da anotação
    current_user: User = Depends(get_current_user),  # Usuário autenticado
    db: Session = Depends(get_db)  # Sessão do banco
):
    # Apenas psicólogos podem adicionar anotações
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem adicionar anotações"
        )
    
    # Verifica se o paciente pertence ao psicólogo autenticado
    patient = db.query(Patient).filter(
        Patient.id == patient_id,
        Patient.psychologist_id == current_user.id
    ).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado"
        )
    
    # TODO: Implementar sistema de anotações separadamente no banco
    # Atualmente, apenas retorna uma mensagem de sucesso
    return {"id": patient_id, "message": "Anotação adicionada com sucesso"}
