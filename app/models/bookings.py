from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import *


class Bookings(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    tool_id = Column(Integer, ForeignKey('tools.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    condition = Column(String(255))
    duration_of_booking = Column(String(255))
    # foreign keys
    returns = relationship("returns")
    invoices = relationship("invoices")
    dispatch = relationship("dispatch")
