from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

# Call functions needed to the router
from app.server.database.class import (
    add_class,
    delete_class,
    retrieve_classes,
    retrieve_class,
    update_class,
)
from app.server.models.class import (
    ErrorResponseModel,
    ResponseModel,
    ClassSchema,
    UpdateClassSchema,
)

router = APIRouter()

# Establishing the different operations to be done using CRUD

@router.post("/", response_description="Class data added into the database")
async def add_class_data(class_data: ClassSchema = Body(...)):
    class_data = jsonable_encoder(class_data)
    new_class = await add_class(class_data)
    return ResponseModel(new_class, "Class added successfully")

@router.get("/", response_description="Classes retrieved")
async def get_classes():
    classes = await retrieve_classes()
    if classes:
        return ResponseModel(classes, "Class data retrieved successfully")
    return ResponseModel(classes, "Empty list returned")

@router.get("/{id}", response_description="Class data retrieved")
async def get_class_data(id: str):
    class_data = await retrieve_class(id)
    if class_data:
        return ResponseModel(class_data, "Class data retrieved successfully")
    return ErrorResponseModel("An error occurred", 404, "Class does not exist")
