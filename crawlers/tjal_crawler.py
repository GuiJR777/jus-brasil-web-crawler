import re

from crawlers.base_crawler import Crawler
from models.parts import Parts
from models.process import Process
from models.process_moviment import ProcessMoviment
from models.process_number import ProcessNumber
from services.browser import Browser
from bs4 import BeautifulSoup


FIRST_GRADE_URL = "https://www2.tjal.jus.br/cpopg/show.do?processo.numero={process_number}"  # noqa
SEARCH_PAGE_URL = "https://www2.tjal.jus.br/cposg5/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado={process_id_process_date}&foroNumeroUnificado={court_id}&dePesquisaNuUnificado={process_number}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO"  # noqa
SECOND_GRADE_URL = "https://www2.tjal.jus.br/cposg5/show.do?processo.codigo={process_code}"  # noqa
PARTS = ["Autor", "Ré"]


class TribunalJusticaAlagoasCrawler(Crawler):
    def __init__(self, process_number: ProcessNumber) -> None:
        self.__process_number = process_number
        self.__browser = Browser()

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

        process_code = bf_soup.find(id="processoSelecionado").get("value")

    def extract_data_from_page(self, page_data: str) -> Process:
        bf_soup = BeautifulSoup(page_data, "html.parser")

        return Process(
            classe=self.__get_classe(bf_soup),
            area=self.__get_area(bf_soup),
            assunto=self.__get_assunto(bf_soup),
            data_de_distribuicao=self.__get_data_de_distribuicao(bf_soup),
            juiz=self.__get_juiz(bf_soup),
            valor_da_acao=self.__get_valor_da_acao(bf_soup),
            partes_do_processo=self.__get_partes_do_processo(bf_soup),
            lista_das_movimentacoes=self.__get_lista_das_movimentacoes(bf_soup),  # noqa
        )

    def __get_classe(self, bf_soup: BeautifulSoup) -> str:
        return bf_soup.find(id="classeProcesso").text

    def __get_area(self, bf_soup: BeautifulSoup) -> str:
        return bf_soup.find(id="areaProcesso").text.strip()

    def __get_assunto(self, bf_soup: BeautifulSoup) -> str:
        return bf_soup.find(id="assuntoProcesso").text

    def __get_data_de_distribuicao(self, bf_soup: BeautifulSoup) -> str:
        text_from_element = bf_soup.find(
            id="dataHoraDistribuicaoProcesso").text
        text_parts = text_from_element.split(" ")

        return text_parts[0]

    def __get_juiz(self, bf_soup: BeautifulSoup) -> str:
        return bf_soup.find(id="juizProcesso").text

    def __get_valor_da_acao(self, bf_soup: BeautifulSoup) -> float:
        text_from_element = bf_soup.find(id="valorAcaoProcesso").text
        text_without_points = text_from_element.replace(".", "")
        text_without_comma = text_without_points.replace(",", ".")
        text_with_only_digits_and_point = re.sub(
            r'[^0-9.]', '', text_without_comma)

        return float(text_with_only_digits_and_point)

    def __get_partes_do_processo(self, bf_soup: BeautifulSoup) -> Parts:
        parts = Parts()

        parts_element = bf_soup.find(
            id="tablePartesPrincipais").find_all('td')

        autor = None
        advogados_autor = []
        reu = None
        advogados_reu = []
        tipo_participacao = None

        for td in parts_element:
            part_text = td.get_text(strip=True)

            if part_text in PARTS:
                tipo_participacao = part_text
                continue

            names = part_text.split("Advogado:")

            if tipo_participacao == "Autor":
                autor = names[0].strip()
                advogados_autor.extend(names[1:])

            elif tipo_participacao == "Ré":
                reu = names[0].strip()
                advogados_reu.extend(names[1:])

        parts.autor = autor
        parts.advogados_autor = advogados_autor
        parts.reu = reu
        parts.advogados_reu = advogados_reu

        return parts

    def __get_lista_das_movimentacoes(self, bf_soup: BeautifulSoup) -> list[ProcessMoviment]:  # noqa
        tr_elements = bf_soup.find_all('tr', class_='containerMovimentacao')

        process_moviments = []

        for tr in tr_elements:
            data = tr.find(
                'td', class_='dataMovimentacao').get_text(strip=True)
            details = tr.find(
                'td', class_='descricaoMovimentacao').get_text(strip=True)

            moviment = ProcessMoviment(data=data, details=details)
            process_moviments.append(moviment)

        return process_moviments