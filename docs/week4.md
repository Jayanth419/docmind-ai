# 📄 DocMind AI — Week 4

## AI Integration, Embeddings & Vector Search

**Days:** 21–27  
**Week 4 Goal:** Integrate AI into DocMind and prepare document chunks for semantic search and RAG.

---

## Day 21 — AI Service Layer

- Create a separate service for AI operations.
- Connect DocMind with an LLM through OpenRouter.
- Keep AI logic outside FastAPI routes.
- Store API keys securely in `.env`.

**Flow:**

text
FastAPI
↓
AI Service
↓
OpenRouter
↓
LLM
↓
AI Response

---

## Day 22 — LLM Integration

- Send prompts to the LLM.
- Receive and process AI responses.
- Handle API errors.
- Test the AI service using Pytest.

The project uses OpenRouter so different AI models can be accessed through a common API.

---

## Day 23 — Text Chunking

Large documents need to be divided into smaller pieces.

text
Document
↓
Extract Text
↓
Split Text
↓
Chunk 1
Chunk 2
Chunk 3
...

### Why chunking?

- Reduces token usage.
- Makes retrieval more accurate.
- Helps stay within model context limits.
- Makes document search possible at a smaller level.

---

## Day 24 — Embeddings

Convert document chunks into numerical vectors.

text
Text Chunk
↓
Embedding Model
↓
Vector

This project uses **1536-dimensional embeddings**.

text
Embedding → [0.12, -0.43, 0.71, ...]
1536 values

The database vector dimension must match the embedding model dimension.

text
Model: 1536
Database: 1536

---

## Day 25 — Store Embeddings

Use PostgreSQL with **pgvector** to store embeddings.

text
Document
↓
Chunk
↓
Embedding
↓
PostgreSQL
↓
pgvector

The `DocumentChunk` table contains the document chunks and their embeddings.

Example:

text
DocumentChunk
├── id
├── document_id
├── chunk_text
├── chunk_index
├── page_number
└── embedding

---

## Day 26 — Vector Similarity Search

Search documents based on **meaning**, rather than only matching exact words.

text
User Question
↓
Question Embedding
↓
Vector Search
↓
Similar Chunks

Example:

text
Question:
"What is the leave allowance?"

Document:
"Employees receive 20 days of annual leave."

The words are different, but the meaning is related.

Cosine distance is used to compare vectors.

text
Smaller distance = More similar

---

## Day 27 — Week 4 Review

Review and integrate everything learned during the week.

### Complete pipeline

text
PDF / DOCX
↓
Text Extraction
↓
Text Chunking
↓
Embedding Generation
↓
1536-D Vector
↓
PostgreSQL + pgvector
↓
Vector Similarity Search
↓
Relevant Chunks

### Review Tasks

- Review AI service.
- Review OpenRouter integration.
- Review text chunking.
- Verify 1536 embedding dimensions.
- Verify pgvector.
- Test storing embeddings.
- Test similarity search.
- Review authentication and document ownership.
- Refactor code.
- Run tests.
- Update GitHub and documentation.

---

# 🏗️ Week 4 Architecture

text
DocMind AI
│
▼
FastAPI Backend
│
┌─────────┴─────────┐
│ │
▼ ▼
Document Services AI Services
│ │
▼ ┌─────┴─────┐
Chunking │ │
│ ▼ ▼
│ LLM Service Embedding
│ │ Service
│ ▼ │
│ OpenRouter │
│ │
└────────────┬─────────────┘
▼
PostgreSQL
│
▼
pgvector
│
▼
Vector Search

---

# 🎯 Week 4 Outcome

At the end of Week 4, DocMind can conceptually process documents like this:

text
Document
↓
Extract Text
↓
Create Chunks
↓
Generate Embeddings
↓
Store Vectors
↓
Search Similar Vectors
↓
Retrieve Relevant Content

This is the foundation required for **RAG**, which will allow DocMind to answer questions using the actual content of uploaded documents.

---

## Week 4 Checklist

[ ] Day 21 — AI Service Layer
[ ] Day 22 — LLM Integration
[ ] Day 23 — Text Chunking
[ ] Day 24 — Embeddings
[ ] Day 25 — Store Embeddings
[ ] Day 26 — Vector Similarity Search
[ ] Day 27 — Weekly Review

[ ] OpenRouter working
[ ] Embeddings working
[ ] 1536 dimensions verified
[ ] pgvector working
[ ] Vector search working
[ ] Tests passing
[ ] GitHub updated
