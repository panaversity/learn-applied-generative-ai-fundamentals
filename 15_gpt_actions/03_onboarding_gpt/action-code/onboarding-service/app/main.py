# main.py
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from app import settings
from app.api.v1 import api
from app.core.config import logger_config
from app.core.db_eng import create_db_and_tables

logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting the Onboarding Service")
    create_db_and_tables()
    logger.info("Created the Database and Tables")
    yield
    logger.info("Close the Onboarding Service!")

app = FastAPI(
    lifespan=lifespan,
    servers=[
        {
            "url": settings.SERVER_URL,
            "description": "CloudFlare Server"
        },
    ]
)

app.include_router(api.api_router, prefix=settings.API_V1_STR)


@app.get("/", include_in_schema=False)
def read_root(request: Request):
    # print header received from the request
    logger.info(request.headers)
    return RedirectResponse(url="/openapi.json")
