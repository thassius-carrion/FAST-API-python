from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    details: str

    class Config:
        orm_mode = True

class Request(BaseModel):
    id: Optional[int] = None
    user: User
    product: Product
    quantity: int

