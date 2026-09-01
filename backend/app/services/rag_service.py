from sqlalchemy.orm import Session

from app.services.embedding_service import EmbeddingService
from app.services.vector_search_service import VectorSearchService
from app.services.openrouter_service import OpenRouterService

class RAGService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_search_service = VectorSearchService()
        self.openrouter_service = OpenRouterService()
    def retrieve_context(
        self,
        db: Session,
        user_id: int,
        question: str,
        limit: int = 5,
    ):

        query_embedding = (
            self.embedding_service.generate_embedding(
                question
            )
        )

        print("QUERY EMBEDDING DIMENSION:", len(query_embedding))

        chunks = (
            self.vector_search_service.search_similar_chunks(
                db=db,
                user_id=user_id,
                query_embedding=query_embedding,
                limit=limit,
            )
        )

        print("RETRIEVED CHUNKS:", len(chunks))

        for chunk in chunks:
            print(
                "CHUNK:",
                chunk.id,
                "| DOCUMENT:",
                chunk.document_id,
                "| TEXT:",
                chunk.text,
            )

        return chunks

    def build_context(self, chunks) -> str:

        context_parts = []

        for chunk in chunks:

            context_parts.append(
                f"[Page {chunk.page_number}]\n"
                f"{chunk.text}"
            )

        return "\n\n".join(context_parts)

    def build_prompt(
        self,
        question: str,
        context: str,
    ) -> str:

        return f"""
        You are a document question-answering assistant.

        Answer the user's question using only the provided context.

        If the answer cannot be found in the context,
        say that the information is not available
        in the provided documents.

        Do not invent facts.

        Context:
        ----------------
        {context}
        ----------------

        Question:
        {question}

        Answer:
        """
    

    def answer_question(
        self,
        db: Session,
        user_id: int,
        question: str,
        limit: int = 5,
    ):

        chunks = self.retrieve_context(
            db=db,
            user_id=user_id,
            question=question,
            limit=limit,
        )

        context = self.build_context(chunks)

        prompt = self.build_prompt(
            question=question,
            context=context,
        )

        return self.openrouter_service.generate_answer(
            prompt
        )


rag_service = RAGService()