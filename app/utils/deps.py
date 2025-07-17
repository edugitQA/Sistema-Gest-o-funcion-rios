from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt import verificar_token
from typing import List

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_usuario_logado(token: str = Depends(oauth2_scheme)):
    """
    Dependência para obter o usuário logado a partir do token JWT.
    """
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

def verificar_permissao(cargos_permitidos: list[str]):
    """
    Dependência para verificar se o usuário logado esta na lista de cargos permitidos.      
    """
    def _verificar_cargo(usuario: dict = Depends(get_usuario_logado)):
        cargo_usuario = usuario.get("cargo")
        if cargo_usuario not in cargos_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Acesso negado. Você não tem permissão para esse recurso.",
            )
        return usuario
    return _verificar_cargo
