from contextlib import asynccontextmanager
from typing import Optional, Annotated
from app import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends
from typing import AsyncGenerator

class TodoBase(SQLModel):
    content: str = Field(index=True)
    price: int

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={}, pool_recycle=300
)

def create_db_and_tables()->None:
    SQLModel.metadata.create_all(engine)
    
# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncGenerator[None, None]:
    print("Creating tables..")
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, title="Hello World API with DB",
              version="0.0.1",
            #   servers=[{
            #       # ADD Cloudflared URL Here Before Creating GPT Action
            #       "url": "https://luxembourg-souls-else-guild.trycloudflare.com",
            #       "description": "Development Server"
            #   }]
              )


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def read_root():
    return {"Hello": "Custom GPT Actions"}

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoBase, session: Annotated[Session, Depends(get_session)])->Todo:
        new_todo = Todo(content=todo.content, price=todo.price)
        session.add(new_todo)
        session.commit()
        session.refresh(new_todo)
        return new_todo

@app.get("/todos/", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
        todos = session.exec(select(Todo)).all()
        return todos