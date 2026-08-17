from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from starlette import status

from app.database.connection import get_db
from app.database.models import Document
from app.schemas.documents import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.get(
    "",
    response_model=list[DocumentResponse],
)
def list_documents(
    status: str | None = None,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    statement = select(Document)

    if status:
        statement = statement.where(
            Document.status == status
        )

    statement = statement.limit(limit)

    documents = db.scalars(statement).all()

    return documents


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


@router.post(
    "",
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

    try:
        db.add(document)
        db.commit()
        db.refresh(document)

    except SQLAlchemyError:
        db.rollback()
        raise

    return document


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

    try:
        db.commit()
        db.refresh(document)

    except SQLAlchemyError:
        db.rollback()
        raise

    return document


@router.delete(
    "/{document_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
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

    try:
        db.delete(document)
        db.commit()

    except SQLAlchemyError:
        db.rollback()
        raise

    return None