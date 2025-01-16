from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated


from server.routes.class_routes import router as ClassRouter 
#from server.database.class_database import router as 
 
app = FastAPI()
models.Base.metadata.create_all(bind=engine)




if __name__ == "__main__":
    # Initialize the database (for first-time setup)
    Base.metadata.create_all(bind=engine)

  
# Database Dependency for FastAPI or Other Frameworks
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}