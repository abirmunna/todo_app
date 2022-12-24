from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///todo.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


