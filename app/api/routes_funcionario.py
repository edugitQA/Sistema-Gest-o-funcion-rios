from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.schemas.funcionario import FuncionarioCreate, FuncionarioResponse
from app.services.funcionario_service import criar_funcionario

router = APIRouter()

@router.post("/funcionarios/", response_model=FuncionarioResponse)
async def criar_func(data: FuncionarioCreate, db: AsyncSession = Depends(get_session)):
    return await criar_funcionario(data, db)