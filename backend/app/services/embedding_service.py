from openai import OpenAI

from app.core.config import (
    OPENROUTER_API_KEY,
    EMBEDDING_MODEL,
)


class EmbeddingService:

    def __init__(self):
        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

        self.model = EMBEDDING_MODEL

    def generate_embedding(
        self,
        text: str,
    ) -> list[float]:

        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        return response.data[0].embedding

    def generate_embeddings(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        if not texts:
            raise ValueError("Texts cannot be empty")

        for text in texts:
            if not text or not text.strip():
                raise ValueError("Text cannot be empty")

        response = self.client.embeddings.create(
            model=self.model,
            input=texts,
        )

        return [
            item.embedding
            for item in response.data
        ]