from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Invoices(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    return_id = Column(String(255))

    def __repr__(self):
        return str(self.__dict__)