Week 3 — DocMind AI
Theme
Authentication, Authorization, Service Layer, File Upload, and Testing

1. Week 3 Goal
   This week focused on converting the basic CRUD application into a more secure and maintainable backend.
   By the end of Week 3, the project supports:

- User authentication
- Password hashing
- JWT authentication
- Protected endpoints
- User-document ownership
- Service-layer architecture
- File upload
- File storage
- Basic automated testing

2. Topics Completed
   Day 15 — Authentication
   Implemented:

- Password hashing
- Login endpoint
- JWT access tokens
- OAuth2 password flow
- Token validation
  Main files:
  app/core/security.py
  app/core/config.py
  app/schemas/auth.py
  app/routes/auth.py
  Day 16 — JWT & Protected Endpoints
  Implemented:
- OAuth2PasswordBearer
- JWT decoding
- Current-user dependency
- Protected API endpoints
  Main file:
  app/core/dependencies.py
  Important function:
  get_current_user()
  Flow:
  Login
  ↓
  JWT Token
  ↓
  Authorization Header
  ↓
  get_current_user()
  ↓
  Current User
  Day 17 — Authorization
  Implemented document ownership.
  Instead of trusting:
  user_id from request
  the application uses:
  current_user.id
  This prevents users from accessing another user's documents.
  Day 18 — User-Document Relationship
  Implemented:
  User
  |
  +--- Document
  |
  +--- Document
  |
  +--- Document
  A user can own multiple documents.
  Database relationship:
  users.id
  ↑
  |
  documents.user_id
  Main file:
  app/database/models.py
  Day 19 — Service Layer
  Moved business logic out of the router.
  Architecture:
  Route
  ↓
  Service
  ↓
  Database
  Main service:
  app/services/document_service.py
  The router now mainly handles:
- HTTP request
- Authentication
- Validation
- Calling service
- HTTP response
  The service handles:
- Document operations
- Business rules
- Database queries
  Day 20 — File Upload & Storage
  Implemented:
  POST /documents/upload
  Created:
  app/services/storage_service.py
  app/services/document_upload_service.py
  Upload flow:
  User
  ↓
  Upload File
  ↓
  Authentication
  ↓
  Upload Service
  ↓
  Storage Service
  ↓
  Save File
  ↓
  Save Document Metadata

3. Important Architecture
   Week 3 introduced separation of responsibilities:
   FastAPI
   |
   v
   Routes
   |
   v
   Dependencies
   |
   v
   Services
   / \
    v v
   PostgreSQL Storage
4. Important Security Rule
   Never trust:
   user_id
   provided by the client for protected operations.
   Instead use:
   current_user.id
   obtained from the JWT.
   Example:
   document_service.get_document(
   db=db,
   document_id=document_id,
   user_id=current_user.id,
   )
5. Testing
   Testing was introduced using Pytest.
   Run:
   python -m pytest -v
   Run a specific test:
   python -m pytest tests/test_documents.py::test_create_document -v
   Testing includes:

- API tests
- Authentication tests
- Authorization tests
- Service-layer tests
- Document tests

6. Important Errors Solved
   Wrong import
   Incorrect:
   from backend.app.core.security import ...
   Correct:
   from app.core.security import ...
   Wrong Token import
   Incorrect:
   from multiprocessing.managers import Token
   Correct:
   from app.schemas.auth import Token
   /documents/me returning 422
   Cause:
   /documents/{document_id}
   was matching:
   /documents/me
   Specific routes should be defined before dynamic routes.
   Missing db_session
   If a test contains:
   def test_create_document(db_session):
   then db_session must exist as a pytest fixture in:
   tests/conftest.py
7. Week 3 Folder Structure
   backend/
   │
   ├── app/
   │ ├── core/
   │ │ ├── config.py
   │ │ ├── security.py
   │ │ └── dependencies.py
   │ │
   │ ├── database/
   │ │ ├── connection.py
   │ │ └── models.py
   │ │
   │ ├── routes/
   │ │ ├── users.py
   │ │ ├── auth.py
   │ │ └── documents.py
   │ │
   │ ├── schemas/
   │ │ ├── auth.py
   │ │ └── documents.py
   │ │
   │ └── services/
   │ ├── document_service.py
   │ ├── storage_service.py
   │ └── document_upload_service.py
   │
   └── tests/
   ├── conftest.py
   └── test_documents.py
8. Week 3 Architecture Principle
   The main lesson of Week 3:
   Don't put everything inside routes.
   Instead:
   Route
   ↓
   Service
   ↓
   Database / Storage
   This makes the application:

- Easier to test
- Easier to maintain
- Easier to debug
- Easier to scale

9. Week 3 Git Commits
   Recommended commits:
   git add .
   git commit -m "feat: add jwt authentication"
   git add .
   git commit -m "feat: protect document endpoints"
   git add .
   git commit -m "feat: add user document ownership"
   git add .
   git commit -m "refactor: add document service layer"
   git add .
   git commit -m "feat: add document file upload"
   git add .
   git commit -m "test: add document service tests"
10. Week 3 Outcome
    At the end of Week 3:
    User
    ↓
    Register
    ↓
    Login
    ↓
    JWT
    ↓
    Authenticated Request
    ↓
    Protected Document API
    ↓
    Service Layer
    ↓
    PostgreSQL
    ↓
    File Storage
    The backend foundation is now ready for the next stage:
    Document Processing
    ↓
    Text Extraction
    ↓
    Chunking
    ↓
    Embeddings
    ↓
    Vector Search
    ↓
    RAG
    ↓
    LLM
