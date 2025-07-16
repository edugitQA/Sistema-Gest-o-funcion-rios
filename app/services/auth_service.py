from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.funcionario_repository import FuncionarioRepository
from app.utils.security import verificar_senha
from app.utils.jwt import criar_token
from app.domain.schemas.auth import LoginData
from fastapi import HTTPException, status

async def autenticar_funcionario(data: LoginData, db: AsyncSession):
    """
    Autentica funcionário usando email e senha, retorna token JWT se sucesso.
    """
    funcionario = await FuncionarioRepository.get_by_email(db, data.email)
    if not funcionario or not verificar_senha(data.senha, funcionario.senha):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou senha inválidos.")
    token = criar_token({"sub": str(funcionario.id), "cargo": funcionario.cargo})
    return {"access_token": token, "token_type": "bearer"}
