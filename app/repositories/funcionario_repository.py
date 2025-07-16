from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.funcionario import Funcionario

class FuncionarioRepository:
    """Repository para acesso a dados de Funcionário."""
    @staticmethod
    async def get_by_email(db: AsyncSession, email: str):
        result = await db.execute(select(Funcionario).where(Funcionario.email == email))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_nome(db: AsyncSession, nome: str):
        result = await db.execute(select(Funcionario).where(Funcionario.nome == nome))
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, funcionario: Funcionario):
        db.add(funcionario)
        await db.commit()
        await db.refresh(funcionario)
        return funcionario
