from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.summary_service import summary_service


router = APIRouter(
    prefix="/summary",
    tags=["Summary"],
)


@router.post("/{document_id}")
def summarize_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    try:
        # Temporary implementation for Day 31.
        # We will connect this to the document database
        # in the next integration step.

        chunks = [
            "Employees receive twenty days of annual leave.",
            "Employees request vacation through the HR portal.",
            "PostgreSQL is used for relational database storage.",
        ]

        summary = summary_service.summarize_document(chunks)

        return {
            "document_id": document_id,
            "summary": summary,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )