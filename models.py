from pydantic import BaseModel

class ParrainageRequest(BaseModel):
    parrain: str
    filleul: str
