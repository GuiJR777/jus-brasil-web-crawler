from typing import Any

from redis import StrictRedis


class RedisCache:
    def __init__(self, host, password, port) -> None:
        self.__redis = StrictRedis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )

    def get(self, name: str) -> Any:
        return self.__redis.get(name)

    def set(self, name: str, value: Any, ttl: int | None = None) -> None:
        self.__redis.set(name, value)

        if ttl:
            self.__redis.expire(name, ttl)
