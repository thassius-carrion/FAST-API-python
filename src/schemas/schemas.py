from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    details: str

    class Config:
        orm_mode = True

class Request(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int

