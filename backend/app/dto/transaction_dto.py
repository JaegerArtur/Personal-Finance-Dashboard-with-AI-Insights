from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

@dataclass
class TransactionDTO:
    date: datetime
    description: str
    amount: Decimal
    category: str | None
    transaction_type: str