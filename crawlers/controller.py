from crawlers.base_crawler import Crawler
from crawlers.tjal_crawler import TribunalJusticaAlagoasCrawler
from models.crawler_response import CrawlerResponse
from models.process_number import ProcessNumber
from models.response import ApiResponse


AVAILABLE_CRAWLERS: dict[str, Crawler] = {
            "8.02": TribunalJusticaAlagoasCrawler,
            "8.06": "crawler ceara",
        }


class CrawlersController:
    def __init__(self) -> None:
        self.__crawler: Crawler = None

    def set_crawler(self, process_number: ProcessNumber) -> None:
        self.__crawler = AVAILABLE_CRAWLERS[
            process_number.judiciary_segment](process_number)

    def get_data_from_web(self) -> ApiResponse:
        response = ApiResponse()
        try:
            first_grade_page_data = self.__crawler.get_first_grade_page_data()

            if not first_grade_page_data:
                response.status = "error"
                response.message = "first grade page data not found"
                return response

            first_grade_process_data = self.__crawler.extract_data_from_page(first_grade_page_data)

            second_grade_page_data = self.__crawler.get_second_grade_page_data()  # noqa

            if not second_grade_page_data:
                response.status = "error"
                response.message = "second grade page data not found"
                return response

            second_grade_process_data = self.__crawler.extract_data_from_page(second_grade_page_data)

            if not first_grade_process_data or not second_grade_process_data:
                response.status = "error"
                response.message = "process data not found"
                return response

            response.message = "data crawled"
            response.data = CrawlerResponse(
                grau_1_data=first_grade_process_data,
                grau_2_data=second_grade_process_data,
            )

        except Exception as exception:
            response.status = "error"
            response.message = f"{exception}"

        return response
