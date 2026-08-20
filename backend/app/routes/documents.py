from typing_extensions import Annotated

from app.schemas.auth import Token
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from starlette import status
from app.core.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models import Document, User
from app.schemas.documents import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse,
)
from app.core.security import (
    create_access_token,
    verify_password,
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
    status_filter: str | None = None,
    limit: int = 10,
    offset:int=0,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = (
        db.query(Document)
        .filter(Document.user_id == current_user.id)
    )


    if status_filter:
        query = query.filter(
            Document.status == status_filter
        )
    return (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )

@router.get("/me")
def read_current_user(
    current_user: Annotated[
        User,
        Depends(get_current_user),
    ],
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
    }

@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == current_user.id,
        )
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
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    document = Document(
        user_id=current_user.id,
        title=document_data.title,
        description=document_data.description,
        file_name=document_data.file_name
    )

    try:
        db.add(document)
        db.commit()
        db.refresh(document)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user_id",
        )

    return document


@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
)
def update_document(
    document_id: int,
    document_data: DocumentUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == current_user.id
        )
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
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == current_user.id
        )
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
