from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import *


class Tools(Base):
    __tablename__ = 'tools'

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(33000), nullable=False)
    daily_price = Column(String(255), nullable=False)
    half_day_price = Column(String(255), nullable=False)
    delivery_cost = Column(String(255), nullable=False)
    availability = Column(Boolean(), nullable=False)
    owner_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    #     add foreign keys
    bookings = relationship("Booking", cascade="delete")
    checkout = relationship("Checkout", cascade="delete")

    def __repr__(self):
        return str(self.__dict__)