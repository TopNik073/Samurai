import uvicorn
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from src.api import api_routers
from passlib.context import CryptContext
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app.mount("/static", StaticFiles(directory="static"), name="static")


for router in api_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
