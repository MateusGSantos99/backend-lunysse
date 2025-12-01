from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, patients, appointments, requests, reports, psychologists, ml_analysis
from core.database import engine
from models import models
from config import settings

# Criar tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lunysse API",
    description="Sistema de Agendamento Psicológico com Machine Learning",
    version="2.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(requests.router)
app.include_router(reports.router)
app.include_router(psychologists.router)
app.include_router(ml_analysis.router)

@app.get("/")
async def root():
    return {"message": "Lunysse API - Sistema de Agendamento Psicológico"}