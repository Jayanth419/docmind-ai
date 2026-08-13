from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    return {
        "id": document.id,
        "title": document.title,
        "description": document.description,
        "status": document.status,
    }


@router.get(
        "",
    response_model=list[DocumentResponse],
)
def list_documents(
    status_filter: str | None = None,
    limit: int = 10,
    offset: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Document)

    if status_filter:
        query = query.filter(Document.status == status_filter)

    documents = query.limit(limit).offset(offset).all()

    return [
        {
            "id": document.id,
            "title": document.title,
            "description": document.description,
            "status": document.status,
            "created_at": document.created_at,
            "updated_at": document.updated_at,
        }
        for document in documents
    ]

@router.post(
        "" ,
        response_model=DocumentResponse,
        status_code=status.HTTP_201_CREATED,
)
def create_document(
        document_data: DocumentCreate,
        db: Session = Depends(get_db),
):
    document = Document(
        title=document_data.title,
        description=document_data.description,
    )

    db.add(document)
    db.commit()
    db.refresh(document)
    return {
        "id": document.id,
        "title": document.title,
        "description": document.description,
        "status": document.status,
         "created_at": document.created_at,
        "updated_at": document.updated_at,
    }

# delete api

@router.delete("/{document_id}",
               status_code=status.HTTP_204_NO_CONTENT,)
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    db.delete(document)
    db.commit()

    return None

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
            status_code=status.HTTP_404_NOT_FOUND,
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
            status_code=status.HTTP_404_NOT_FOUND,
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