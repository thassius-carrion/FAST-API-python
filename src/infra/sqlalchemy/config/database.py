from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./app_py.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #url banco de dados
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #conecao local bd

Base = declarative_base() 

def create_db():
    Base.metadata.create_all(bind=engine) #classe para criar nosso db

def get_db(): #metodo para chamar nosso db, iremos utilizar na classe principal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    