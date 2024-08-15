from contextlib import asynccontextmanager
from typing import Optional, Annotated
from app.configuration import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from app.database import database
from app.models import models
from fastapi.middleware.cors import CORSMiddleware

Todo = models.Todo
TodoCreate = models.TodoCreate
TodoUpdate = models.TodoUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    database.create_db_and_tables()
    yield

def get_session():
    with Session(database.engine) as session:
        yield session

app = FastAPI(lifespan=lifespan, title="Hello World API with DB", 
    version="0.0.1",
    servers=[
        {
            "url": "https://web.wania.xyz", # ADD LIVE URL Here Before Creating GPT Action
            "description": "Production Server"
        }
        ])

# Set up CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://backend:8001",
    "http://frontend:3000",
    "https://web.wania.xyz"
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Message": "Todo GPT"}


@app.get("/todos/", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
        todos = session.exec(select(Todo)).all()
        return todos
    
@app.post("/todos/", response_model=Todo)
def create_todo(todo_create: TodoCreate, session: Annotated[Session, Depends(get_session)]):
        todo = Todo.model_validate(todo_create)  # Convert TodoCreate to Todo
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate, session: Annotated[Session, Depends(get_session)]):
        # Fetch existing todo from DB
        existing_todo = session.get(Todo, todo_id)

        # If the todo does not exist - raise an HTTPException 
        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        # Update the content
        existing_todo.content = updated_todo.content
        session.commit()
        session.refresh(existing_todo)
        return existing_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
        #Fetch existing todo from DB
        existing_todo = session.get(Todo, todo_id)

        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        # Delete the todo from DB
        session.delete(existing_todo)
        session.commit()
        return {"message": "Todo successfully deleted"}