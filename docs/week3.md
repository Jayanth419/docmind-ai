# 📄 DocMind AI — Week 3

## Backend Architecture, Services & Authentication

**Days:** 14–20  
**Week 3 Goal:** Improve the backend architecture, introduce authentication, enforce document ownership, and separate business logic from API routes.

---

## Day 14 — Backend Architecture

Review the existing FastAPI project and introduce a cleaner architecture.

app/
├── core/
├── database/
├── routes/
├── schemas/
└── services/

Understand the responsibility of each layer.

### Main principle

Route
↓
Service
↓
Database

Routes should not contain all the business logic.

---

## Day 15 — JWT Authentication

Implement user authentication using JWT.

Login
↓
Verify Email + Password
↓
Create JWT
↓
Return Access Token

Learn:

- Password hashing
- Password verification
- JWT creation
- JWT payload
- Access tokens
- OAuth2 password flow

Swagger can be used to test authentication.

---

## Day 16 — Protect API Endpoints

Create authentication dependencies.

Authorization Header
↓
Bearer Token
↓
JWT Validation
↓
Current User
↓
Protected Endpoint

Example:

GET /documents

should require authentication.

Without a valid token:

401 Unauthorized

---

## Day 17 — Service Layer Refactoring

Move business logic from routes into services.

For example:

app/
└── services/
└── document_service.py

Instead of:

Route
└── SQLAlchemy queries

use:

Route
↓
document_service
↓
Database

This makes the application easier to test and maintain.

---

## Day 18 — User-Document Relationship

Connect users with their documents.

User
│
└── Documents
├── Document 1
├── Document 2
└── Document 3

Database relationship:

users.id
│
▼
documents.user_id

A document belongs to a specific user.

---

## Day 19 — Document Ownership & Authorization

Authentication tells us:

> Who is the user?

Authorization tells us:

> Is this user allowed to access this document?

Implement ownership checks.

Current User
↓
Document
↓
Check document.user_id
↓
Allow / Reject

A user must not be able to access another user's document simply by changing:

/document_id

---

## Day 20 — Week 3 Review

Review and refactor the backend.

### Review Tasks

- Review JWT authentication.
- Review protected endpoints.
- Review current-user dependency.
- Review user-document relationship.
- Review authorization.
- Move SQLAlchemy/business logic into services.
- Remove unnecessary imports and duplicated code.
- Write service-layer tests.
- Run the complete test suite.
- Update README/documentation.
- Push changes to GitHub.

---

# 🏗️ Week 3 Architecture

                    FastAPI
                       │
                       ▼
                    Routes
                       │
                       ▼
                 Dependencies
                       │
                       ▼
              Authentication
                       │
                       ▼
                  Services
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Document Service      User Service
             │                   │
             └─────────┬─────────┘
                       ▼
                  SQLAlchemy
                       │
                       ▼
                  PostgreSQL

---

# 🎯 Week 3 Outcome

At the end of Week 3, DocMind has a more production-style backend:

User
↓
Login
↓
JWT Token
↓
Protected API
↓
Current User
↓
Authorization
↓
Document Service
↓
PostgreSQL

The backend is now ready for the AI layer.

---

## Week 3 Checklist

[ ] Day 14 — Backend Architecture
[ ] Day 15 — JWT Authentication
[ ] Day 16 — Protected Endpoints
[ ] Day 17 — Service Layer
[ ] Day 18 — User-Document Relationship
[ ] Day 19 — Document Authorization
[ ] Day 20 — Weekly Review

[ ] JWT working
[ ] Swagger authentication working
[ ] Protected endpoints working
[ ] Current user dependency working
[ ] User-document relationship working
[ ] Ownership checks working
[ ] Service layer implemented
[ ] Service tests passing
[ ] Documentation updated
[ ] GitHub updated
