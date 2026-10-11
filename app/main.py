from fastapi import FastAPI
from app.routers import text_route
from contextlib import asynccontextmanager
from app.services.profanity_engine import init_languages_engines

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_languages_engines()
    yield

app = FastAPI(
    title="Profanity Filter API",
    description="API para detectar y censurar groserias en multiples idiomas.",
    version="1.0.0",
    lifespan=lifespan
)



app.include_router(text_route.router)