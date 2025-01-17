
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime

from app.server.models.models import Class


# Helper Function to Convert ORM Object to Dictionary
def class_helper(cls:Class) -> dict:
    return {
        "id": cls.id,
        "name": cls.name,
        "created_at": cls.created_at,
        "created_by": cls.created_by,
        "updated_at": cls.updated_at,
        "updated_by": cls.updated_by
    }

# CRUD Functions

# Retrieve All Classes
def retrieve_classes(db: Session):
    classes = db.query(Class).all()
    return classes
    # return [class_helper(cls) for cls in classes]


# Retrieve a Class by ID
def retrieve_class(db: Session, id: int):
    cls = db.query(Class).filter(Class.id == id).first()
    return class_helper(cls) if cls else None

# Add a New Class
def add_class(db: Session, class_data: dict):
    try:
        new_class = Class(**class_data)
        db.add(new_class)
        db.commit()
        db.refresh(new_class)
        return class_helper(new_class)
    except Exception as e:
        db.rollback()
        raise ValueError(f"Failed to add class: {str(e)}")

def update_class(db: Session, id: int, class_data: dict):
    try:
        class_to_update = db.query(Class).filter(Class.id == id).first()
        if not class_to_update:
            return None
        for key, value in class_data.items():
            setattr(class_to_update, key, value)
        class_to_update.updated_at = datetime.utcnow()  # Explicitly set update time
        db.commit()
        db.refresh(class_to_update)
        return class_helper(class_to_update)
    except Exception as e:
        db.rollback()
        raise ValueError(f"Failed to update class: {str(e)}")


# Delete a Class by ID
def delete_class(db: Session, id: int):
    cls = db.query(Class).filter(Class.id == id).first()
    if cls:
        db.delete(cls)
        db.commit()
        return True
    return False


