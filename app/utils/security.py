from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    """Gera um hash seguro para a senha fornecida."""
    return pwd_context.hash(senha)

def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado"""
    return pwd_context.verify(senha_plana, senha_hash)