from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app.server.database import SessionLocal
from app.server.models.class_models import ClassSchema, UpdatedClassSchema
from app.server.database.class_database import (
    add_class,
    delete_class,
    retrieve_classes,
    retrieve_class,
    update_class,
)

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_description="Class data added into the database")
def add_class_data(class_data: ClassSchema = Body(...), db: Session = Depends(get_db)):
    new_class = add_class(db, class_data.dict())
    return {"data": new_class, "message": "Class added successfully"}

@router.get("/", response_description="Classes retrieved")
def get_classes(db: Session = Depends(get_db)):
    classes = retrieve_classes(db)
    if classes:
        return {"data": classes, "message": "Class data retrieved successfully"}
    return {"data": [], "message": "Empty list returned"}

@router.get("/{id}", response_description="Class data retrieved")
def get_class_data(id: int, db: Session = Depends(get_db)):
    class_data = retrieve_class(db, id)
    if not class_data:
        raise HTTPException(status_code=404, detail="Class does not exist")
    return {"data": class_data, "message": "Class data retrieved successfully"}

@router.put("/{id}", response_description="Class data updated")
def update_class_data(
    id: int, updated_data: UpdatedClassSchema = Body(...), db: Session = Depends(get_db)
):
    updated_class = update_class(db, id, updated_data.dict(exclude_unset=True))
    if not updated_class:
        raise HTTPException(status_code=404, detail="Class does not exist")
    return {"data": updated_class, "message": "Class updated successfully"}

@router.delete("/{id}", response_description="Class data deleted")
def delete_class_data(id: int, db: Session = Depends(get_db)):
    is_deleted = delete_class(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Class does not exist")
    return {"message": "Class deleted successfully"}



