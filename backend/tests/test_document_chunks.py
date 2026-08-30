from app.database.models import User, Document, DocumentChunk
from app.services.embedding_service import EmbeddingService


def test_store_three_embeddings(db_session):
    embedding_service = EmbeddingService()

    print("\nDATABASE TEST STARTED")

    # Create user
    user = User(
        email="day25@example.com",
        full_name="Day 25 User",
        hashed_password="test_password",
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    print("User ID:", user.id)

    # Create document
    document = Document(
        user_id=user.id,
        title="Employee Policy",
        description="Employee vacation policy",
        file_name="employee_policy.txt",
    )

    db_session.add(document)
    db_session.commit()
    db_session.refresh(document)

    print("Document ID:", document.id)

    chunks = [
        "Employees receive twenty days of annual leave.",
        "Employees request vacation through the HR portal.",
        "PostgreSQL is used for relational database storage.",
    ]

    for index, text in enumerate(chunks):

        print(f"\nGenerating embedding for chunk {index}...")

        embedding = embedding_service.generate_embedding(text)

        print("Embedding dimension:", len(embedding))

        assert len(embedding) == 1536

        chunk = DocumentChunk(
            document_id=document.id,
            chunk_index=index,
            page_number=None,
            text=text,
            embedding=embedding,
            embedding_model=embedding_service.model,
        )

        db_session.add(chunk)

    db_session.commit()

    print("\nCHUNKS COMMITTED")

    stored_chunks = (
        db_session.query(DocumentChunk)
        .filter(DocumentChunk.document_id == document.id)
        .all()
    )

    print("Stored chunk count:", len(stored_chunks))

    for chunk in stored_chunks:
        print(
            chunk.id,
            chunk.document_id,
            chunk.chunk_index,
            chunk.text,
            chunk.embedding_model,
        )

    assert len(stored_chunks) == 3