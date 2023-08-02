import pytest
from unittest.mock import patch
from crawlers.base_crawler import Crawler
from controllers.crawler import CrawlersController
from models.crawler_response import CrawlerResponse
from models.parts import Parts
from models.process import Process
from models.process_moviment import ProcessMoviment
from models.process_number import ProcessNumber


DEFAULT_DATA_EXTRACTED = Process(
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
)


class FakeCrawlerTJA(Crawler):
    def get_first_grade_page_data(self) -> str:
        return "first_grade_data"

    def get_second_grade_page_data(self) -> str:
        return "second_grade_data"

    def extract_data_from_page(self, page_data) -> Process:
        return DEFAULT_DATA_EXTRACTED


class FakeCrawlerTJC(Crawler):
    def get_first_grade_page_data(self) -> str:
        return None

    def get_second_grade_page_data(self) -> str:
        return None

    def extract_data_from_page(self, page_data) -> dict:
        return None


class FakeCrawlerTJCWithFirstGrade(FakeCrawlerTJC):
    def get_first_grade_page_data(self) -> str:
        return "first_grade_data"


class FakeCrawlerTJAWithError(FakeCrawlerTJA):
    def extract_data_from_page(self, page_data) -> dict:
        raise Exception("Exception")


@pytest.fixture
def default_crawler() -> FakeCrawlerTJA:
    return FakeCrawlerTJA()


@pytest.fixture
def default_crawler_without_data() -> FakeCrawlerTJC:
    return FakeCrawlerTJC()


@pytest.fixture
def crawlers_controller() -> CrawlersController:
    return CrawlersController()


@patch(
    "controllers.crawler.AVAILABLE_CRAWLERS",
    {
        "8.02": FakeCrawlerTJA,
        "8.06": FakeCrawlerTJC,
    }
)
class TestSetCrawler:
    def test_when_we_got_a_process_number_with_802_segment_should_set_a_crawler_at_tja_crawler(  # noqa
        self, crawlers_controller
    ) -> None:
        #  Arrange
        process_number = ProcessNumber(
            "0710802-55.2018.8.02.0001"
        )

        #  Act
        crawlers_controller.set_crawler(process_number)

        #  Assert
        assert isinstance(
            crawlers_controller._CrawlersController__crawler,
            FakeCrawlerTJA
        )

    def test_when_we_got_a_process_number_with_806_segment_should_set_a_crawler_at_tjc_crawler(  # noqa
        self, crawlers_controller
    ) -> None:
        #  Arrange
        process_number = ProcessNumber(
            "0710802-55.2018.8.06.0001"
        )

        #  Act
        crawlers_controller.set_crawler(process_number)

        #  Assert
        assert isinstance(
            crawlers_controller._CrawlersController__crawler,
            FakeCrawlerTJC
        )

    def test_when_we_got_a_process_number_without_a_implemented_crawler_segment_should_raise_an_exception(  # noqa
        self, crawlers_controller
    ) -> None:
        #  Arrange
        process_number = ProcessNumber(
            "0710802-55.2018.8.03.0001"
        )

        #  Act
        with pytest.raises(Exception) as exception:
            crawlers_controller.set_crawler(process_number)

        #  Assert
            assert str(exception.value) == "Crawler not implemented"


class TestGetDataFromWeb:
    @patch(
        "controllers.crawler.AVAILABLE_CRAWLERS",
        {
            "8.02": FakeCrawlerTJA,
            "8.06": FakeCrawlerTJC,
        }
    )
    def test_when_get_data_from_web_with_data_should_return_it(
        self, crawlers_controller
    ) -> None:
        # Arrange
        response_data = CrawlerResponse(
            grau_1_data=DEFAULT_DATA_EXTRACTED,
            grau_2_data=DEFAULT_DATA_EXTRACTED,
        )
        process_number = ProcessNumber(
            "0710802-55.2018.8.02.0001"
        )

        # Act
        crawlers_controller.set_crawler(process_number)
        response = crawlers_controller.get_data_from_web()

        # Assert
        assert response.status == "ok"
        assert response.message == "data crawled"
        assert response.data == response_data

    @patch(
        "controllers.crawler.AVAILABLE_CRAWLERS",
        {
            "8.02": FakeCrawlerTJA,
            "8.06": FakeCrawlerTJC,
        }
    )
    def test_when_get_data_from_web_without_first_grade_data_should_return_error_message(  # noqa
        self, crawlers_controller
    ) -> None:
        # Arrange
        process_number = ProcessNumber(
            "0710802-55.2018.8.06.0001"
        )

        # Act
        crawlers_controller.set_crawler(process_number)
        response = crawlers_controller.get_data_from_web()

        # Assert
        assert response.status == "error"
        assert response.message == "first grade page data not found"

    @patch(
        "controllers.crawler.AVAILABLE_CRAWLERS",
        {
            "8.02": FakeCrawlerTJA,
            "8.06": FakeCrawlerTJCWithFirstGrade,
        }
    )
    def test_when_get_data_from_web_without_second_grade_data__should_return_error_message(  # noqa
        self, crawlers_controller
    ) -> None:
        # Arrange
        process_number = ProcessNumber(
            "0710802-55.2018.8.06.0001"
        )

        # Act
        crawlers_controller.set_crawler(process_number)
        response = crawlers_controller.get_data_from_web()

        # Assert
        assert response.status == "error"
        assert response.message == "second grade page data not found"

    @patch(
        "controllers.crawler.AVAILABLE_CRAWLERS",
        {
            "8.02": FakeCrawlerTJAWithError,
            "8.06": FakeCrawlerTJC,
        }
    )
    def test_when_have_a_exception_in_extract_data_from_page_should_return_error_message(  # noqa
        self, crawlers_controller
    ) -> None:
        # Arrange
        process_number = ProcessNumber(
            "0710802-55.2018.8.02.0001"
        )

        # Act
        crawlers_controller.set_crawler(process_number)
        response = crawlers_controller.get_data_from_web()

        # Assert
        assert response.status == "error"
        assert response.message == "Error in extract data: Exception"
