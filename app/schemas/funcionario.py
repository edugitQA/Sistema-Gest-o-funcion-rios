from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class FuncionarioCreate(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    senha: str = Field(..., min_length=6)
    cargo: str = Field(default="colaborador", max_length=50)
    
class FuncionarioResponse(BaseModel):
    id: UUID
    nome: str
    email: str
    cargo: str
    data_criacao: datetime

    class Config:
        orm_mode = True