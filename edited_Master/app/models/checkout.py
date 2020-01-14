from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship

from app.models.base import *


class Checkout(Base):
    __tablename__ = 'checkout'

    id = Column(Integer, primary_key=True)
    booked_date = Column(String(255))
    duration_of_booking = Column(String(255), nullable=False)
    delivery = Column(Boolean())
    tool_id = Column(Integer, ForeignKey('tools.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # foreign keys

    def __repr__(self):
        return str(self.__dict__)
