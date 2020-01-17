from sqlalchemy import Column, Integer, String, Sequence, Boolean
from sqlalchemy.orm import relationship

from app.models.base import *


class Users(Base):
    __tablename__ = 'users'
    id = Column(String(255), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    address = Column(String(255), nullable=False)
    post_code = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    phone_no = Column(String(50), nullable=False)
    is_supplier = Column(Boolean(), nullable=False)
    password = Column(String(255), nullable=False)
    # add the foreign keys
    tools = relationship("Tools", cascade="delete")
    bookings = relationship("Booking", cascade="delete")
    checkout = relationship("Checkout", cascade="delete")

    def __repr__(self):
        return str(self.__dict__)
