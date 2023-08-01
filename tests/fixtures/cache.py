import freezegun
from redislite.client import StrictRedis


class CacheTesting:
    def __init__(self) -> None:
        with freezegun.freeze_time("2020-01-01T00:00:00"):
            self.__redis = StrictRedis()

    def set(self, name: str, value: str, ttl: int = None) -> None:
        self.__redis.set(name, value)

        if ttl:
            self.__redis.expire(name, ttl)

    def get(self, name: str) -> str:
        return self.__redis.get(name)
