# Vector Search Debugging

## Embedding

- [ ] API/model is available
- [ ] API key is valid
- [ ] Input text is not empty
- [ ] Embedding is a list
- [ ] Embedding dimension is 1536

## PostgreSQL

- [ ] pgvector is installed
- [ ] vector extension is enabled
- [ ] document_chunks table exists
- [ ] embedding column is vector(1536)

## Storage

- [ ] chunks are created
- [ ] embeddings are generated
- [ ] transaction commits
- [ ] no duplicate ingestion

## Retrieval

- [ ] query embedding generated
- [ ] query dimension is 1536
- [ ] cosine distance is used
- [ ] ascending distance order
- [ ] top-k is reasonable
- [ ] user authorization is enforced
