from sqlalchemy import Column, Integer, String, Float, JSON
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    rating = Column(String)
    images = Column(JSON)
    sellers = Column(JSON)
    min_price = Column(Float)
    max_price = Column(Float)
