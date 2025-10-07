from pydantic import BaseModel
from typing import List, Dict, Optional

class Seller(BaseModel):
    Seller: str
    SellerPrice: str
    Delivery: str

class ProductBase(BaseModel):
    title: str
    price: str
    rating: str
    images: List[str]
    sellers: List[Seller]
    min_price: Optional[float]
    max_price: Optional[float]

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
