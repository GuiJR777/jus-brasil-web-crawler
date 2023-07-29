import json

from configs import REDIS_PASS, REDIS_PORT, REDIS_TTL, REDIS_URL
from controllers.crawler import CrawlersController

from models.consult import Consult
from models.process_number import ProcessNumber
from models.response import ApiResponse

from services.cache import RedisCache


class ApiController:
    def __init__(self) -> None:
        self.__cache = RedisCache(REDIS_URL, REDIS_PASS, REDIS_PORT)
        self.__crawlers = CrawlersController()

    def health_check() -> ApiResponse:
        return ApiResponse(
            status="ok",
            message="Everything is fine"
        )

    def get_process_data(self, consult_data: Consult) -> ApiResponse:
        response = ApiResponse()
        cached_data = self.__cache.get(consult_data.numero_processo)

        if cached_data:
            response.message = "data from cache"
            response.data = json.loads(cached_data)

            return response

        process_number = ProcessNumber(consult_data.numero_processo)

        try:
            process_data = self.__get_process_data(process_number)

            if process_data:
                self.__cache.set(
                    name=consult_data.numero_processo,
                    value=process_data.model_dump_json(),
                    ttl=REDIS_TTL,
                )

                response.message = "data crawled"
                response.data = f"{process_data}"

        except Exception as exception:
            response.status = "error"
            response.message = f"{exception}"

        return response

    def __get_process_data(self, process_number: ProcessNumber) -> ApiResponse:
        self.__crawlers.set_crawler(process_number)
        data = self.__crawlers.get_data_from_web()

        return data
