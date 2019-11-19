from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class Returns(Base):
    # TODO: add foreign keys, datetime
    __tablename__ = 'returns'
    id = Column(Integer, primary_key=True)
    booking_id = Column(String(255))
    return_datetime = Column(String(255))
