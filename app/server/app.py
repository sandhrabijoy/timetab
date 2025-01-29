from fastapi import FastAPI, HTTPException, Depends
from app.server.database.config import Base,engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Base.metadata.create_all(bind=engine)

origins=[
"http://localhost:3000",
"http://localhost:8000",
]
app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:5173"],
allow_credentials=True,
allow_methods=["*"],  
allow_headers=["*"],  
)

from app.server.routes.class_routes import router as ClassRouter 

app.include_router(ClassRouter,tags=["Class"],prefix="/class")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}