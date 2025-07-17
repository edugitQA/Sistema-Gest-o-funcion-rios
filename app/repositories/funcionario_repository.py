from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.models.funcionario import Funcionario
from uuid import UUID

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

    @staticmethod
    async def get_by_id(db: AsyncSession, funcionario_id: UUID):
        result = await db.execute(select(Funcionario).where(Funcionario.id == funcionario_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Funcionario))
        return result.scalars().all()

    @staticmethod
    async def delete(db: AsyncSession, funcionario: Funcionario):
        await db.delete(funcionario)
        await db.commit()