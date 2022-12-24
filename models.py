from sqlalchemy import Column, Integer, String
from database import Base

class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(256))