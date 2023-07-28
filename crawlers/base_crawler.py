from abc import ABC, abstractmethod
from models.process import Process

from models.process_number import ProcessNumber


class Crawler(ABC):
    def __init__(self, process_number: ProcessNumber) -> None:
        pass

    @abstractmethod
    def get_first_grade_page_data(self) -> str:
        pass

    @abstractmethod
    def get_second_grade_page_data(self) -> str:
        pass

    @abstractmethod
    def extract_data_from_page(self, page_data: str) -> Process:
        pass
