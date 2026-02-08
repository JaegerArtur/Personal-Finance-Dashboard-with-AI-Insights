from fastapi import FastAPI
from .core.database import engine, Base

from .models.user import User
from .models.account import Account
from .models.transaction import Transaction

Base.metadata.create_all(bind=engine)