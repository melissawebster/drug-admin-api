from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean
from .connection import SessionLocal
from typing import Self


Base = declarative_base()

class Drug(Base):
    __tablename__ = 'drug'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Boolean, nullable=False)