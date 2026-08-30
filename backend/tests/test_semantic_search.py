from app.database.models import DocumentChunk
from app.services.embedding_service import EmbeddingService


def test_semantic_search(db_session):
    embedding_service = EmbeddingService()

    query = "How many vacation days do employees receive?"

    query_embedding = embedding_service.generate_embedding(query)

    assert len(query_embedding) == 1536

    results = (
        db_session.query(DocumentChunk)
        .order_by(
            DocumentChunk.embedding.cosine_distance(
                query_embedding
            )
        )
        .limit(2)
        .all()
    )

    print("\nSEARCH RESULTS:")

    for result in results:
        print(result.text)

    assert len(results) == 2

    assert results[0].text == (
        "Employees receive twenty days of annual leave."
    )

    assert results[1].text == (
        "Employees request vacation through the HR portal."
    )