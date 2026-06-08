from fastapi import FastAPI, APIRouter
from pymongo import AsyncMongoClient
from contextlib import asynccontextmanager
from config import settings
from Routers import insights

route = APIRouter()

class Database:
    client: AsyncMongoClient = None

db_container = Database();

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_container.client = AsyncMongoClient(settings.MONGODB_URL)
    app.mongodb = db_container.client[settings.DATABASE_NAME]
    print("Connected to MongoDB")
    try:
        yield 
    finally: 
        db_container.client.close()
    print("Disconnected from MongoDB")
    
app = FastAPI(lifespan=lifespan)

app.include_router(insights.route)

