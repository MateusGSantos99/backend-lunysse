from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from models.models import User, UserType
from schemas.schemas import Psychologist

router = APIRouter(prefix="/psychologists", tags=["psychologists"])

@router.get("/", response_model=List[Psychologist])
async def get_psychologists(db: Session = Depends(get_db)):
    psychologists = db.query(User).filter(User.type == UserType.PSICOLOGO).all()
    
    return [
        Psychologist(
            id=psych.id,
            name=psych.name,
            specialty=psych.specialty or "",
            crp=psych.crp or ""
        )
        for psych in psychologists
    ]