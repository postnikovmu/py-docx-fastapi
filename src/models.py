from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Test2(Base):
    __tablename__ = 'test2'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
