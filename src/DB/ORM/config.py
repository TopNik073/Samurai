from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    def __init__(
        self,
        DB_USER: str,
        DB_PASS: str,
        DB_HOST: str,
        DB_PORT: str,
        DB_NAME: str,
        DB_CONN: str,
        DB_TYPE: str,
    ):
        self.DB_USER: str = DB_USER
        self.DB_PASS: str = DB_PASS
        self.DB_HOST: str = DB_HOST
        self.DB_PORT: str = DB_PORT
        self.DB_NAME: str = DB_NAME
        self.DB_CONN: str = DB_CONN
        self.DB_TYPE: str = DB_TYPE


cfg = Config(
    DB_USER=os.environ.get("DB_USER"),
    DB_PASS=os.environ.get("DB_PASS"),
    DB_HOST=os.environ.get("DB_HOST"),
    DB_PORT=os.environ.get("DB_PORT"),
    DB_NAME=os.environ.get("DB_NAME"),
    DB_CONN=os.environ.get("DB_CONN"),
    DB_TYPE=os.environ.get("DB_TYPE"),
)
