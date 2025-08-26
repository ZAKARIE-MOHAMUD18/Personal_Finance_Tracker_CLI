from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .account import Account
from .transaction import Transaction
from .budget import Budget
