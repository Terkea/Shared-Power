from click import DateTime
from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Dispatch(Base):
    __tablename__ = 'dispatch'
    id = Column(Integer, primary_key=True)
    booking_id = Column(String(255), ForeignKey("bookings.id"))
    dispatch_datetime = Column(DateTime())
