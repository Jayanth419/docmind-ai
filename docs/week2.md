# 📄 DocMind AI — Week 2

## File Upload, Document Processing & Storage

**Days:** 7–13  
**Week 2 Goal:** Build the document upload and processing foundation for DocMind.

---

## Day 7 — File Upload Basics

- Learn FastAPI file uploads.
- Use `UploadFile`.
- Accept documents through an API.
- Validate uploaded files.
- Understand multipart/form-data.

**Flow:**

User
↓
Upload File
↓
FastAPI
↓
File Validation
↓
Storage

---

## Day 8 — File Validation

Implement validation for uploaded documents.

Validate:

- File extension
- MIME type
- File size
- Empty files

Supported documents:

PDF
DOCX

The API should reject unsupported or invalid files.

---

## Day 9 — File Storage Service

Create a dedicated storage service.

app/
└── services/
└── storage_service.py

The storage service handles:

- Saving files
- Generating file paths
- Checking file existence
- Deleting files

Keep file-writing logic out of the API routes.

---

## Day 10 — PDF Text Extraction

Use **PyMuPDF** to extract text from PDF files.

PDF
↓
PyMuPDF
↓
Pages
↓
Extracted Text

Learn:

- Opening PDFs
- Reading pages
- Extracting text
- Handling empty PDFs
- Handling corrupted PDFs

---

## Day 11 — DOCX Text Extraction

Use `python-docx` to extract text from Word documents.

DOCX
↓
python-docx
↓
Paragraphs
↓
Extracted Text

The application should provide a common document-processing flow for PDF and DOCX files.

---

## Day 12 — Document Upload Integration

Integrate the pieces:

Upload
↓
Validate
↓
Store
↓
Extract Text
↓
Create Document Record

Connect:

- FastAPI
- Storage Service
- PDF processor
- DOCX processor
- PostgreSQL

---

## Day 13 — Week 2 Review

Review and integrate:

File Upload
↓
Validation
↓
Storage
↓
Text Extraction
↓
Document Database Record

### Review Tasks

- Test PDF upload.
- Test DOCX upload.
- Test invalid files.
- Test large files.
- Test corrupted files.
- Review storage paths.
- Review error handling.
- Refactor services.
- Run tests.
- Update documentation.

---

# 🏗️ Week 2 Architecture

FastAPI
│
▼
Upload Route
│
┌──────┴──────┐
▼ ▼
File Validation Storage
│
▼
Local Storage
│
▼
Document Processor
│ │
▼ ▼
PDF DOCX
PyMuPDF python-docx
│ │
└────┬─────┘
▼
Extracted Text
│
▼
PostgreSQL

---

# 🎯 Week 2 Outcome

At the end of Week 2, DocMind has the foundation to:

Upload Document
↓
Validate Document
↓
Store Document
↓
Extract Text
↓
Save Document Information

This extracted text becomes the input for the **AI processing and chunking work in Week 4**.

---

## Week 2 Checklist

[ ] Day 7 — File Upload
[ ] Day 8 — File Validation
[ ] Day 9 — Storage Service
[ ] Day 10 — PDF Processing
[ ] Day 11 — DOCX Processing
[ ] Day 12 — Upload Integration
[ ] Day 13 — Weekly Review

[ ] PDF upload working
[ ] DOCX upload working
[ ] File validation working
[ ] Storage working
[ ] PDF text extraction working
[ ] DOCX text extraction working
[ ] Tests passing
[ ] Documentation updated
