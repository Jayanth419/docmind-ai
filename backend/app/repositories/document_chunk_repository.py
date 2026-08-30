from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


class DocumentChunkRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        document_id: int,
        chunk_index: int,
        page_number: int | None,
        text: str,
        embedding: list[float],
        embedding_model: str,
    ) -> DocumentChunk:

        chunk = DocumentChunk(
            document_id=document_id,
            chunk_index=chunk_index,
            page_number=page_number,
            text=text,
            embedding=embedding,
            embedding_model=embedding_model,
        )

        self.db.add(chunk)

        return chunk

    def search_similar(
        self,
        query_embedding: list[float],
        user_id: int,
        limit: int = 5,
    ):
        distance = DocumentChunk.embedding.cosine_distance(
            query_embedding
        )

        statement = (
            select(
                DocumentChunk,
                distance.label("distance"),
            )
            .order_by(distance)
            .limit(limit)
        )

        return self.db.execute(
            statement
        ).all()