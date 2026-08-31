from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import Document, DocumentChunk


class VectorSearchService:

    def search_similar_chunks(
        self,
        db: Session,
        user_id: int,
        query_embedding: list[float],
        limit: int = 5,
    ) -> list[DocumentChunk]:

        statement = (
            select(DocumentChunk)
            .join(
                Document,
                Document.id == DocumentChunk.document_id,
            )
            .where(
                Document.user_id == user_id,
                DocumentChunk.embedding.is_not(None),
            )
            .order_by(
                DocumentChunk.embedding.cosine_distance(
                    query_embedding
                )
            )
            .limit(limit)
        )

        return list(
            db.scalars(statement).all()
        )

vector_search_service = VectorSearchService()