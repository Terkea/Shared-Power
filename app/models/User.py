from sqlalchemy import Column, Integer, String, Sequence
from app.models.base import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
