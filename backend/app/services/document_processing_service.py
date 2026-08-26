from pathlib import Path

from app.services.text_cleaning_service import (
    TextCleaningService,
)
from app.services.text_extraction_service import (
    TextExtractionService,
)


class DocumentProcessingService:

    def __init__(
        self,
        text_extraction_service: TextExtractionService,
        text_cleaning_service: TextCleaningService,
    ):
        self.text_extraction_service = (
            text_extraction_service
        )
        self.text_cleaning_service = text_cleaning_service

    def process_pdf(
        self,
        file_path: Path,
    ):
        pages = self.text_extraction_service.extract_pdf(
            file_path
        )
        cleaned_pages = []
        for page in pages:
            cleanesd_text = (self.text_cleaning_service.clean
                (page.text)
            )
            if cleanesd_text:  # Only add non-empty cleaned texts
                cleaned_pages.append({
                    "page_number": page.page_number,
                    "text": cleanesd_text,
                })
        return cleaned_pages