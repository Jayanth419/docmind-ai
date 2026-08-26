from pathlib import Path

from app.services.text_extraction_service import (
    TextExtractionService,
)


class DocumentProcessingService:

    def __init__(
        self,
        text_extraction_service: TextExtractionService,
    ):
        self.text_extraction_service = (
            text_extraction_service
        )

    def process_pdf(
        self,
        file_path: Path,
    ):
        return self.text_extraction_service.extract_pdf(
            file_path
        )