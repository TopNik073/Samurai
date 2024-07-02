from loguru import logger
from src.DB.User import User
from src.models.users import Users
from src.AuthManger.JWTAuth import JWTAuth


class UserManager(User):
    def __init__(self, user: Users = None) -> None:
        super().__init__()
        self.JWTManager = JWTAuth()
        self._user: Users = user

    def get_tokens(self) -> dict:
        access_token = self.JWTManager.create_token(self._user)
        refresh_token = self.JWTManager.create_token(self._user, "refresh")
        return access_token, refresh_token

    def register_user(self, auth_type: str) -> Users:
        if auth_type == "standart":
            self._user = self.create(self._user.to_dict())

        elif auth_type == "google":
            ...

        elif auth_type == "vk":
            ...

        return self.get_tokens()

    def login_user(self, auth_type: str) -> Users:
        if auth_type == "standart":
            self.get(data)

        elif auth_type == "google":
            ...

        elif auth_type == "vk":
            ...

        return self.get_tokens()

    def logout_user(self) -> None:
        pass
