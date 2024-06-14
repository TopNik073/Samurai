from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    password: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserGetSchema(BaseModel):
    id: int
    name: str
    is_verified: bool
    access_token: str | None
    refresh_token: str | None

    class Config:
        from_attributes = True
