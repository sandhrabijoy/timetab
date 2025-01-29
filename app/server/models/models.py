from typing import Optional
from datetime import datetime,date
from pydantic import BaseModel, Field
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
Base = declarative_base()

# ORM Model for Classes
class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    updated_by = Column(String, nullable=False)
    teachername= Column(String, nullable=False)

# Creation of initial class structure
class ClassSchema(BaseModel):
    name: str
    created_at: date
    created_by: str
    updated_at: date
    updated_by: str
    teachername:str

    # Adding schema example
    class Config:
        orm_mode = True

# Update schema for PUT operation
class UpdatedClassSchema(BaseModel):
    name: Optional[str]
    created_at: Optional[date]
    created_by: Optional[str]
    updated_at: Optional[date]
    updated_by: Optional[str]
    teachername:Optional[str]

    # Adding schema example
    class Config:
        orm_mode = True
        
#define the response messaage to be obtained
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
#Define the error message to be obtained
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}