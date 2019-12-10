from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime
from app.models.base import *


class Dispatch(Base):
    __tablename__ = 'dispatch'
    id = Column(Integer, primary_key=True)
    booking_id = Column(String(255), ForeignKey("booking.id"), nullable=False)
    dispatch_datetime = Column(String(255))

    def __repr__(self):
        return str(self.__dict__)