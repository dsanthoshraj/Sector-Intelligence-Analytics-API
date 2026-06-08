from fastapi import APIRouter, Request
from model.sector import Sector
from config import settings

route = APIRouter(
    prefix="/insights",
    tags=["insights"]
)

def get_db(request: Request):
    return request.app.mongodb

@route.get("/")
async def get_data(request: Request):
    db = get_db(request)
    sectorCollection = db.sector
    data = await sectorCollection.find().sort("_id", -1).to_list(length=100)
    return [Sector.model_validate({**doc, "_id": str(doc["_id"])}) for doc in data]

@route.post('/', response_model=Sector)
async def save_sector(sector: Sector, request: Request):
    data = sector.model_dump(by_alias=True, exclude=["id"])
    db = get_db(request)
    sectorCollection = db["sector"]
    result = await sectorCollection.insert_one(data)
    sector.id = str(result.inserted_id)
    return sector
