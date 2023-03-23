from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True, nullable=False)
    store = Column(String(100), nullable=False)
    product = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
    date_created = Column(DateTime, nullable=False)