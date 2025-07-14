from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.utils.security import verificar_senha
from app.utils.jwt import criar_token
from app.schemas.auth import LoginData

async def autenticar_funcionario(data: LoginData, db: AsyncSession):
    from app.models.funcionario import Funcionario
    result = await db.execute(select(Funcionario).where(Funcionario.email == data.email))
    funcionario = result.scalar_one_or_none()
    
    if not funcionario or not verificar_senha(data.senha, funcionario.senha):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou senha inválidos.")
    
    token = criar_token({"sub": str(funcionario.id), "cargo": funcionario.cargo})
    return {"access_token": token, "token_type": "bearer"}
