from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt import verificar_token

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

