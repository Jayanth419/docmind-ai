from app.database.models import User, Document, DocumentChunk
from app.services.embedding_service import EmbeddingService


def test_user_isolation(db_session):

    embedding_service = EmbeddingService()

    # -------------------------
    # User 1
    # -------------------------

    user1 = User(
        email="user1_day25@example.com",
        full_name="User One",
        hashed_password="password",
    )

    # -------------------------
    # User 2
    # -------------------------

    user2 = User(
        email="user2_day25@example.com",
        full_name="User Two",
        hashed_password="password",
    )

    db_session.add_all([user1, user2])
    db_session.commit()

    # -------------------------
    # Document A → User 1
    # -------------------------

    document_a = Document(
        user_id=user1.id,
        title="Document A",
        description="User 1 document",
    )

    # -------------------------
    # Document B → User 2
    # -------------------------

    document_b = Document(
        user_id=user2.id,
        title="Document B",
        description="User 2 document",
    )

    db_session.add_all([document_a, document_b])
    db_session.commit()

    # -------------------------
    # Chunk A → User 1
    # -------------------------

    text_a = "Employees receive twenty days of annual leave."

    chunk_a = DocumentChunk(
        document_id=document_a.id,
        chunk_index=0,
        text=text_a,
        embedding=embedding_service.generate_embedding(text_a),
        embedding_model=embedding_service.model,
    )

    # -------------------------
    # Chunk B → User 2
    # -------------------------

    text_b = "PostgreSQL is used for relational database storage."

    chunk_b = DocumentChunk(
        document_id=document_b.id,
        chunk_index=0,
        text=text_b,
        embedding=embedding_service.generate_embedding(text_b),
        embedding_model=embedding_service.model,
    )

    db_session.add_all([chunk_a, chunk_b])
    db_session.commit()

    # -------------------------
    # User 1 search
    # -------------------------

    query = "database storage"

    query_embedding = embedding_service.generate_embedding(query)

    results = (
        db_session.query(DocumentChunk)
        .join(Document)
        .filter(Document.user_id == user1.id)
        .order_by(
            DocumentChunk.embedding.cosine_distance(
                query_embedding
            )
        )
        .limit(5)
        .all()
    )

    print("\nUSER 1 SEARCH RESULTS:")

    for result in results:
        print(result.text)

    # -------------------------
    # Security checks
    # -------------------------

    result_ids = [result.id for result in results]

    assert chunk_b.id not in result_ids

    assert all(
        result.document.user_id == user1.id
        for result in results
    )