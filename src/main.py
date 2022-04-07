from fastapi import FastAPI, Body, Request, Depends, File, UploadFile, Form

from sqlalchemy.orm import Session

from schemas import schemas
from infra.sqlalchemy.repositories.product import RepositoryProduct
from infra.sqlalchemy.config.database import get_db, create_db

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

create_db()

app = FastAPI()

# permitir que minha API seja consumida, sem problema de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="htmldirectory")

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return {"Msg": "Pagina inicial"}

@app.get("/home/products")
def get_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).get()
    return products

@app.get("/home/products/{product_id}",  response_class=HTMLResponse)
def get_products_by_id( product_id: int, request: Request, db: Session = Depends(get_db)):
    product = RepositoryProduct(db).get_by_id(product_id)
    #return templates.TemplateResponse("home.html", {"request": request, "product_id": product_id})
    return product

@app.post("/home/products")
def  post_product(product: schemas.Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created

@app.delete("/home/products/{id}")
def delete_products_by_id(product_id: int , db: Session = Depends(get_db)):
    RepositoryProduct(db).delete_by_id(product_id)
    return {"Msg": "Removido com sucesso"}