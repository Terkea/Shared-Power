from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import *


class Tools(Base):
    __tablename__ = 'tools'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(33000))
    daily_price = Column(String(255))
    half_day_price = Column(String(255))
    availability = Column(Boolean())
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    #     add foreign keys
    bookings = relationship("Bookings")
    investigation = relationship("Investigation")

    def __repr__(self):
        return str(self.__dict__)