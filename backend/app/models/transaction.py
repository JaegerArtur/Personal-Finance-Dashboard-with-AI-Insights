from sqlalchemy import Column, Integer, DateTime, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    # ID da transação
    id = Column(Integer, primary_key=True, autoincrement=True)
    # ID da conta da transação
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    # Data da transação
    date = Column(DateTime, nullable=False)
    # Descrição da transação
    description = Column(String(100))
    # Categoria da transação
    category = Column(String(30), nullable=False)
    # Valor pago/recebido da transação
    amount = Column(Numeric(10,2), nullable=False)
    # Tipo de transação (income/expense)
    transaction_type = Column(String, nullable=False)
    # Conta referente à transação (relação apenas para o SQLAlchemy)
    account = relationship("Account", back_populates="transactions")