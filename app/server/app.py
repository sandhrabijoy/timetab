from fastapi import FastAPI, HTTPException, Depends
from app.server.database.config import Base,engine
# from app.server.models import models

app = FastAPI()
Base.metadata.create_all(bind=engine)

from app.server.routes.class_routes import router as ClassRouter 

app.include_router(ClassRouter,tags=["Class"],prefix="/class")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}