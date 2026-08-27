from pathlib import Path
from app.services.text_chunking_service import (
    TextChunkingService,
)

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
        text_chunking_service: TextChunkingService,
    ):
        self.text_extraction_service = (
            text_extraction_service
        )
        self.text_cleaning_service = text_cleaning_service
        self.text_chunking_service = text_chunking_service
    def process_pdf(
        self,
        file_path: Path,
    ):
        pages = self.text_extraction_service.extract_pdf(
            file_path
        )
        chunks = []

        for page in pages:

            cleaned_text = (
                self.text_cleaning_service
                .clean(page.text)
            )

            page_chunks = (
                self.text_chunking_service
                .chunk_text(
                    text=cleaned_text,
                    page_number=page.page_number,
                )
            )

            chunks.extend(page_chunks)

        return chunks