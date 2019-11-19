from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    address = Column(String(255))
    post_code = Column(String(255))
    city = Column(String(255))
    phone_no = Column(String(50))
    is_supplier = Column(Boolean())
    password = Column(String(255))
