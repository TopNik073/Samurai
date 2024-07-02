from dotenv import load_dotenv
import os


class JWTConfig:
    def __init__(self, JWT_SECRET_KEY: str, JWT_ALGORITHM: str):
        self.JWT_SECRET_KEY = JWT_SECRET_KEY
        self.JWT_ALGORITHM = JWT_ALGORITHM
        self.JWT_ACCESS_TOKEN_EXPIRE = 600
        self.JWT_REFRESH_TOKEN_EXPIRE = 60 * 60 * 24 * 30


load_dotenv()

config = JWTConfig(
    os.getenv("JWT_SECRET_KEY"),
    os.getenv("JWT_ALGORITHM"),
)
