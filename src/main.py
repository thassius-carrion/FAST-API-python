from fastapi import FastAPI, Body, Request, Depends
from pydantic import BaseModel

from sqlalchemy.orm import Session

from schemas import schemas
from infra.sqlalchemy.repositories.product import RepositoryProduct
from infra.sqlalchemy.config.database import get_db, create_db

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

create_db()

app = FastAPI()

templates = Jinja2Templates(directory="htmldirectory")

@app.get("/home")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/home/produts")
def get_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).get()
    return products

@app.post("/home/produts")
def  post_product(product: schemas.Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created