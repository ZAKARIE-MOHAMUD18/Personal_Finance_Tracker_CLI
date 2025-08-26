from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from . import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)  # e.g. 'deposit', 'withdrawal', 'expense'
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=True)  # e.g. 'food', 'rent', 'salary'
    created_at = Column(DateTime, default=func.now())

    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, type='{self.type}', amount={self.amount}, category='{self.category}')>"
