from fastapi import HTTPException, status
from app.domain.models.funcionario import Funcionario
from app.domain.schemas.funcionario import FuncionarioCreate
from app.utils.security import hash_senha
from app.utils.logger import get_logger, log_event
from app.repositories.funcionario_repository import FuncionarioRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.schemas.funcionario import FuncionarioUpdate # Adicionar
from uuid import UUID

logger = get_logger()

async def criar_funcionario(data: FuncionarioCreate, db: AsyncSession) -> Funcionario:
    """
    Cria um novo funcionário no banco, validar unicidade de email e nome.
    """
    endpoint = "POST /funcionarios"
    log_event(logger, endpoint, "INICIADO", "Tentativa de cadastro", email=data.email, nome=data.nome)

    # Validação: verifica se email já existe
    if await FuncionarioRepository.get_by_email(db, data.email):
        log_event(logger, endpoint, "CONFLITO", "Email já cadastrado", email=data.email)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado."
        )

    # Validação: verifica se nome já existe
    if await FuncionarioRepository.get_by_nome(db, data.nome):
        log_event(logger, endpoint, "CONFLITO", "Nome já cadastrado", nome=data.nome)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Nome já cadastrado."
        )

    novo = Funcionario(
        nome=data.nome,
        email=data.email,
        senha=hash_senha(data.senha),
        cargo=data.cargo
    )
    try:
        novo = await FuncionarioRepository.create(db, novo)
    except Exception as e:
        log_event(logger, endpoint, "ERRO", f"Erro inesperado: {str(e)}", email=data.email, nome=data.nome)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro inesperado ao cadastrar funcionário."
        )
    log_event(
        logger,
        endpoint,
        "SUCESSO",
        "Funcionário cadastrado com sucesso",
        id=str(novo.id),
        email=novo.email,
        timestamp=str(novo.data_criacao)
    )
    return novo

async def listar_todos_funcionarios(db: AsyncSession):
    return await FuncionarioRepository.get_all(db)

async def atualizar_funcionario(funcionario_id: UUID, data: FuncionarioUpdate, db: AsyncSession):
    funcionario = await FuncionarioRepository.get_by_id(db, funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionário não encontrado.")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(funcionario, key, value)

    await db.commit()
    await db.refresh(funcionario)
    return funcionario

async def deletar_funcionario(funcionario_id: UUID, db: AsyncSession):
    funcionario = await FuncionarioRepository.get_by_id(db, funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionário não encontrado.")
    await FuncionarioRepository.delete(db, funcionario)
