from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.funcionario import Funcionario
from app.schemas.funcionario import FuncionarioCreate
from app.utils.security import hash_senha

async def criar_funcionario(data: FuncionarioCreate, db: AsyncSession) -> Funcionario:
    """Cria um novo funcionário no bd."""
    novo = Funcionario(
        nome=data.nome,
        email=data.email,
        senha=hash_senha(data.senha),
        cargo=data.cargo    
    )
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return novo