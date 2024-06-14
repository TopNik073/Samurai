import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import api_routers
from loguru import logger

logger.add(
    "logs/logs.log",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} | {message}\n{exception}",
    level="INFO",
    rotation="1 week",
    compression="zip",
    backtrace=True,
    diagnose=True,
)

app = FastAPI(title="Samurai")

app.mount("/static", StaticFiles(directory="src/static"), name="static")


for router in api_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
