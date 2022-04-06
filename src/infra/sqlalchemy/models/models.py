from sqlalchemy import Column, Float, Integer, String
from infra.sqlalchemy.config.database import Base

# modelando nossas classes que representam dados no bd
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    details = Column(String)