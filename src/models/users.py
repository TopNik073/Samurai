from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from src.shemas.users import UserSchema
from src.models.Base import Base

from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    repr_cols = ("name",)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str] = mapped_column(nullable=True)

    standart_auth: Mapped[bool] = mapped_column(default=False)
    google: Mapped[bool] = mapped_column(default=False)
    vk: Mapped[bool] = mapped_column(default=False)

    is_verified: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            surname=self.name,
            is_verified=self.is_verified,
            is_admin=self.is_admin,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_dict(self) -> dict:
        return vars(self)


class UserStandartAuth(Base):
    __tablename__ = "user_standart_auth"

    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    email: Mapped[str] = mapped_column(nullable=True, primary_key=True)
    hash_password: Mapped[str] = mapped_column(nullable=True)


class UserGoogleAuth(Base):
    __tablename__ = "user_google_auth"

    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    email: Mapped[str] = mapped_column(nullable=True, primary_key=True)


class UserVKAuth(Base):
    __tablename__ = "user_vk_auth"

    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    vk_id: Mapped[str] = mapped_column(nullable=True, primary_key=True)
