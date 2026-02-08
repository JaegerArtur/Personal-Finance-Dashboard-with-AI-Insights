from sqlalchemy import Column, Integer, DateTime, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String(100))
    category = Column(String(30))
    amount = Column(Numeric(10,2), nullable=False)
    transaction_type = Column(String, nullable=False)
    account = relationship("Account", back_populates="transactions")