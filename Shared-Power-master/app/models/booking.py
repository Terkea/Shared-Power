from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship

from app.models.base import *


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(String(255), primary_key=True)
    condition = Column(String(255))
    booked_date = Column(String(255))
    delivery = Column(Boolean())
    duration_of_booking = Column(String(255), nullable=False)
    tool_id = Column(String(255), ForeignKey('tools.id'), nullable=False)
    user_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    # foreign keys
    returns = relationship("Returns", cascade="delete")

    def __repr__(self):
        return str(self.__dict__)
