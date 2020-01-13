from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Invoices(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    month = Column(String(255), nullable=False)
    description = Column(String(30000), nullable=False)
    ammount = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return str(self.__dict__)