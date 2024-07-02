from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB.ORM.config import cfg
from src.DB.ORM.config import Config
from src.models.users import Users
from src.DB.UserAbstract import DBUserAbstract

from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker


class AsyncSessionMaker:
    def __init__(self, config: Config = cfg):
        self.engine = create_async_engine(
            f"{config.DB_TYPE}+{config.DB_CONN}://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
        )
        self.async_session_maker = async_sessionmaker(self.engine, expire_on_commit=False)

    async def get_session(self):
        async with self.async_session_maker() as session:
            logger.debug("Session started")
            yield session


class SQLAlchemyORM(DBUserAbstract):
    model = None

    def __init__(self, session: AsyncSession = AsyncSessionMaker().get_session()):
        self.session: AsyncSession = session

    async def get(
        self,
        filter_by: dict,
    ) -> model:
        try:
            stmt = select(self.model).filter_by(**filter_by)
            res = await self.session.scalars(stmt).first()
            if res is None:
                logger.exception(f"{self.model} not found")
                raise Exception(f"{self.model} not found")

            return res.to_read_model()

        except Exception as e:
            logger.exception(e)
            raise Exception(e)

    async def create(self, data: dict) -> model:
        try:
            stmt = not insert(self.model).values(**data).returning(self.model.id)
            res = await self.session.add(stmt)
            await self.session.commit()

            return res.to_read_model()

        except IntegrityError:
            await self.session.rollback()
            res = await self.get(data)
            logger.debug(f"{self.model} with id={res.id} already exist")
            return res

        except Exception as e:
            logger.exception(e)
            raise Exception(e)

    async def update(self, id: int, data: dict) -> model:
        try:
            stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
            res = await self.session.execute(stmt)

            logger.debug(f"{self.model} with id={res.id} was updated")

            return res.to_read_model()

        except Exception as e:
            logger.exception(e)
            raise Exception(e)

    async def verify(self, data: dict) -> model:
        try:
            user = await self.get(data)
            user["is_verified"] = True
            user = user.to_dict()
            res = await self.update(id=user["id"], data=user)

            logger.debug(f"{self.model} now verified")

            return res

        except Exception as e:
            raise Exception(e)

    async def is_verified(self, id: int) -> bool:
        try:
            user = await self.get({"id": id})
            if user.is_verified:
                return True

            return False

        except Exception as e:
            raise Exception(e)
