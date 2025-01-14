from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
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
    LotSchema,
    UpdateLotSchema,
)
router = APIRouter()