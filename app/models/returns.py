from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Returns(Base):
    __tablename__ = 'returns'
    id = Column(Integer, primary_key=True)
    returned = Column(Boolean)
    booking_id = Column(Integer, ForeignKey('booking.id'), nullable=False)

    def __repr__(self):
        return str(self.__dict__)