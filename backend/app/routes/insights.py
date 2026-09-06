from fastapi import APIRouter, HTTPException

from app.schemas.insights import DocumentInsightsResponse
from app.services.document_insights_service import (
    document_insights_service,
)


router = APIRouter(
    prefix="/insights",
    tags=["Document Insights"],
)


@router.post(
    "/{document_id}",
    response_model=DocumentInsightsResponse,
)
def get_document_insights(
    document_id: int,
):
    try:
        # Temporary Day 33 test data.
        # Real document retrieval will be connected
        # after the AI capability layer is complete.

        text = """
        The company was founded in 2018.

        It currently has 350 employees.

        Employees receive 20 days of annual leave.

        Vacation requests must be submitted through
        the HR portal.

        The annual leave policy was updated in January 2026.
        """

        return document_insights_service.analyze(text)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )