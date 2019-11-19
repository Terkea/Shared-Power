from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class Dispatch(Base):
    # TODO: add foreign keys, dispatch has to be datetime
    __tablename__ = 'dispatch'
    id = Column(Integer, primary_key=True)
    booking_id = Column(String(255))
    dispatch_datetime = Column(Boolean())
