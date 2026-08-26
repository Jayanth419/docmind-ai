from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


@dataclass
class ExtractedPage:
    page_number: int
    text: str


class TextExtractionService:

    def extract_pdf(
        self,
        file_path: Path,
    ) -> list[ExtractedPage]:

        if not file_path.exists():
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        if file_path.suffix.lower() != ".pdf":
            raise ValueError(
                "Only PDF files are supported"
            )

        reader = PdfReader(file_path)

        pages: list[ExtractedPage] = []

        for index, page in enumerate(
            reader.pages,
            start=1,
        ):
            text = page.extract_text() or ""
            text = text.strip()

            if text:
                pages.append(
                    ExtractedPage(
                        page_number=index,
                        text=text,
                    )
                )

        if not pages:
            raise ValueError(
                "No text could be extracted from the PDF"
            )

        return pages


    def extract_txt(
        self,
        file_path: Path,
    ) -> str:

        if not file_path.exists():
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        if file_path.suffix.lower() != ".txt":
            raise ValueError(
                "Only TXT files are supported"
            )

        text = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if not text:
            raise ValueError(
                "No text could be extracted from the TXT file"
            )

        return text