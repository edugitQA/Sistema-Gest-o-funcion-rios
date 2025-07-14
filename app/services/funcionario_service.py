from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.funcionario import Funcionario
from app.schemas.funcionario import FuncionarioCreate
from app.utils.security import hash_senha
from app.utils.logger import get_logger, log_event

logger = get_logger()

async def criar_funcionario(data: FuncionarioCreate, db: AsyncSession) -> Funcionario:
    """
    Cria um novo funcionário no banco de dados.
    Aplica validações, logging estruturado e tratamento de erros conforme boas práticas.
    """
    endpoint = "POST /funcionarios"
    # Loga tentativa de cadastro
    log_event(logger, endpoint, "INICIADO", "Tentativa de cadastro", email=data.email, nome=data.nome)

    # Validação: verifica se email já existe
    result_email = await db.execute(select(Funcionario).where(Funcionario.email == data.email))
    if result_email.scalar():
        log_event(logger, endpoint, "CONFLITO", "Email já cadastrado", email=data.email)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado."
        )

    # Validação: verifica se nome já existe
    result_nome = await db.execute(select(Funcionario).where(Funcionario.nome == data.nome))
    if result_nome.scalar():
        log_event(logger, endpoint, "CONFLITO", "Nome já cadastrado", nome=data.nome)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Nome já cadastrado."
        )

    # Hash da senha antes de salvar (segurança)
    novo = Funcionario(
        nome=data.nome,
        email=data.email,
        senha=hash_senha(data.senha),
        cargo=data.cargo    
    )
    db.add(novo)
    try:
        await db.commit()
        await db.refresh(novo)
    except Exception as e:
        # Loga erro inesperado
        log_event(logger, endpoint, "ERRO", f"Erro inesperado: {str(e)}", email=data.email, nome=data.nome)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro inesperado ao cadastrar funcionário."
        )

    # Loga sucesso
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