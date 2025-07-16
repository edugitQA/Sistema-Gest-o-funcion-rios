from app.repositories.funcionario_repository import FuncionarioRepository
from app.domain.schemas.funcionario import FuncionarioCreate, FuncionarioResponse
from app.services.funcionario_service import criar_funcionario
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session

router = APIRouter()

@router.post("/funcionarios/", response_model=FuncionarioResponse)
async def criar_func(data: FuncionarioCreate, db: AsyncSession = Depends(get_session)):
    """
    Endpoint para criar funcionário, usando camada de serviço e repository.
    """
    return await criar_funcionario(data, db)