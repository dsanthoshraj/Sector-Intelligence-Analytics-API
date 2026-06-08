import os;
from dotenv import load_dotenv;

load_dotenv();

class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017");
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "data_visual");
    
settings = Settings();

