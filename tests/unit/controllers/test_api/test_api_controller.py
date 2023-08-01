import pytest

from controllers.api import ApiController
from models.consult import Consult
from models.crawler_response import CrawlerResponse
from models.parts import Parts
from models.process import Process
from models.process_moviment import ProcessMoviment
from models.response import ApiResponse
from tests.fixtures.cache import CacheTesting


DEFAULT_API_RESPONSE = ApiResponse(
    status="ok",
    message="data crawled",
    data=CrawlerResponse(
        grau_1_data=Process(
            classe="Apelação Cível",
            area="Cível",
            assunto="Indenização por Dano Moral",
            data_de_distribuicao="2018-03-23",
            juiz="Des(a). Fábio José Bittencourt Araújo",
            valor_da_acao=10000.00,
            partes_do_processo=Parts(),
            lista_das_movimentacoes=[
                ProcessMoviment(
                    data="2020-01-01T00:00:00",
                    details="Lorem ipsum dolor sit amet."
                )
            ],
        ),
        grau_2_data=Process(
            classe="Apelação Cível",
            area="Cível",
            assunto="Indenização por Dano Moral",
            data_de_distribuicao="2018-03-23T00:00:00",
            juiz="Des(a). Fábio José Bittencourt Araújo",
            valor_da_acao=10000.00,
            partes_do_processo=Parts(),
            lista_das_movimentacoes=[
                ProcessMoviment(
                    data="2020-01-01T00:00:00",
                    details="Lorem ipsum dolor sit amet."
                )
            ],
        ),
    )
)


class FakeCrawlerController:
    def set_crawler(self, process_number) -> None:
        pass

    def get_data_from_web(self) -> ApiResponse:
        return DEFAULT_API_RESPONSE


@pytest.fixture
def default_consult() -> Consult:
    return Consult(numero_processo="0710802-55.2018.8.02.0001")


@pytest.fixture
def default_cache_service() -> CacheTesting:
    return CacheTesting()


class TestHealthCheck:
    def test_when_call_health_check_metod_should_return_a_ApiResponse_instance(
        self, default_cache_service
    ) -> None:
        #  Arrange
        controller = ApiController(
            default_cache_service,
            FakeCrawlerController()
        )

        #  Act
        response = controller.health_check()

        #  Assert
        assert isinstance(response, ApiResponse)

    def test_when_call_health_check_metod_should_return_a_ok_status(
        self, default_cache_service
    ) -> None:
        #  Arrange
        controller = ApiController(
            default_cache_service,
            FakeCrawlerController()
        )

        #  Act
        response = controller.health_check()

        #  Assert
        assert response.status == "ok"

    def test_when_call_health_check_metod_should_return_a_message(
        self, default_cache_service
    ) -> None:
        #  Arrange
        controller = ApiController(
            default_cache_service,
            FakeCrawlerController()
        )

        #  Act
        response = controller.health_check()

        #  Assert
        assert response.message == "Everything is fine"


class TestGetProcessData:
    def test_when_we_have_a_process_number_in_cache_should_return_it(
        self, default_cache_service, default_consult
    ) -> None:
        #  Arrange
        data_to_save = DEFAULT_API_RESPONSE
        default_cache_service.set(
            default_consult.numero_processo, data_to_save.model_dump_json()
        )

        controller = ApiController(
            default_cache_service,
            FakeCrawlerController()
        )

        #  Act
        response = controller.get_process_data(default_consult)

        #  Assert
        assert response.status == "ok"
        assert response.message == "data from cache"
        assert response.data == data_to_save.data.model_dump()

    def test_when_we_dont_have_a_process_number_in_cache_should_return_it_from_crawler(  # noqa
        self, default_cache_service, default_consult
    ) -> None:
        #  Arrange
        controller = ApiController(
            default_cache_service,
            FakeCrawlerController()
        )

        #  Act
        response = controller.get_process_data(default_consult)

        #  Assert
        assert response.status == "ok"
        assert response.message == "data crawled"
        assert response.data == DEFAULT_API_RESPONSE.data

    def test_when_we_get_data_from_crawler_we_should_save_data_in_cache(
        self, default_cache_service, default_consult
    ) -> None:
        #  Arrange
        controller = ApiController(
            default_cache_service,
            FakeCrawlerController()
        )

        #  Act
        controller.get_process_data(default_consult)

        #  Assert
        assert default_cache_service.get(default_consult.numero_processo)

    def test_when_we_have_a_exception_should_return_a_error_message(
        self, default_cache_service, default_consult
    ) -> None:
        #  Arrange
        class FakeCrawlerControllerWithException:
            def set_crawler(self, process_number) -> None:
                pass

            def get_data_from_web(self) -> ApiResponse:
                raise Exception("error")

        controller = ApiController(
            default_cache_service,
            FakeCrawlerControllerWithException()
        )

        #  Act
        response = controller.get_process_data(default_consult)

        #  Assert
        assert response.status == "error"
        assert response.message == "error"
