from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from models.models import Request, User, UserType, RequestStatus
from schemas.schemas import RequestCreate, RequestUpdate, Request as RequestSchema
from services.auth_service import get_current_user
from services.email_service import send_email_new_request_to_psychologist, send_email_request_accepted, send_email_request_reject
import json
from datetime import datetime
 
router = APIRouter(prefix="/requests", tags=["requests"])
 
@router.get("/", response_model=List[RequestSchema])
async def get_requests(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type == UserType.PSICOLOGO:
        # Psicólogos veem solicitações direcionadas a eles
        requests = db.query(Request).filter(
            Request.preferred_psychologist == current_user.id
        ).all()
    elif current_user.type == UserType.PACIENTE:
        # Pacientes veem suas próprias solicitações
        requests = db.query(Request).filter(
            Request.patient_email == current_user.email
        ).all()
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso não autorizado"
        )
   
    # Converte JSON strings de volta para listas
    for req in requests:
        req.preferred_dates = json.loads(req.preferred_dates) if req.preferred_dates else []
        req.preferred_times = json.loads(req.preferred_times) if req.preferred_times else []
   
    return requests
 
@router.post("/", response_model=RequestSchema)
async def create_request(
    request_data: RequestCreate,
    db: Session = Depends(get_db)
):
    # Verifica se já existe solicitação pendente
    existing_request = db.query(Request).filter(
        Request.patient_email == request_data.patient_email,
        Request.preferred_psychologist == request_data.preferred_psychologist,
        Request.status == RequestStatus.PENDENTE
    ).first()
   
    if existing_request:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você já possui uma solicitação pendente para este psicólogo"
        )
   
    db_request = Request(
        patient_id=request_data.patient_id,
        patient_name=request_data.patient_name,
        patient_email=request_data.patient_email,
        patient_phone=request_data.patient_phone,
        preferred_psychologist=request_data.preferred_psychologist,
        description=request_data.description,
        urgency=request_data.urgency,
        preferred_dates=json.dumps(request_data.preferred_dates),
        preferred_times=json.dumps(request_data.preferred_times),
        status=RequestStatus.PENDENTE
    )
   
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
   
    # Buscar dados do psicólogo para envio de email
    psychologist = db.query(User).filter(User.id == request_data.preferred_psychologist).first()
    if psychologist:
        try:
            send_email_new_request_to_psychologist(
                psychologist_email=psychologist.email,
                psychologist_name=psychologist.name,
                patient_name=request_data.patient_name
            )
        except Exception as e:
            print(f"Erro ao enviar email para psicólogo: {e}")
   
    # Converte de volta para retorno
    db_request.preferred_dates = request_data.preferred_dates
    db_request.preferred_times = request_data.preferred_times
   
    return db_request
 
@router.put("/{request_id}", response_model=RequestSchema)
async def update_request_status(
    request_id: int,
    update_data: RequestUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem atualizar solicitações"
        )
   
    request = db.query(Request).filter(
        Request.id == request_id,
        Request.preferred_psychologist == current_user.id
    ).first()
   
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solicitação não encontrada"
        )
   
    request.status = update_data.status
    request.notes = update_data.notes or ""
    request.updated_at = datetime.utcnow()
   
    db.commit()
    db.refresh(request)
   
    # Enviar email baseado no status
    try:
        if update_data.status == RequestStatus.ACEITO:
            send_email_request_accepted(
                patient_email=request.patient_email,
                patient_name=request.patient_name,
                psychologist_name=current_user.name
            )
        elif update_data.status == RequestStatus.REJEITADO:
            send_email_request_reject(
                patient_email=request.patient_email,
                patient_name=request.patient_name,
                psychologist_name=current_user.name
            )
    except Exception as e:
        print(f"Erro ao enviar email para paciente: {e}")
   
    # Converte JSON strings de volta para listas
    request.preferred_dates = json.loads(request.preferred_dates) if request.preferred_dates else []
    request.preferred_times = json.loads(request.preferred_times) if request.preferred_times else []
   
    return request
 