import re

from crawlers.base_crawler import Crawler
from crawlers.extractor import Extractor
from models.process import Process
from models.process_number import ProcessNumber
from services.browser import Browser
from bs4 import BeautifulSoup


FIRST_GRADE_URL = "https://esaj.tjce.jus.br/cpopg/show.do?processo.numero={process_number}"  # noqa
SEARCH_PAGE_URL = "https://esaj.tjce.jus.br/cposg5/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado={process_id_process_date}&foroNumeroUnificado={court_id}&dePesquisaNuUnificado={process_number}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO"  # noqa
SECOND_GRADE_URL = "https://esaj.tjce.jus.br/cposg5/show.do?processo.codigo={process_code}"  # noqa
PARTS = ["Autor", "Ré"]


class TribunalJusticaCearaCrawler(Crawler):
    def __init__(self, process_number: ProcessNumber) -> None:
        self.__process_number = process_number
        self.__browser = Browser()
        self.__extractor = Extractor()

    def get_first_grade_page_data(self) -> str:
        url = FIRST_GRADE_URL.format(
            process_number=self.__process_number.number
        )

        return self.__browser.get(url)

    def get_second_grade_page_data(self) -> str:
        url = SEARCH_PAGE_URL.format(
            process_id_process_date=f"{self.__process_number.process_id}-{self.__process_number.process_date}",  # noqa
            court_id=self.__process_number.court_id,
            process_number=self.__process_number.number,
        )

        search_page = self.__browser.get(url)

        bf_soup = BeautifulSoup(search_page, "html.parser")

        process_code = bf_soup.find(id="processoSelecionado")

        if process_code:
            process_code = process_code.get("value")
        else:
            pattern = re.compile(r'P00\w{10}')
            found_code = pattern.search(search_page)

            if found_code:
                process_code = found_code.group(0)

        second_grade_url = SECOND_GRADE_URL.format(
            process_code=process_code
        )

        return self.__browser.get(second_grade_url)

    def extract_data_from_page(self, page_data: str) -> Process:
        return self.__extractor.extract_data_from_page(page_data)
