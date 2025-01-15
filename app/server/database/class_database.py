from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime

# Database URL
URL_DATABASE = 'postgresql://postgres:Sandhra11$@localhost:5432/TimeTAB'

# SQLAlchemy engine and session
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
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


# Helper Function to Convert ORM Object to Dictionary
def class_helper(cls) -> dict:
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
    return [class_helper(cls) for cls in classes]

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

# Database Dependency for FastAPI or Other Frameworks
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example Usage
if __name__ == "__main__":
    # Initialize the database (for first-time setup)
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        # Example: Add a new class
        new_class_data = {
            "name": "Math",
            "created_at": datetime(),
            "created_by": "admin",
            "updated_at": datetime(),
            "updated_by": "admin"
        }
        added_class = add_class(db, new_class_data)
        print("Added Class:", added_class)

        # Example: Retrieve all classes
        all_classes = retrieve_classes(db)
        print("All Classes:", all_classes)

        # Example: Update a class
        updated_class = update_class(db, added_class["id"], {"block": "B", "updated_by": "admin2"})
        print("Updated Class:", updated_class)

        # Example: Retrieve a specific class by ID
        retrieved_class = retrieve_class(db, added_class["id"])
        print("Retrieved Class:", retrieved_class)

        # Example: Delete a class
        is_deleted = delete_class(db, added_class["id"])
        print("Deleted Class:", is_deleted)
