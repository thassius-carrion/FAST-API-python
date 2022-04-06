from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from schemas import schemas
from infra.sqlalchemy.models import models

class RepositoryProduct():

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(name=product.name, price=product.price, details=product.details)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get(self):
        products = self.db.query(models.Product).all()  #esses metodos QUERY/ALL são do ORM, para nao ser necessario Query em SQL
        return products
    
    def get_by_id(self, product_id: int):
        stmt = select(models.Product).filter_by(id=product_id)
        product = self.db.execute(stmt).one()  
        return product
    
    def delete_by_id(self, product_id: int):
        stmt = delete(models.Product).where(models.Product.id == product_id)
        self.db.execute(stmt)
        self.db.commit()


