from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from app.server.models import models
from sqlalchemy import create_engine
from app.server.database.config import Base,SessionLocal,engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

#from server.routes.class_routes import router as ClassRouter 
Base=declarative_base()
 
app = FastAPI()
Base.metadata.create_all(bind=engine)
  
# Database Dependency for FastAPI or Other Frameworks
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#db_dependency=Annotated[Session,Depends(get_db)]

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}