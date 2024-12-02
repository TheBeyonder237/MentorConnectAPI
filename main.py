from fastapi import FastAPI
from parainnage import router as parrainage_router

# Créer une instance de l'application FastAPI
app = FastAPI(
    title="API de Parrainage - Keyce Informatique",  # Titre de l'API
    description="Cette API gère le système de parrainage entre différents niveaux d'étudiants dans l'application de parrainage de Keyce Informatique. Elle permet aux étudiants de différents niveaux (B1, B2, B3, M1, M2) de se parrainer selon des règles définies, tout en respectant une répartition équilibrée et automatique des parrainages.",
    version="1.0.0",  # Version de l'API
    docs_url="/docs",  # URL de la documentation Swagger
    redoc_url="/redoc",  # URL de la documentation ReDoc
)

# Inclure les routes de parrainage provenant du module "parainnage"
app.include_router(parrainage_router)

# Route d'accueil
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de parrainage de Keyce Informatique. Cette API gère les parrainages entre les différents niveaux d'étudiants."}

