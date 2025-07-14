from fastapi import APIRouter, Depends
from app.utils.deps import get_usuario_logado

router = APIRouter()

@router.get("/protegida")
async def rota_secreta(usuario = Depends(get_usuario_logado)):
    return {"mensagem": f"Acesso permitido para {usuario['cargo']}"}
