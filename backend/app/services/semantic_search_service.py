class SemanticSearchService:

    def __init__(
        self,
        embedding_service,
        chunk_repository,
    ):
        self.embedding_service = embedding_service
        self.chunk_repository = chunk_repository

    def search(
        self,
        query: str,
        user_id: int,
        limit: int = 5,
    ):

        query_embedding = (
            self.embedding_service.generate_embedding(
                query
            )
        )

        return self.chunk_repository.search_similar(
            query_embedding=query_embedding,
            user_id=user_id,
            limit=limit,
        )