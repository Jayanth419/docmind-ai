from dataclasses import dataclass


@dataclass
class TextChunk:
    chunk_index: int
    page_number: int
    text: str