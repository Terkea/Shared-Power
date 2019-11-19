from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class Invoices(Base):
    # TODO: add foreign keys
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    booking_id = Column(String(255))
    return_id = Column(String(255))
