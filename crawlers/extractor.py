import re
from bs4 import BeautifulSoup
from models.parts import Parts
from models.process import Process
from models.process_moviment import ProcessMoviment


PARTS = [
    "Apelada",
    "Apelado",
    "Apelante",
    "Autor",
    "Custos legis",
    "Ré",
    "Réu",
    "Terceiro",
    "Testemunha",
    "Vítima",
]


class Extractor:
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
        element = bf_soup.find(id="classeProcesso")

        if not element:
            return ""
        return element.text

    def __get_area(self, bf_soup: BeautifulSoup) -> str:
        element = bf_soup.find(id="areaProcesso")

        if not element:
            return ""
        return element.text.strip()

    def __get_assunto(self, bf_soup: BeautifulSoup) -> str:
        element = bf_soup.find(id="assuntoProcesso")

        if not element:
            return ""
        return element.text

    def __get_data_de_distribuicao(self, bf_soup: BeautifulSoup) -> str:
        element = bf_soup.find(
            id="dataHoraDistribuicaoProcesso")

        if element:
            text_from_element = element.text
            text_parts = text_from_element.split(" ")

            return text_parts[0]
        return ""

    def __get_juiz(self, bf_soup: BeautifulSoup) -> str:
        element = bf_soup.find(id="juizProcesso")

        if element:
            return bf_soup.find(id="juizProcesso").text
        return ""

    def __get_valor_da_acao(self, bf_soup: BeautifulSoup) -> float:
        element = bf_soup.find(id="valorAcaoProcesso")

        if not element:
            return 0.0

        text_from_element = element.text
        text_without_points = text_from_element.replace(".", "")
        text_without_comma = text_without_points.replace(",", ".")
        text_with_only_digits_and_point = re.sub(
            r'[^0-9.]', '', text_without_comma)

        return float(text_with_only_digits_and_point)

    def __get_partes_do_processo(self, bf_soup: BeautifulSoup) -> Parts:
        parts = Parts()

        element = bf_soup.find(id="tablePartesPrincipais")

        if not element:
            return parts

        parts_element = element.find_all("td")

        tipo_participacao = None

        for td in parts_element:
            part_text = td.get_text(strip=True)

            if part_text.replace(":", "") in PARTS:
                tipo_participacao = part_text.replace(":", "")
                continue

            part_text = part_text.replace("Advogada:", "Advogado:")
            names = part_text.split("Advogado:")

            match tipo_participacao:
                case "Apelada":
                    parts.apelada = names[0].strip()
                    parts.advogados_apelada.extend(names[1:])
                case "Apelado":
                    parts.apelado = names[0].strip()
                    parts.advogados_apelado.extend(names[1:])
                case "Apelante":
                    parts.apelante.append(names[0])
                    parts.advogados_apelante.extend(names[1:])
                case "Autor":
                    parts.autor = names[0].strip()
                    parts.advogados_autor.extend(names[1:])
                case "Custos legis":
                    parts.custos_legis = part_text
                case "Ré" | "Réu":
                    parts.reu = names[0].strip()
                    parts.advogados_reu.extend(names[1:])
                case "Terceiro":
                    parts.terceiros.append(part_text)
                case "Testemunha":
                    parts.testemunhas.append(part_text)
                case "Vítima":
                    parts.vitima = part_text

        return parts

    def __get_lista_das_movimentacoes(self, bf_soup: BeautifulSoup) -> list[ProcessMoviment]:  # noqa
        tr_elements = bf_soup.find_all("tr", class_="containerMovimentacao")

        process_moviments = []

        for tr in tr_elements:
            data = tr.find(
                "td", class_="dataMovimentacao").get_text(strip=True)
            details = tr.find(
                "td", class_="descricaoMovimentacao").get_text(strip=True)

            moviment = ProcessMoviment(data=data, details=details)
            process_moviments.append(moviment)

        if not process_moviments:
            tr_elements = bf_soup.find_all("tr", class_="movimentacaoProcesso")

            for tr in tr_elements:
                data = tr.find(
                    "td", class_="dataMovimentacaoProcesso").get_text(
                        strip=True)
                details = tr.find(
                    "td", class_="descricaoMovimentacaoProcesso").get_text(
                        strip=True)

                moviment = ProcessMoviment(data=data, details=details)
                process_moviments.append(moviment)

        return process_moviments
