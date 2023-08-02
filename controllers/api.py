import json

from configs import REDIS_TTL
from models.consult import Consult
from models.process_number import ProcessNumber
from models.response import ApiResponse


class ApiController:
    def __init__(self, cache_service, crawlers_controller) -> None:
        self.__cache = cache_service
        self.__crawlers = crawlers_controller

    def health_check(self) -> ApiResponse:
        return ApiResponse(
            status="ok",
            message="Everything is fine"
        )

    def get_process_data(self, consult_data: Consult) -> ApiResponse:
        response = ApiResponse()
        cached_data = self.__cache.get(consult_data.numero_processo)

        if cached_data:
            response.data = json.loads(cached_data).get("data")
            response.message = "data from cache"

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

                response = process_data
                response.message = "data crawled"

        except Exception as exception:
            response.status = "error"
            response.message = f"{exception}"

        return response

    def __get_process_data(self, process_number: ProcessNumber) -> ApiResponse:
        try:
            self.__crawlers.set_crawler(process_number)
            data = self.__crawlers.get_data_from_web()

        except Exception as exception:
            raise Exception(f"{exception}")

        return data
