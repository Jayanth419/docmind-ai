from sqlalchemy.orm import Session

from app.database.models import Document
from app.schemas.documents import DocumentCreate


def create_document(
    db: Session,
    user_id: int,
    document_data: DocumentCreate,
) -> Document:
    document = Document(
        user_id=user_id,
        title=document_data.title,
        description=document_data.description,
        file_name=document_data.file_name,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document

def get_document(
    db: Session,
    document_id: int,
    user_id: int,
) -> Document | None:
    return (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == user_id,
        )
        .first()
    )

def list_documents(
    db: Session,
    user_id: int,
    status_filter: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> list[Document]:

    query = (
        db.query(Document)
        .filter(
            Document.user_id == user_id
        )
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
def update_document(
    db: Session,
    document_id: int,
    user_id: int,
    title: str | None,
    description: str | None,
) -> Document | None:

    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == user_id,
        )
        .first()
    )

    if not document:
        return None

    if title is not None:
        document.title = title

    if description is not None:
        document.description = description

    db.commit()
    db.refresh(document)

    return document

def delete_document(
    db: Session,
    document_id: int,
    user_id: int,
) -> bool:

    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == user_id,
        )
        .first()
    )

    if not document:
        return False

    db.delete(document)
    db.commit()

    return True