from typing import Optional
from datetime import date
from pydantic import BaseModel, Field

# Creation of initial class structure
class ClassSchema(BaseModel):
    name: str
    created_at: date
    created_by: str
    updated_at: date
    updated_by: str

    # Adding schema example
    class Config:
        schema_extra = {
            "example": {
                "name": "Computer Science",
                "created_at": "2022-12-27",
                "created_by": "admin",
                "updated_at": "2022-12-27",
                "updated_by": "admin",
            }
        }

# Update schema for PUT operation
class UpdatedClassSchema(BaseModel):
    name: Optional[str]
    created_at: Optional[date]
    created_by: Optional[str]
    updated_at: Optional[date]
    updated_by: Optional[str]

    # Adding schema example
    class Config:
        schema_extra = {
            "example": {
                "name": "Data Science",
                "created_at": "2023-01-01",
                "created_by": "editor",
                "updated_at": "2023-01-10",
                "updated_by": "editor",
            }
        }
