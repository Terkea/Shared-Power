from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.models.base import *


class Investigation(Base):
    # TODO: add foreign keys
    __tablename__ = 'investigation'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    tool_id = Column(String(255))
    user_description = Column(String(255))
    insurrance_report = Column(String(255))
