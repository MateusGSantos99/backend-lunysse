from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.models import User, Patient, UserType
from schemas.schemas import UserCreate, UserLogin, Token, User as UserSchema
from services.auth_service import authenticate_user
from utils import get_password_hash, create_access_token, calculate_age
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    
    access_token = create_access_token(
        data={"sub": user.email}, 
        expires_delta=timedelta(minutes=30)
    )
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserSchema.from_orm(user)
    )

@router.post("/register", response_model=Token)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Verifica se usuário já existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    # Cria novo usuário
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        password=hashed_password,
        name=user_data.name,
        type=user_data.type,
        specialty=user_data.specialty,
        crp=user_data.crp,
        phone=user_data.phone
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Se for paciente, cria registro na tabela de pacientes
    if user_data.type == UserType.PACIENTE and user_data.birth_date:
        age = calculate_age(user_data.birth_date)
        db_patient = Patient(
            id=db_user.id,
            name=user_data.name,
            email=user_data.email,
            phone=user_data.phone or "",
            birth_date=user_data.birth_date,
            age=age,
            status="Ativo"
        )
        db.add(db_patient)
        db.commit()
    
    access_token = create_access_token(
        data={"sub": db_user.email},
        expires_delta=timedelta(minutes=30)
    )
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserSchema.from_orm(db_user)
    )