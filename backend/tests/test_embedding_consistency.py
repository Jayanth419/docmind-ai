from app.database.models import DocumentChunk
from app.services.embedding_service import EmbeddingService


def test_embedding_model_consistency(db_session):

    embedding_service = EmbeddingService()

    stored_chunks = (
        db_session.query(DocumentChunk)
        .all()
    )

    assert len(stored_chunks) > 0

    stored_models = {
        chunk.embedding_model
        for chunk in stored_chunks
    }

    print("\nSTORED EMBEDDING MODELS:")

    for model in stored_models:
        print(model)

    # All stored embeddings should use one model
    assert len(stored_models) == 1

    stored_model = stored_models.pop()

    print("Configured model:", embedding_service.model)
    print("Stored model:", stored_model)

    assert stored_model == embedding_service.model