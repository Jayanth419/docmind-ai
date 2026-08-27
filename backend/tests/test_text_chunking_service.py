from app.services.text_chunking_service import (
    TextChunkingService,
)


def test_chunk_short_text():
    service = TextChunkingService(
        chunk_size=100,
        overlap=20,
    )

    text = "Hello DocMind AI"

    chunks = service.chunk_text(
        text=text,
        page_number=1,
    )

    assert len(chunks) == 1
    assert chunks[0].text == text
    assert chunks[0].page_number == 1
    assert chunks[0].chunk_index == 0

def test_chunk_long_text():
    service = TextChunkingService(
        chunk_size=10,
        overlap=2,
    )

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = service.chunk_text(
        text=text,
        page_number=1,
    )

    assert len(chunks) > 1

def test_chunk_preserves_page_number():
    service = TextChunkingService(
        chunk_size=10,
        overlap=2,
    )

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = service.chunk_text(
        text=text,
        page_number=5,
    )

    assert chunks

    for chunk in chunks:
        assert chunk.page_number == 5

def test_chunk_indexes_are_sequential():
    service = TextChunkingService(
        chunk_size=10,
        overlap=2,
    )

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = service.chunk_text(
        text=text,
        page_number=1,
    )

    indexes = [
        chunk.chunk_index
        for chunk in chunks
    ]

    assert indexes == list(
        range(len(chunks))
    )

def test_empty_text_returns_no_chunks():
    service = TextChunkingService()

    chunks = service.chunk_text(
        text="",
        page_number=1,
    )

    assert chunks == []

def test_whitespace_text_returns_no_chunks():
    service = TextChunkingService()

    chunks = service.chunk_text(
        text="     ",
        page_number=1,
    )

    assert chunks == []


import pytest

from app.services.text_chunking_service import (
    TextChunkingService,
)


def test_chunk_size_must_be_positive():
    with pytest.raises(ValueError):
        TextChunkingService(
            chunk_size=0,
        )

def test_overlap_cannot_be_negative():
    with pytest.raises(ValueError):
        TextChunkingService(
            chunk_size=100,
            overlap=-1,
        )

def test_overlap_must_be_smaller_than_chunk_size():
    with pytest.raises(ValueError):
        TextChunkingService(
            chunk_size=100,
            overlap=100,
        )