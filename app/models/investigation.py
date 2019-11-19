from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Investigation(Base):
    __tablename__ = 'investigation'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    tool_id = Column(Integer, ForeignKey('tools.id'))
    user_description = Column(String(255))
    insurrance_report = Column(String(33000))
