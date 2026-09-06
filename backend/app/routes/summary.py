from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.summary import SummaryResponse
from app.services.summary_service import summary_service


router = APIRouter(
    prefix="/summary",
    tags=["Summary"],
)


@router.post(
    "/structured/{document_id}",
    response_model=SummaryResponse,
)
def structured_summary(
    document_id: int,
    db: Session = Depends(get_db),
):
    try:
        # Temporary Day 32 test data.
        # We will replace this with real document chunks
        # during the integration phase.

        text = """
        The company was founded in 2018.

        It currently has 350 employees.

        Employees receive 20 days of annual leave.

        Vacation requests must be submitted through
        the HR portal.

        The annual leave policy was updated in January 2026.
        """

        return summary_service.summarize_structured(text)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )