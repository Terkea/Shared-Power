from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Invoices(Base):
    __tablename__ = 'invoices'
    id = Column(String(255), primary_key=True)
    tool_name = Column(String(255), ForeignKey('tools.name'))
    customer_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    owner_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    total_cost = Column(String(255))

    def __repr__(self):
        return str(self.__dict__)