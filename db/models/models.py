from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime

from ..db import Base


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    is_add_choices_active = Column(Boolean, default=False, nullable=False)
    is_voting_active = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    update_at = Column(DateTime, default=datetime.now())
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)

    owner = relationship("User", back_populates="polls")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    user_name = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    polls = relationship("Poll", back_populates="owner")
