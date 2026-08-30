import pytest

from app.database.models import DocumentChunk


def test_wrong_embedding_dimension(db_session):

    wrong_embedding = [0.1] * 768

    chunk = DocumentChunk(
        document_id=1,
        chunk_index=0,
        text="Wrong dimension test",
        embedding=wrong_embedding,
        embedding_model="wrong-model",
    )

    db_session.add(chunk)

    with pytest.raises(Exception):
        db_session.commit()

    db_session.rollback()