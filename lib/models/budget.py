from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    limit = Column(Float, nullable=False)

    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account", back_populates="budgets")

    def __repr__(self):
        return f"<Budget(id={self.id}, category='{self.category}', limit={self.limit})>"
