Document:

Document
↓
Extraction
↓
Chunking
↓
Embedding
↓
PostgreSQL
↓
pgvector
↓
Similarity Search

Then document responsibilities:

EmbeddingService
→ generates embeddings

DocumentChunk
→ stores chunks and vectors

VectorSearchService
→ retrieves similar chunks

OpenRouterService
→ generates AI responses
