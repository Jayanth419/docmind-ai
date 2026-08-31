# 📄 DocMind AI — Week 1

## Project Setup, FastAPI & Database Fundamentals

**Days:** 1–6  
**Day 7:** Monday Review  
**Week 1 Goal:** Build the basic backend foundation of DocMind AI using Python, FastAPI, PostgreSQL, and SQLAlchemy.

---

## Day 1 — Project Setup & Python Environment

- Understand the DocMind AI project.
- Create the backend project structure.
- Create a Python virtual environment.
- Install required packages.
- Understand `requirements.txt`.
- Configure Git and `.gitignore`.

### Basic structure

text
docmind-ai/
│
├── backend/
│ ├── app/
│ ├── tests/
│ ├── requirements.txt
│ └── .gitignore
│
├── frontend/
│
├── docs/
│
└── README.md

### Environment

bash
python -m venv .venv

Activate:

bash
.venv\Scripts\Activate

---

## Day 2 — FastAPI Fundamentals

Learn the basics of FastAPI.

Create:

text
app/main.py

Basic application:

text
Client
↓
FastAPI
↓
Route
↓
Response

Learn:

- FastAPI application
- Routes
- HTTP methods
- Request/response
- Status codes
- Swagger
- ReDoc

Swagger:

text
http://127.0.0.1:8000/docs

---

## Day 3 — REST API & Pydantic Schemas

Learn how APIs receive and validate data.

Create:

text
app/
├── routes/
└── schemas/

Use Pydantic schemas for request validation.

Example:

text
Client
↓
JSON Request
↓
Pydantic Schema
↓
Validation
↓
Route

Learn:

- GET
- POST
- PUT
- DELETE
- Request body
- Query parameters
- Path parameters
- Pydantic validation
- HTTP status codes

---

## Day 4 — PostgreSQL & SQLAlchemy

Introduce the database layer.

text
FastAPI
↓
SQLAlchemy
↓
PostgreSQL

Learn:

- PostgreSQL database
- Tables
- Columns
- Primary keys
- Foreign keys
- SQLAlchemy models
- Database sessions
- CRUD operations

Create:

text
app/database/
├── connection.py
└── models.py

---

## Day 5 — Database Migrations with Alembic

Introduce Alembic for database schema migrations.

text
SQLAlchemy Model
↓
Alembic
↓
Migration
↓
PostgreSQL

Learn:

- Why migrations are needed
- Creating migrations
- Applying migrations
- Checking migration status
- Rolling back migrations

Common commands:

bash
alembic revision --autogenerate -m "create documents table"

bash
alembic upgrade head

bash
alembic current

---

## Day 6 — Document CRUD API

Build the first real DocMind feature: document management.

Create:

text
app/
├── routes/
│ └── documents.py
│
├── schemas/
│ └── documents.py
│
└── database/
└── models.py

Implement:

text
POST /documents
GET /documents
GET /documents/{id}
PUT /documents/{id}
DELETE /documents/{id}

### Flow

text
Client
↓
FastAPI Route
↓
Pydantic Schema
↓
SQLAlchemy
↓
PostgreSQL

---

## Day 7 — Week 1 Review

Review the complete backend foundation.

### Review Tasks

- Review Python virtual environments.
- Review FastAPI.
- Review REST APIs.
- Review Pydantic.
- Review PostgreSQL.
- Review SQLAlchemy.
- Review Alembic.
- Test document CRUD.
- Fix bugs.
- Refactor code.
- Write tests.
- Update README.
- Commit and push to GitHub.

---

# 🏗️ Week 1 Architecture

text
DocMind AI
│
▼
FastAPI App
│
┌───────┴───────┐
│ │
▼ ▼
Routes Schemas
│
▼
SQLAlchemy
│
▼
PostgreSQL
▲
│
Alembic

---

# 📁 Week 1 Project Structure

text
backend/
│
├── app/
│ ├── **init**.py
│ ├── main.py
│ │
│ ├── routes/
│ │ ├── **init**.py
│ │ └── documents.py
│ │
│ ├── schemas/
│ │ ├── **init**.py
│ │ └── documents.py
│ │
│ └── database/
│ ├── **init**.py
│ ├── connection.py
│ └── models.py
│
├── tests/
│ └── test_documents.py
│
├── alembic/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md

---

# 🎯 Week 1 Outcome

By the end of Week 1, you should have:

text
FastAPI Backend
↓
REST API
↓
Pydantic Validation
↓
SQLAlchemy
↓
PostgreSQL
↓
Alembic Migrations
↓
Document CRUD

DocMind starts as a basic backend and is then extended week by week.

---

## Week 1 Checklist

text
[ ] Day 1 — Project Setup
[ ] Day 2 — FastAPI Fundamentals
[ ] Day 3 — REST API + Pydantic
[ ] Day 4 — PostgreSQL + SQLAlchemy
[ ] Day 5 — Alembic
[ ] Day 6 — Document CRUD
[ ] Day 7 — Weekly Review

[ ] Virtual environment working
[ ] FastAPI working
[ ] Swagger working
[ ] PostgreSQL connected
[ ] SQLAlchemy models working
[ ] Alembic migrations working
[ ] Document CRUD working
[ ] Tests written
[ ] README updated
[ ] GitHub updated
