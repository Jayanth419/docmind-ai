from app.services.embedding_service import EmbeddingService


def test_embedding_dimension():

    service = EmbeddingService()

    embedding = service.generate_embedding(
        "DocMind AI"
    )

    assert isinstance(embedding, list)
    assert len(embedding) == 1536