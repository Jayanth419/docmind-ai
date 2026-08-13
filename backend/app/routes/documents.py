from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Document
from app.schemas.documents import DocumentCreate
from app.schemas.documents import DocumentUpdate
from app.schemas.documents import DocumentResponse

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return {
        "id": document.id,
        "title": document.title,
        "description": document.description,
        "status": document.status,
    }


@router.get("")
def list_documents(
    status: str | None = None,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Document)

    if status:
        query = query.filter(Document.status == status)

    documents = query.limit(limit).all()

    return [
        {
            "id": document.id,
            "title": document.title,
            "description": document.description,
            "status": document.status,
        }
        for document in documents
    ]

@router.post("")
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
):
    new_document = Document(
        title=document.title,
        description=document.description,
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return {
        "id": new_document.id,
        "title": new_document.title,
        "description": new_document.description,
        "status": new_document.status,
    }

# delete api

@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }

@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
)
def update_document(
    document_id: int,
    document_data: DocumentUpdate,
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    if document_data.title is not None:
        document.title = document_data.title

    if document_data.description is not None:
        document.description = document_data.description

    db.commit()
    db.refresh(document)

    return document

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document


@router.get(
    "",
    response_model=list[DocumentResponse],
)
def list_documents(
    status: str | None = None,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Document)

    if status:
        query = query.filter(
            Document.status == status
        )

    return query.limit(limit).all()