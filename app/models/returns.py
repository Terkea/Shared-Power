from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Returns(Base):
    __tablename__ = 'returns'
    id = Column(Integer, primary_key=True)
    return_datetime = Column(String(255))
    booking_id = Column(Integer, ForeignKey('bookings.id'))
