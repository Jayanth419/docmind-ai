from pathlib import Path

import pytest

from app.services.text_extraction_service import (
    TextExtractionService,
)


# def test_extract_pdf():
#     service = TextExtractionService()

#     file_path = Path(
#         "tests/fixture/excercise2.pdf"
#     )

#     pages = service.extract_pdf(file_path)

#     assert len(pages) == 2

#     assert pages[0].page_number == 1
#     assert pages[1].page_number == 2
#     assert "a document intelligence " in pages[0].text
#     assert "python -m pytest tests" in pages[1].text

def test_extract_txt():
    service = TextExtractionService()

    file_path = Path(
        "tests/fixture/sample.txt"
    )

    text = service.extract_txt(file_path)

    assert "This is a" in text
    assert "sample" in text
    assert "text file" in text

def test_extract_txt_missing_file():
    service = TextExtractionService()

    with pytest.raises(FileNotFoundError):
        service.extract_txt(
            Path("tests/fixture/missing.txt")
        )

def test_extract_empty_txt():
    service = TextExtractionService()

    with pytest.raises(ValueError):
        service.extract_txt(
            Path("tests/fixture/empty.txt")
        )