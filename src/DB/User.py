from src.models.users import Users
from src.DB.ORM.SQLAlchemy import SQLAlchemyORM


class User(SQLAlchemyORM):
    model = Users
