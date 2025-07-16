from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db.base import Base

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    cargo = Column(String, default="colaborador")
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
