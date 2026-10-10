from fastapi import FastAPI
from app.routers import text_route

app = FastAPI(
    title="Profanity Filter API",
    description="API para detectar y censurar groserias en multiples idiomas.",
    version="1.0.0"
)



app.include_router(text_route.router)