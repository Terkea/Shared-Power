from sqlalchemy import Column, Integer, String, Sequence, Boolean
from sqlalchemy.orm import relationship

from app.models.base import *


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    address = Column(String(255))
    post_code = Column(String(255))
    city = Column(String(255))
    phone_no = Column(String(50))
    is_supplier = Column(Boolean())
    password = Column(String(255))
    # add the foreign keys
    tools = relationship("Tools")
    bookings = relationship("Bookings")
    investigation = relationship("Investigation")

    def __repr__(self):
        return str(self.__dict__)
