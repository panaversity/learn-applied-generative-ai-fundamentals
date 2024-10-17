from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI(
    title="Location Finder API", 
    version="1.0.0", 
    servers=[
            {
                "url": "https://custom-domain.ngrok-free.app",
                "description": "Production Server"
            },
            {
                "url": "http://localhost:8000",
                "description": "Development Server"
            }
        ]
)

class Location(SQLModel, table=True):
    name: str = Field(index=True, primary_key=True)
    location: str

database_url = "postgresql://neon_postgress_db_url/hero_class?sslmode=require"


engine = create_engine(database_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/persons/")
def read_all_persons():
    """
    Retrieves all persons from the database.

    Returns:
        list: A list of Location objects representing the persons.
    """
    with Session(engine) as session:
        loc_data = session.exec(select(Location)).all()
        return loc_data


@app.post("/person/")
def create_person(person_data: Location):
    """
    Creates a new person record in the database.

    Args:
        person_data (Location): name and location of person. 

    Returns:
        Location: The created person record that is name and location of person. 
    """
    with Session(engine) as session:
        session.add(person_data)
        session.commit()
        session.refresh(person_data)
        return person_data


# dependency injection function
def get_location_or_404(name:str)->Location:
    with Session(engine) as session:
        loc_data = session.exec(select(Location).where(Location.name == name)).first()
        if not loc_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No location found for {name}")
        return loc_data


@app.get("/location/{name}")
def get_person_location(name: str, location: Annotated[Location, Depends(get_location_or_404)]):
    """
    Retrieve the location of a person by their name.

    Args:
        name (str): The name of the person.

    Returns:
        Location: The location of the person.
    """
    return location