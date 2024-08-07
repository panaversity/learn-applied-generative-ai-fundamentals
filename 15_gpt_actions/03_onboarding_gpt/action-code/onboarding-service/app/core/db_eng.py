from sqlmodel import create_engine, SQLModel
from app import settings
from app import models


connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string,
    pool_recycle=300,    # Recycle connections after 5 minutes
    pool_size=100,       # Increase pool size to 100
    max_overflow=100,    # Allow an additional 100 connections beyond the pool size
    pool_timeout=30      # Increase timeout duration to 30 seconds
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)