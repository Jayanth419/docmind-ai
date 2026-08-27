import re
from app.schemas.text_chunk import TextChunk

class TextChunkingService:

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 200,
    ):
        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than zero"
            )

        if overlap < 0:
            raise ValueError(
                "overlap cannot be negative"
            )

        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(
        self,
        text: str,
        page_number: int,
    ) -> list[TextChunk]:

        if not text.strip():
            return []

        chunks = []

        start = 0
        chunk_index = 0

        step = self.chunk_size - self.overlap

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    TextChunk(
                        chunk_index=chunk_index,
                        page_number=page_number,
                        text=chunk_text,
                    )
                )

                chunk_index += 1

            start += step

        return chunks

    def split_sentences(
    self,
    text: str,
) -> list[str]:

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text,
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]