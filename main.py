from fastapi import FastAPI
from parainnage import router as parrainage_router

app = FastAPI()

# Inclure les routes du parrainage
app.include_router(parrainage_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de parrainage"}
