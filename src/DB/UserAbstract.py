from abc import ABC, abstractmethod


class DBUserAbstract(ABC):
    @abstractmethod
    async def get(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def create(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def verify(self, data: dict):
        raise NotImplementedError
