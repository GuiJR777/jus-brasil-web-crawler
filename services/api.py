from configs import REDIS_PASS, REDIS_PORT, REDIS_TTL, REDIS_URL
from fastapi import FastAPI
from crawlers.controller import CrawlersController

from models.consult import Consult
from models.process_number import ProcessNumber
from models.response import ApiResponse

from services.cache import RedisCache


class ConsultApi:
    def __init__(self) -> None:
        self.__cache = RedisCache(REDIS_URL, REDIS_PASS, REDIS_PORT)
        self.__app = FastAPI()
        self.__crawlers = CrawlersController()

        self.__create_routes()

    @property
    def app(self) -> FastAPI:
        return self.__app

    def __create_routes(self) -> None:
        @self.app.get("/status")
        def health_check() -> dict[str, str]:
            return {"status": "ok"}

        @self.app.post("/consult")
        def consult(consult_data: Consult) -> ApiResponse:
            response = ApiResponse()
            cached_data = self.__cache.get(consult_data.numero_processo)

            if cached_data:
                response.message = "data from cache"
                response.data = f"{cached_data}"

                return response

            process_number = ProcessNumber(consult_data.numero_processo)

            try:
                process_data = self.__get_process_data(process_number)

                if process_data:
                    self.__cache.set(
                        name=consult_data.numero_processo,
                        value=f"{process_data}",
                        ttl=REDIS_TTL,
                    )

                    response.message = "data crawled"
                    response.data = f"{process_data}"

            except Exception as exception:
                response.status = "error"
                response.message = f"{exception}"

            return response

    def __get_process_data(self, process_number: ProcessNumber) -> dict[str, str]:
        self.__crawlers.set_crawler(process_number)
        data = self.__crawlers.get_data_from_web()

        return data
