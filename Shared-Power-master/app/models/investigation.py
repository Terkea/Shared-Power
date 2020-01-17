from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey
from app.models.base import *


class Investigation(Base):
    __tablename__ = 'investigation'

    id = Column(String(255), primary_key=True)
    user_description = Column(String(255), nullable=False)
    insurrance_report = Column(String(33000))
    user_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    tool_id = Column(String(255), ForeignKey('tools.id'), nullable=False)

    def __repr__(self):
        return str(self.__dict__)