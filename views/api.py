from fastapi import FastAPI
from controllers.api import ApiController

from models.consult import Consult
from models.response import ApiResponse


class ConsultApi:
    def __init__(self) -> None:
        self.__controller = ApiController()
        self.__app = FastAPI()

        self.__create_routes()

    @property
    def app(self) -> FastAPI:
        return self.__app

    def __create_routes(self) -> None:
        @self.app.get("/status")
        def health_check() -> dict[str, str]:
            return self.__controller.health_check()

        @self.app.post("/consult")
        def consult(consult_data: Consult) -> ApiResponse:
            return self.__controller.get_process_data(consult_data)
