from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.models import User, UserType
from services.auth_service import get_current_user
from services.ml_services import calculate_patient_risk

router = APIRouter(prefix="/ml", tags=["machine-learning"])

@router.get("/risk-analysis")
async def get_risk_analysis(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Análise de risco ML dos pacientes baseada em frequência de consultas
    """
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem acessar análise de risco"
        )
    
    risk_analysis = calculate_patient_risk(db, current_user.id)
    
    # Estatísticas resumidas
    total_patients = len(risk_analysis)
    high_risk = len([p for p in risk_analysis if p["risk"] == "Alto"])
    moderate_risk = len([p for p in risk_analysis if p["risk"] == "Moderado"])
    low_risk = len([p for p in risk_analysis if p["risk"] == "Baixo"])
    
    return {
        "summary": {
            "total_patients": total_patients,
            "high_risk": high_risk,
            "moderate_risk": moderate_risk,
            "low_risk": low_risk,
            "risk_distribution": {
                "Alto": f"{(high_risk/total_patients*100):.1f}%" if total_patients > 0 else "0%",
                "Moderado": f"{(moderate_risk/total_patients*100):.1f}%" if total_patients > 0 else "0%",
                "Baixo": f"{(low_risk/total_patients*100):.1f}%" if total_patients > 0 else "0%"
            }
        },
        "patients": risk_analysis
    }

@router.get("/risk-analysis/{patient_id}")
async def get_patient_risk_details(
    patient_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Análise detalhada de risco de um paciente específico
    """
    if current_user.type != UserType.PSICOLOGO:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas psicólogos podem acessar análise de risco"
        )
    
    risk_analysis = calculate_patient_risk(db, current_user.id)
    patient_analysis = next((p for p in risk_analysis if p["id"] == patient_id), None)
    
    if not patient_analysis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado ou sem dados suficientes"
        )
    
    return patient_analysis