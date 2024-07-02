import jwt
from src.AuthManger.config import config
from src.DB.User import User
from datetime import datetime


class JWTAuth(config):
    def create_token(self, user: Users, token_type: str = "access") -> str:
        if token_type == "access":
            expiration = datetime.datetime.utcnow() + self.JWT_ACCESS_TOKEN_EXPIRE
        else:
            expiration = datetime.datetime.utcnow() + self.JWT_REFRESH_TOKEN_EXPIRE

        data = {
            "name": user.name,
            "surname": user.surname,
            "token_type": token_type,
            "exp": expiration,
        }
        return jwt.encode(data, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)

    def is_token_valid(self, token: str) -> bool:
        pass
