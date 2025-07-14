from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.services.auth_service import autenticar_funcionario
from app.schemas.auth import LoginData, TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(data: LoginData, db: AsyncSession = Depends(get_session)):
    """
    Endpoint para autenticar FUNCIONARIO e gerar um token JWT.
    """
    return await autenticar_funcionario(data, db)