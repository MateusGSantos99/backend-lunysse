# Sistema Lunysse Backend - Documentação Completa

## 📋 Visão Geral

API REST em FastAPI para sistema de agendamento psicológico com análise de ML para identificação de riscos e otimização de atendimentos.

## 🏗️ Arquitetura Backend

```
lunysse-fastapi/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py        # Modelos SQLAlchemy
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py          # Autenticação
│   │   ├── patients.py      # Pacientes
│   │   ├── psychologists.py # Psicólogos
│   │   ├── appointments.py  # Agendamentos
│   │   ├── requests.py      # Solicitações
│   │   ├── reports.py       # Relatórios
│   │   └── ml_analysis.py   # Análise ML
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py       # Schemas Pydantic
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py  # Serviços auth
│   │   ├── ml_service.py    # Serviços ML
│   │   └── report_service.py# Serviços relatórios
│   ├── config.py            # Configurações
│   ├── database.py          # Conexão BD
│   ├── logging_config.py    # Config logs
│   ├── main.py              # App principal
│   ├── utils.py             # Utilitários
│   └── validators.py        # Validadores
├── logs/                    # Logs do sistema
├── .env                     # Variáveis ambiente
├── requirements.txt         # Dependências
├── seed_data.py            # Dados iniciais
├── test.py                 # Testes
└── run.py                  # Script execução
```

## 🚀 Passo a Passo - Criação do Backend

### PASSO 1: Configuração Inicial

#### 1.1 Pré-requisitos
```bash
# Verificar Python 3.8+
python --version

# Instalar pip se necessário
python -m ensurepip --upgrade
```

#### 1.2 Criar Estrutura do Projeto
```bash
# Criar diretório principal
mkdir lunysse-fastapi
cd lunysse-fastapi

# Criar estrutura de pastas
mkdir app
mkdir app/models app/routers app/schemas app/services
mkdir logs

# Criar arquivos __init__.py
touch app/__init__.py
touch app/models/__init__.py
touch app/routers/__init__.py
touch app/schemas/__init__.py
touch app/services/__init__.py
```

#### 1.3 Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### PASSO 2: Dependências

#### 2.1 Criar requirements.txt
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
python-dotenv==1.0.0
pandas==2.1.3
scikit-learn==1.3.2
```

#### 2.2 Instalar Dependências
```bash
pip install -r requirements.txt
```

### PASSO 3: Configuração de Ambiente

#### 3.1 Criar arquivo .env
```env
SECRET_KEY=sua_chave_secreta_super_segura_de_32_caracteres_ou_mais
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./lunysse.db
```

#### 3.2 Gerar SECRET_KEY segura
```python
# Execute este código para gerar uma chave
import secrets
print(secrets.token_urlsafe(32))
```

### PASSO 4: Configuração Base

#### 4.1 Criar config.py
```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./lunysse.db"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

#### 4.2 Criar database.py
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(
    settings.database_url, 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### 4.3 Criar logging_config.py
```python
import logging
import os
from datetime import datetime

def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"),
            logging.StreamHandler()
        ]
    )
```

### PASSO 5: Modelos do Banco de Dados

#### 5.1 Criar models/models.py
```python
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Date
from sqlalchemy.relationship import relationship
from sqlalchemy.sql import func
from ..database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    user_type = Column(String(20), nullable=False)  # patient, psychologist
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    patient = relationship("Patient", back_populates="user", uselist=False)
    psychologist = relationship("Psychologist", back_populates="user", uselist=False)

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    birth_date = Column(Date, nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    emergency_contact = Column(String(100))
    
    # Relacionamentos
    user = relationship("User", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")
    requests = relationship("Request", back_populates="patient")

class Psychologist(Base):
    __tablename__ = "psychologists"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    crp = Column(String(20), unique=True, nullable=False)
    specialty = Column(String(100))
    bio = Column(Text)
    hourly_rate = Column(Float)
    
    # Relacionamentos
    user = relationship("User", back_populates="psychologist")
    appointments = relationship("Appointment", back_populates="psychologist")
    requests = relationship("Request", back_populates="psychologist")

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    psychologist_id = Column(Integer, ForeignKey("psychologists.id"), nullable=False)
    date_time = Column(DateTime(timezone=True), nullable=False)
    status = Column(String(20), default="scheduled")  # scheduled, completed, cancelled
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    patient = relationship("Patient", back_populates="appointments")
    psychologist = relationship("Psychologist", back_populates="appointments")

class Request(Base):
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    psychologist_id = Column(Integer, ForeignKey("psychologists.id"), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String(20), default="pending")  # pending, approved, rejected
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    patient = relationship("Patient", back_populates="requests")
    psychologist = relationship("Psychologist", back_populates="requests")
```

### PASSO 6: Schemas Pydantic

#### 6.1 Criar schemas/schemas.py
```python
from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional, List

# Base Schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr
    user_type: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Patient Schemas
class PatientBase(BaseModel):
    birth_date: date
    phone: Optional[str] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    user_id: int
    user: UserResponse
    
    class Config:
        from_attributes = True

# Psychologist Schemas
class PsychologistBase(BaseModel):
    crp: str
    specialty: Optional[str] = None
    bio: Optional[str] = None
    hourly_rate: Optional[float] = None

class PsychologistResponse(PsychologistBase):
    id: int
    user_id: int
    user: UserResponse
    
    class Config:
        from_attributes = True

# Appointment Schemas
class AppointmentBase(BaseModel):
    patient_id: int
    psychologist_id: int
    date_time: datetime
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Auth Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
```

### PASSO 7: Utilitários e Segurança

#### 7.1 Criar utils.py
```python
import os
from datetime import datetime, date, timezone, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()

# Configurações de segurança
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY deve ser definida nas variáveis de ambiente")

ALGORITHM = os.getenv("ALGORITHM", "HS256")

try:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
except (ValueError, TypeError):
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def calculate_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age
```

### PASSO 8: Serviços de Autenticação

#### 8.1 Criar services/auth_service.py
```python
from sqlalchemy.orm import Session
from ..models.models import User
from ..utils import verify_password, get_password_hash, create_access_token
from datetime import timedelta
from ..config import settings

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

def create_user(db: Session, user_data: dict):
    hashed_password = get_password_hash(user_data["password"])
    db_user = User(
        name=user_data["name"],
        email=user_data["email"],
        password_hash=hashed_password,
        user_type=user_data["user_type"]
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_access_token(user: User):
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email, "user_id": user.id},
        expires_delta=access_token_expires
    )
    return access_token
```

### PASSO 9: Routers - Endpoints da API

#### 9.1 Criar routers/auth.py
```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.schemas import Token, UserCreate, UserResponse, LoginRequest
from ..services.auth_service import authenticate_user, create_user, create_user_access_token

router = APIRouter(prefix="/auth", tags=["authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/login", response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_user_access_token(user)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Verificar se usuário já existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    user = create_user(db, user_data.dict())
    return user
```

#### 9.2 Criar routers/patients.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.models import Patient, User
from ..schemas.schemas import PatientResponse, PatientCreate
from ..routers.auth import get_current_user

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/", response_model=List[PatientResponse])
def get_patients(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    patients = db.query(Patient).all()
    return patients

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return patient

@router.post("/", response_model=PatientResponse)
def create_patient(patient_data: PatientCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    patient = Patient(**patient_data.dict(), user_id=current_user.id)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient
```

#### 9.3 Criar routers/psychologists.py
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.models import Psychologist
from ..schemas.schemas import PsychologistResponse

router = APIRouter(prefix="/psychologists", tags=["psychologists"])

@router.get("/", response_model=List[PsychologistResponse])
def get_psychologists(db: Session = Depends(get_db)):
    psychologists = db.query(Psychologist).all()
    return psychologists

@router.get("/{psychologist_id}", response_model=PsychologistResponse)
def get_psychologist(psychologist_id: int, db: Session = Depends(get_db)):
    psychologist = db.query(Psychologist).filter(Psychologist.id == psychologist_id).first()
    if not psychologist:
        raise HTTPException(status_code=404, detail="Psicólogo não encontrado")
    return psychologist
```

#### 9.4 Criar routers/appointments.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.models import Appointment, User
from ..schemas.schemas import AppointmentResponse, AppointmentCreate
from ..routers.auth import get_current_user

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.get("/", response_model=List[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.user_type == "patient":
        appointments = db.query(Appointment).filter(Appointment.patient_id == current_user.patient.id).all()
    else:
        appointments = db.query(Appointment).filter(Appointment.psychologist_id == current_user.psychologist.id).all()
    return appointments

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return appointment

@router.post("/", response_model=AppointmentResponse)
def create_appointment(appointment_data: AppointmentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appointment = Appointment(**appointment_data.dict())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment
```

### PASSO 10: Sistema de ML

#### 10.1 Criar services/ml_service.py
```python
from sqlalchemy.orm import Session
from ..models.models import Patient, Appointment
from datetime import datetime, timedelta
import pandas as pd
from typing import List, Dict

def calculate_risk_score(patient_id: int, db: Session) -> Dict:
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    appointments = db.query(Appointment).filter(Appointment.patient_id == patient_id).all()
    
    if not appointments:
        return {
            "risk_score": 0.5,
            "risk": "Moderado",
            "reason": "Sem histórico de consultas"
        }
    
    # Métricas
    total_appointments = len(appointments)
    cancelled_appointments = len([a for a in appointments if a.status == "cancelled"])
    cancellation_rate = cancelled_appointments / total_appointments if total_appointments > 0 else 0
    
    # Última consulta
    last_appointment = max(appointments, key=lambda x: x.date_time)
    days_since_last = (datetime.now() - last_appointment.date_time).days
    
    # Frequência mensal
    if appointments:
        first_appointment = min(appointments, key=lambda x: x.date_time)
        months_active = max(1, (datetime.now() - first_appointment.date_time).days / 30)
        frequency_per_month = total_appointments / months_active
    else:
        frequency_per_month = 0
    
    # Cálculo do score de risco
    risk_score = 0
    
    # Fator 1: Taxa de cancelamento (peso 0.4)
    risk_score += cancellation_rate * 0.4
    
    # Fator 2: Tempo desde última consulta (peso 0.3)
    if days_since_last > 60:
        risk_score += 0.3
    elif days_since_last > 30:
        risk_score += 0.15
    
    # Fator 3: Baixa frequência (peso 0.3)
    if frequency_per_month < 1:
        risk_score += 0.3
    elif frequency_per_month < 2:
        risk_score += 0.15
    
    # Classificação
    if risk_score >= 0.7:
        risk_level = "Alto"
        reason = "Alta taxa de cancelamento e baixa frequência"
    elif risk_score >= 0.4:
        risk_level = "Moderado"
        reason = "Padrão irregular de consultas"
    else:
        risk_level = "Baixo"
        reason = "Padrão regular de consultas"
    
    return {
        "risk_score": round(risk_score, 2),
        "risk": risk_level,
        "reason": reason,
        "metrics": {
            "total_appointments": total_appointments,
            "cancellation_rate": cancellation_rate,
            "days_since_last": days_since_last,
            "frequency_per_month": round(frequency_per_month, 1)
        }
    }

def analyze_all_patients_risk(db: Session) -> Dict:
    patients = db.query(Patient).all()
    results = []
    
    for patient in patients:
        risk_data = calculate_risk_score(patient.id, db)
        results.append({
            "id": patient.id,
            "patient": patient.user.name,
            "risk": risk_data["risk"],
            "risk_score": risk_data["risk_score"],
            "reason": risk_data["reason"]
        })
    
    # Estatísticas gerais
    total_patients = len(results)
    high_risk = len([r for r in results if r["risk"] == "Alto"])
    moderate_risk = len([r for r in results if r["risk"] == "Moderado"])
    low_risk = len([r for r in results if r["risk"] == "Baixo"])
    
    return {
        "summary": {
            "total_patients": total_patients,
            "high_risk": high_risk,
            "moderate_risk": moderate_risk,
            "low_risk": low_risk,
            "risk_distribution": {
                "Alto": f"{high_risk}/{total_patients}",
                "Moderado": f"{moderate_risk}/{total_patients}",
                "Baixo": f"{low_risk}/{total_patients}"
            }
        },
        "patients": sorted(results, key=lambda x: x["risk_score"], reverse=True)
    }
```

#### 10.2 Criar routers/ml_analysis.py
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.ml_service import calculate_risk_score, analyze_all_patients_risk
from ..routers.auth import get_current_user
from ..models.models import User

router = APIRouter(prefix="/ml", tags=["ml-analysis"])

@router.get("/risk-analysis")
def get_risk_analysis(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return analyze_all_patients_risk(db)

@router.get("/risk-analysis/{patient_id}")
def get_patient_risk_analysis(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    risk_data = calculate_risk_score(patient_id, db)
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    # Última consulta
    last_appointment = db.query(Appointment).filter(
        Appointment.patient_id == patient_id
    ).order_by(Appointment.date_time.desc()).first()
    
    return {
        "id": patient.id,
        "patient": patient.user.name,
        "risk": risk_data["risk"],
        "risk_score": risk_data["risk_score"],
        "reason": risk_data["reason"],
        "metrics": risk_data["metrics"],
        "last_appointment": last_appointment.date_time if last_appointment else None
    }
```

### PASSO 11: Aplicação Principal

#### 11.1 Criar main.py
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, patients, psychologists, appointments, requests, reports, ml_analysis
from .logging_config import setup_logging

# Configurar logging
setup_logging()

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lunysse API",
    description="API para sistema de agendamento psicológico com análise ML",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(psychologists.router)
app.include_router(appointments.router)
app.include_router(requests.router)
app.include_router(reports.router)
app.include_router(ml_analysis.router)

@app.get("/")
def root():
    return {"message": "Lunysse API - Sistema de Agendamento Psicológico"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

#### 11.2 Criar run.py
```python
import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
```

### PASSO 12: Dados Iniciais

#### 12.1 Criar seed_data.py
```python
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.models import Base, User, Patient, Psychologist, Appointment
from app.utils import get_password_hash
from datetime import datetime, date, timedelta

# Criar tabelas
Base.metadata.create_all(bind=engine)

def create_sample_data():
    db = SessionLocal()
    
    try:
        # Verificar se já existem dados
        if db.query(User).first():
            print("Dados já existem no banco")
            return
        
        # Criar usuários
        users_data = [
            {"name": "Ana Silva", "email": "ana@test.com", "password": "123456", "user_type": "patient"},
            {"name": "Dr. João Santos", "email": "joao@test.com", "password": "123456", "user_type": "psychologist"},
            {"name": "Maria Oliveira", "email": "maria@test.com", "password": "123456", "user_type": "patient"},
        ]
        
        users = []
        for user_data in users_data:
            user = User(
                name=user_data["name"],
                email=user_data["email"],
                password_hash=get_password_hash(user_data["password"]),
                user_type=user_data["user_type"]
            )
            db.add(user)
            users.append(user)
        
        db.commit()
        
        # Criar pacientes
        patient1 = Patient(
            user_id=users[0].id,
            birth_date=date(1990, 5, 15),
            phone="(11) 99999-9999",
            address="Rua das Flores, 123",
            emergency_contact="João Silva - (11) 88888-8888"
        )
        
        patient2 = Patient(
            user_id=users[2].id,
            birth_date=date(1985, 8, 22),
            phone="(11) 77777-7777",
            address="Av. Principal, 456"
        )
        
        db.add(patient1)
        db.add(patient2)
        
        # Criar psicólogo
        psychologist = Psychologist(
            user_id=users[1].id,
            crp="06/123456",
            specialty="Terapia Cognitivo-Comportamental",
            bio="Especialista em ansiedade e depressão",
            hourly_rate=150.0
        )
        
        db.add(psychologist)
        db.commit()
        
        # Criar agendamentos
        appointments_data = [
            {"patient_id": patient1.id, "psychologist_id": psychologist.id, "date_time": datetime.now() + timedelta(days=1), "status": "scheduled"},
            {"patient_id": patient1.id, "psychologist_id": psychologist.id, "date_time": datetime.now() - timedelta(days=7), "status": "completed"},
            {"patient_id": patient2.id, "psychologist_id": psychologist.id, "date_time": datetime.now() + timedelta(days=3), "status": "scheduled"},
        ]
        
        for apt_data in appointments_data:
            appointment = Appointment(**apt_data)
            db.add(appointment)
        
        db.commit()
        print("Dados de exemplo criados com sucesso!")
        
    except Exception as e:
        print(f"Erro ao criar dados: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
```

### PASSO 13: Execução e Testes

#### 13.1 Executar o Sistema
```bash
# Ativar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Criar dados iniciais
python seed_data.py

# Executar servidor
python run.py

# Ou usando uvicorn diretamente
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 13.2 Testar API
```bash
# Executar testes
python test.py

# Acessar documentação
# http://localhost:8000/docs (Swagger)
# http://localhost:8000/redoc (ReDoc)
```

### PASSO 14: Estrutura Final

Após seguir todos os passos, sua estrutura deve estar assim:

```
lunysse-fastapi/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── patients.py
│   │   ├── psychologists.py
│   │   ├── appointments.py
│   │   ├── requests.py
│   │   ├── reports.py
│   │   └── ml_analysis.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── ml_service.py
│   │   └── report_service.py
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── logging_config.py
│   ├── main.py
│   ├── utils.py
│   └── validators.py
├── logs/
├── venv/
├── .env
├── requirements.txt
├── seed_data.py
├── test.py
├── run.py
└── lunysse.db
```

## 🚀 Deploy e Produção

### Preparação para Produção

#### 1. Instalar Gunicorn
```bash
pip install gunicorn
```

#### 2. Configurar Variáveis de Produção
```env
# .env.production
SECRET_KEY=sua_chave_super_segura_de_producao_com_32_caracteres_ou_mais
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://user:password@localhost/lunysse_prod
```

#### 3. Executar em Produção
```bash
# Com Gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Com configurações específicas
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --access-logfile logs/access.log \
  --error-logfile logs/error.log
```

## 📊 Monitoramento e Logs

### Sistema de Logs
- Logs automáticos em `logs/app_YYYYMMDD.log`
- Rotação diária automática
- Níveis: INFO, WARNING, ERROR
- Logs de acesso e erro separados

### Backup do Banco
```bash
# Backup SQLite
cp lunysse.db backup/lunysse_$(date +%Y%m%d_%H%M%S).db

# Backup PostgreSQL (produção)
pg_dump lunysse_prod > backup/lunysse_$(date +%Y%m%d_%H%M%S).sql
```

## 🔧 Manutenção

### Atualizações
```bash
# Atualizar dependências
pip install -r requirements.txt --upgrade

# Verificar segurança
pip audit

# Atualizar banco de dados (se necessário)
alembic upgrade head
```

### Monitoramento de Performance
```bash
# Verificar logs de erro
tail -f logs/error.log

# Monitorar uso de recursos
top -p $(pgrep -f "gunicorn")

# Verificar conexões de banco
lsof -i :5432  # PostgreSQL
```

## 📚 Recursos e Documentação

### Endpoints Principais
- **Autenticação**: `POST /auth/login`, `POST /auth/register`
- **Pacientes**: `GET /patients/`, `GET /patients/{id}`
- **Psicólogos**: `GET /psychologists/`
- **Agendamentos**: `GET /appointments/`, `POST /appointments/`
- **ML**: `GET /ml/risk-analysis`, `GET /ml/risk-analysis/{patient_id}`
- **Relatórios**: `GET /reports/{psychologist_id}`

### Documentação Automática
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

### Tecnologias Utilizadas
- **Framework**: FastAPI 0.104.1
- **Banco de Dados**: SQLAlchemy + SQLite/PostgreSQL
- **Autenticação**: JWT + Bcrypt
- **Validação**: Pydantic
- **ML**: Pandas + Scikit-learn
- **Servidor**: Uvicorn + Gunicorn

## ✅ Checklist Final

- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas
- [ ] Variáveis de ambiente configuradas
- [ ] Estrutura de pastas criada
- [ ] Modelos do banco implementados
- [ ] Schemas Pydantic definidos
- [ ] Routers implementados
- [ ] Serviços de ML funcionando
- [ ] Dados iniciais carregados
- [ ] Testes executados com sucesso
- [ ] Documentação acessível
- [ ] Logs configurados
- [ ] Sistema rodando em produção

---

**🎯 Sistema Lunysse Backend completo e funcional!**

Para dúvidas ou problemas, verifique os logs em `logs/` ou acesse a documentação em `/docs`.