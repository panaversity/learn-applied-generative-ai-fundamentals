from sqlmodel import create_engine, SQLModel
from app.configuration import settings

connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
engine = create_engine(connection_string, connect_args={}, pool_recycle=300)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)