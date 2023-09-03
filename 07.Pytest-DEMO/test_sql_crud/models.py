# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, Integer, DATETIME
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String(64))
    birthday: datetime = Column(DATETIME)