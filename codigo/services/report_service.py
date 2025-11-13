from sqlalchemy.orm import Session
from models.models import Appointment, Patient, AppointmentStatus
from schemas.schemas import ReportsData, ReportStats, FrequencyData, StatusData, RiskAlert
from services.ml_services import calculate_patient_risk
from typing import List
import random
from datetime import datetime, date

def generate_reports_data(db: Session, psychologist_id: int) -> ReportsData:
    # Busca dados do psicólogo
    appointments = db.query(Appointment).filter(Appointment.psychologist_id == psychologist_id).all()
    patients = db.query(Patient).filter(Patient.psychologist_id == psychologist_id).all()
    
    # Calcula estatísticas
    total_sessions = len(appointments)
    completed_sessions = len([apt for apt in appointments if apt.status == AppointmentStatus.CONCLUIDO])
    canceled_sessions = len([apt for apt in appointments if apt.status == AppointmentStatus.CANCELADO])
    scheduled_sessions = len([apt for apt in appointments if apt.status == AppointmentStatus.AGENDADO])
    
    # Pacientes com sessões
    patients_with_sessions = set(apt.patient_id for apt in appointments)
    patients_without_sessions = len([p for p in patients if p.id not in patients_with_sessions])
    
    # Análise de risco com ML (movido para cima)
    ml_risk_analysis = calculate_patient_risk(db, psychologist_id)
    high_risk_patients = [p for p in ml_risk_analysis if p["risk"] in ["Alto", "Moderado"]]
    
    # Estatísticas principais
    stats = ReportStats(
        active_patients=len(patients),
        total_sessions=total_sessions,
        completed_sessions=completed_sessions,
        attendance_rate=f"{(completed_sessions / total_sessions * 100):.1f}" if total_sessions > 0 else "0.0",
        risk_alerts=len(high_risk_patients)
    )
    
    # Dados de frequência (simulados)
    months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    frequency_data = [FrequencyData(month=month, sessions=random.randint(10, 30)) for month in months]
    
    # Dados de status
    status_data = []
    if completed_sessions > 0:
        status_data.append(StatusData(name="Concluídas", value=completed_sessions, color="#26B0BF"))
    if canceled_sessions > 0:
        status_data.append(StatusData(name="Canceladas", value=canceled_sessions, color="#ef4444"))
    if scheduled_sessions > 0:
        status_data.append(StatusData(name="Agendadas", value=scheduled_sessions, color="#10b981"))
    
    # Dados de pacientes
    patients_data = []
    patients_with_sessions_count = len(patients) - patients_without_sessions
    if patients_with_sessions_count > 0:
        patients_data.append(StatusData(name="Com sessões", value=patients_with_sessions_count, color="#26B0BF"))
    if patients_without_sessions > 0:
        patients_data.append(StatusData(name="Sem sessões", value=patients_without_sessions, color="#ef4444"))
    
    # Cria alertas de risco com tratamento de erros
    risk_alerts = []
    for patient_risk in high_risk_patients[:5]:  # Máximo 5 alertas
        try:
            risk_alerts.append(RiskAlert(
                id=patient_risk.get("id", 0),
                patient=patient_risk.get("patient", "Paciente Desconhecido"),
                risk=patient_risk.get("risk", "Baixo"),
                reason=patient_risk.get("reason", "Sem informações"),
                date=patient_risk.get("last_appointment") or date.today().isoformat()
            ))
        except (KeyError, TypeError) as e:
            # Log do erro e continua processamento
            continue
    
    return ReportsData(
        stats=stats,
        frequency_data=frequency_data,
        status_data=status_data,
        patients_data=patients_data,
        risk_alerts=risk_alerts
    )