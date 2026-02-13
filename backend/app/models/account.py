from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Account(Base):
    __tablename__ = "accounts"

    # ID da conta
    id = Column(Integer, autoincrement=True, primary_key=True)
    # ID do usuário dono da conta
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # Nome da conta (referente ao banco)
    name = Column(String(100), nullable=False)
    # Tipo da conta (débito ou crédito)
    account_type = Column(String(20), nullable=False)
    # Relação com a tabela de transações (para o SQLAlchemy)
    transactions = relationship("Transaction", back_populates="account")