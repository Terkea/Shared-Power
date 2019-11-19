from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class Tools(Base):
    # TODO: add foreign keys
    __tablename__ = 'tools'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    owner_id = Column(String(255))
    daily_price = Column(String(255))
    half_day_price = Column(String(255))
    availability = Column(Boolean())
