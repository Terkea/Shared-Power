from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Returns(Base):
    __tablename__ = 'returns'
    id = Column(String(255), primary_key=True)
    returned = Column(Boolean)
    date = Column(String(255))
    tool_condition = Column(String(33000), nullable=False)
    booking_id = Column(String(255), ForeignKey('booking.id'), nullable=False)

    def __repr__(self):
        return str(self.__dict__)