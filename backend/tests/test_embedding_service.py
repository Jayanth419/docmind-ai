import pytest

from app.services.embedding_service import (
    EmbeddingService,
)


def test_empty_text():

    service = EmbeddingService()

    with pytest.raises(ValueError):
        service.generate_embedding("")


def test_whitespace_text():

    service = EmbeddingService()

    with pytest.raises(ValueError):
        service.generate_embedding("     ")


import math

from app.services.embedding_service import (
    EmbeddingService,
)


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:

    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError(
            "Cannot calculate similarity for zero vector"
        )

    return dot_product / (
        magnitude_a * magnitude_b
    )


def test_semantic_similarity():

    service = EmbeddingService()

    text1 = (
        "Employees receive twenty days "
        "of annual leave."
    )

    text2 = (
        "Workers are entitled to twenty "
        "days of vacation."
    )

    text3 = (
        "PostgreSQL stores relational data."
    )

    embedding1 = service.generate_embedding(text1)
    embedding2 = service.generate_embedding(text2)
    embedding3 = service.generate_embedding(text3)

    similarity_1_2 = cosine_similarity(
        embedding1,
        embedding2,
    )

    similarity_1_3 = cosine_similarity(
        embedding1,
        embedding3,
    )

    similarity_2_3 = cosine_similarity(
        embedding2,
        embedding3,
    )

    print("\nSemantic Similarity")

    print(
        "Annual leave vs vacation:",
        similarity_1_2,
    )

    print(
        "Annual leave vs PostgreSQL:",
        similarity_1_3,
    )

    print(
        "Vacation vs PostgreSQL:",
        similarity_2_3,
    )

    assert len(embedding1) == len(embedding2)
    assert len(embedding2) == len(embedding3)

def test_batch_embeddings():

    service = EmbeddingService()

    texts = [
        "DocMind AI",
        "Document intelligence platform",
        "PostgreSQL database",
    ]

    embeddings = service.generate_embeddings(texts)

    print("\nNumber of embeddings:", len(embeddings))
    print(
        "Vector dimension:",
        len(embeddings[0]),
    )

    assert len(embeddings) == 3

    vector_dimension = len(embeddings[0])

    assert all(
        len(embedding) == vector_dimension
        for embedding in embeddings
    )