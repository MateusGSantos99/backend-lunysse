# Importações necessárias
from fastapi import APIRouter, Depends  # FastAPI para criar rotas e lidar com dependências
from sqlalchemy.orm import Session  # Session do SQLAlchemy para interação com o banco de dados
from typing import List  # Para definir que a resposta será uma lista de psicólogos
from core.database import get_db  # Função que fornece a sessão do banco de dados
from models.models import User, UserType  # Importa o modelo User e enumeração UserType
from schemas.schemas import Psychologist  # Importa o schema para a resposta da rota

# Criação do roteador FastAPI para a entidade "psychologists"
router = APIRouter(prefix="/psychologists", tags=["psychologists"])

# ======================================
# Rota para listar todos os psicólogos
# ======================================
@router.get("/", response_model=List[Psychologist])
async def get_psychologists(db: Session = Depends(get_db)):  # Recebe a sessão do banco como dependência
    # Consulta todos os usuários do tipo PSICOLOGO
    psychologists = db.query(User).filter(User.type == UserType.PSICOLOGO).all()
    
    # Retorna a lista de psicólogos convertida para o schema de resposta
    # Para cada psicólogo, cria um objeto Psychologist preenchendo:
    # - id: id do usuário
    # - name: nome do usuário
    # - specialty: especialidade do psicólogo (vazio se None)
    # - crp: número do CRP (vazio se None)
    return [
        Psychologist(
            id=psych.id,
            name=psych.name,
            specialty=psych.specialty or "",  # Garante string vazia caso seja None
            crp=psych.crp or ""  # Garante string vazia caso seja None
        )
        for psych in psychologists
    ]
