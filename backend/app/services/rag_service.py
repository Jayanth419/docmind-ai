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

        if len(query_embedding) != 1536:
            raise ValueError(
                "Query embedding dimension must be 1536"
            )

        results = (
            self.vector_search_service.search_similar_chunks(
                db=db,
                user_id=user_id,
                query_embedding=query_embedding,
                limit=limit,
            )
        )

        return results

    def build_context(self, results) -> str:

        context_parts = []

        for chunk, distance in results:

            context_parts.append(
                f"""
Source:
Document ID: {chunk.document_id}
Chunk ID: {chunk.id}
Page: {chunk.page_number}

Content:
{chunk.text}
""".strip()
            )

        return "\n\n".join(context_parts)

    def build_sources(self, results):

        sources = []

        for chunk, distance in results:

            sources.append(
                {
                    "document_id": chunk.document_id,
                    "chunk_id": chunk.id,
                    "page_number": chunk.page_number,
                }
            )

        return sources

    def build_prompt(
        self,
        question: str,
        context: str,
    ) -> str:

        return f"""
You are a document question-answering assistant.

Your task is to answer the user's question using ONLY
the information contained in the provided context.

Rules:

1. Do not use outside knowledge.
2. Do not invent facts.
3. Do not infer unsupported information.
4. If the answer is not present in the context,
   explicitly say that the information is not available
   in the provided documents.
5. Keep the answer concise and factual.
6. When possible, mention the relevant source page.

Context:
----------------
{context}
----------------

Question:
{question}

Answer:
""".strip()

    def answer_question(
        self,
        db: Session,
        user_id: int,
        question: str,
        limit: int = 5,
    ):

        results = self.retrieve_context(
            db=db,
            user_id=user_id,
            question=question,
            limit=limit,
        )

        context = self.build_context(results)

        prompt = self.build_prompt(
            question=question,
            context=context,
        )

        answer = (
            self.openrouter_service.generate_answer(
                prompt
            )
        )

        sources = self.build_sources(results)

        return {
            "answer": answer,
            "sources": sources,
        }


rag_service = RAGService()

print("RAG SERVICE FILE LOADED")
print("RAG SERVICE METHODS:", dir(rag_service))



for chunk, distance in results:

    print(
        f"""
RETRIEVED CHUNK
----------------
Chunk ID: {chunk.id}
Document ID: {chunk.document_id}
Page: {chunk.page_number}
Distance: {distance}
Text: {chunk.text}
----------------
"""
    )