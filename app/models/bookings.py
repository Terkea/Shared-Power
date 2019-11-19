from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class Bookings(Base):
    #TODO: add foreign keys
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    tool_id = Column(String(255))
    user_id = Column(Boolean())
    condition = Column(String(255))
    duration_of_booking = Column(String(255))
