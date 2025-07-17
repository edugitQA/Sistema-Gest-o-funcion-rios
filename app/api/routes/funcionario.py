from app.repositories.funcionario_repository import FuncionarioRepository
from app.domain.schemas.funcionario import FuncionarioCreate, FuncionarioResponse, FuncionarioUpdate 
from app.services.funcionario_service import criar_funcionario, listar_todos_funcionarios, atualizar_funcionario, deletar_funcionario # Adicionar novas funções de serviço
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.utils.deps import verificar_permissao 
from typing import List
from uuid import UUID

router = APIRouter()

#Permisão: Administrador e RH podem cadastrar funcionários
@router.post("/funcionarios/", response_model=FuncionarioResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(verificar_permissao(["admin", "rh"]))])
async def criar_func(data: FuncionarioCreate, db: AsyncSession = Depends(get_session)):
    return await criar_funcionario(data, db)


# Permissão: admin, rh e colaborador podem listar
@router.get("/funcionarios/", response_model=List[FuncionarioResponse],
            dependencies=[Depends(verificar_permissao(["admin", "rh", "colaborador"]))])
async def listar_funcionarios(db: AsyncSession = Depends(get_session)):
    return await listar_todos_funcionarios(db)


# Permissão: admin e rh podem atualizar
@router.put("/funcionarios/{funcionario_id}", response_model=FuncionarioResponse,
            dependencies=[Depends(verificar_permissao(["admin", "rh"]))])
async def atualizar_func(funcionario_id: UUID, data: FuncionarioUpdate, db: AsyncSession = Depends(get_session)):
    """
    Endpoint para atualizar um funcionário. Acesso restrito para 'admin' e 'rh'.
    """
    return await atualizar_funcionario(funcionario_id, data, db)


# Permissão: apenas admin pode deletar
@router.delete("/funcionarios/{funcionario_id}", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(verificar_permissao(["admin"]))])
async def deletar_func(funcionario_id: UUID, db: AsyncSession = Depends(get_session)):
    """
    Endpoint para deletar um funcionário. Acesso restrito para 'admin'.
    """
    await deletar_funcionario(funcionario_id, db)
    return None
