from app.services.vector_search_service import (
    VectorSearchService,
)


def test_vector_search_service_exists():

    service = VectorSearchService()

    assert service is not None
    assert hasattr(
        service,
        "search_similar_chunks",
    )

def test_search_similar_chunks(db_session):

    service = VectorSearchService()

    query_embedding = [0.0] * 1536

    results = service.search_similar_chunks(
            db=db_session,
            user_id=1,
            query_embedding=query_embedding,
            limit=5,
        )

        assert isinstance(results, list)