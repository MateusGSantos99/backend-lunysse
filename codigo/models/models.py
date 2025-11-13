from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime, timezone
import enum

class UserType(str, enum.Enum):
    PSICOLOGO = "psicologo"
    PACIENTE = "paciente"

class AppointmentStatus(str, enum.Enum):
    AGENDADO = "agendado"
    CONCLUIDO = "concluido"
    CANCELADO = "cancelado"
    REAGENDADO = "reagendado"

class RequestStatus(str, enum.Enum):
    PENDENTE = "pendente"
    ACEITO = "aceito"
    REJEITADO = "rejeitado"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    type = Column(Enum(UserType))
    name = Column(String)
    specialty = Column(String, nullable=True)
    crp = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    birth_date = Column(Date)
    age = Column(Integer)
    status = Column(String)
    psychologist_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    psychologist = relationship("User", foreign_keys=[psychologist_id])

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    psychologist_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    time = Column(String)
    status = Column(Enum(AppointmentStatus))
    description = Column(String)
    duration = Column(Integer, default=50)
    notes = Column(Text, default="")
    full_report = Column(Text, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    patient = relationship("Patient")
    psychologist = relationship("User")

class Request(Base):
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    patient_email = Column(String)
    patient_phone = Column(String)
    preferred_psychologist = Column(Integer, ForeignKey("users.id"))
    description = Column(Text)
    urgency = Column(String)
    preferred_dates = Column(Text)  # JSON string
    preferred_times = Column(Text)  # JSON string
    status = Column(Enum(RequestStatus), default=RequestStatus.PENDENTE)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=True)
    
    psychologist = relationship("User")