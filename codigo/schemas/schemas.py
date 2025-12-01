from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, List
from models.models import UserType, AppointmentStatus, RequestStatus

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    name: str
    type: UserType

class UserCreate(UserBase):
    password: str
    specialty: Optional[str] = None
    crp: Optional[str] = None
    phone: Optional[str] = None
    birth_date: Optional[date] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    specialty: Optional[str] = None
    crp: Optional[str] = None
    phone: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User

# Patient schemas
class PatientBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    birth_date: date

class PatientCreate(PatientBase):
    psychologist_id: int

class Patient(PatientBase):
    id: int
    age: int
    status: str
    notes: Optional[str] = ""
    psychologist_id: Optional[int] = None
    total_sessions: Optional[int] = 0
    last_session: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True
        
class PatientUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    birth_date: Optional[date] = None
    psychologist_id: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


# Appointment schemas
class AppointmentBase(BaseModel):
    patient_id: int
    psychologist_id: int
    date: date
    time: str
    description: str
    duration: Optional[int] = 50

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    date: Optional[date] = None
    time: Optional[str] = None
    status: Optional[AppointmentStatus] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    notes: Optional[str] = None
    full_report: Optional[str] = None

class Appointment(AppointmentBase):
    id: int
    status: AppointmentStatus
    notes: str
    full_report: str
    created_at: datetime

    class Config:
        from_attributes = True

# Request schemas
class RequestBase(BaseModel):
    patient_id: int
    patient_name: str
    patient_email: EmailStr
    patient_phone: str
    preferred_psychologist: int
    description: str
    urgency: str
    preferred_dates: List[str]
    preferred_times: List[str]

class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    status: RequestStatus
    notes: Optional[str] = None

class Request(RequestBase):
    id: int
    status: RequestStatus
    notes: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Psychologist schemas
class Psychologist(BaseModel):
    id: int
    name: str
    specialty: str
    crp: str

    class Config:
        from_attributes = True

# Report schemas
class ReportStats(BaseModel):
    active_patients: int
    total_sessions: int
    completed_sessions: int
    attendance_rate: str
    risk_alerts: int

class FrequencyData(BaseModel):
    month: str
    sessions: int

class StatusData(BaseModel):
    name: str
    value: int
    color: str

class RiskAlert(BaseModel):
    id: int
    patient: str
    risk: str
    reason: str
    date: str

class ReportsData(BaseModel):
    stats: ReportStats
    frequency_data: List[FrequencyData]
    status_data: List[StatusData]
    patients_data: List[StatusData]
    risk_alerts: List[RiskAlert]