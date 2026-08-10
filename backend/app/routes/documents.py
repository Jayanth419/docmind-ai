from fastapi import APIRouter

from app.schemas.documents import DocumentCreate

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/{document_id}")
def get_document(document_id: int):
    return {
        "document_id": document_id
    }


@router.get("")
def list_documents(
    status: str | None = None,
    limit: int = 10
):
    return {
        "status": status,
        "limit": limit
    }


@router.post("")
def create_document(document: DocumentCreate):
    return {
        "title": document.title,
        "description": document.description
    }