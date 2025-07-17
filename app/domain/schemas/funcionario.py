from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr 
from typing import Optional

class FuncionarioCreate(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    senha: str = Field(..., min_length=6)
    cargo: str = Field(default="colaborador", max_length=50)

class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    cargo: Optional[str] = Field(None, max_length=50)
   
class FuncionarioResponse(BaseModel):
    id: UUID
    nome: str
    email: EmailStr
    cargo: str
    data_criacao: datetime

    class Config:
        orm_mode = True