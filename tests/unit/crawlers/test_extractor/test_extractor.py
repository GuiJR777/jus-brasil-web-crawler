import pytest
from crawlers.extractor import Extractor
from tests.fixtures.first_grade_tja_page import FIRST_GRADE_TJA_PAGE
from tests.fixtures.first_grade_tja_data import FIRST_PAGE_TJA_DATA


@pytest.fixture
def extractor() -> Extractor:
    return Extractor()


class TestExtractor:
    def test_extract_data_from_page(self) -> None:
        # Arrange
        page_data = FIRST_GRADE_TJA_PAGE

        expected_process = FIRST_PAGE_TJA_DATA

        extractor = Extractor()

        # Act
        result = extractor.extract_data_from_page(page_data)

        # Assert
        assert result == expected_process
