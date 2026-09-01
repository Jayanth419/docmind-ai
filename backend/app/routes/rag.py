from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.rag import (
    QuestionRequest,
    QuestionResponse,
)
from app.services.rag_service import rag_service

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.post(
    "/ask",
    response_model=QuestionResponse,
)
def ask_question(
    request: QuestionRequest,
    db: Session = Depends(get_db),
):
    # Use your existing authentication dependency here.
    # For example, you might get the user ID from the access token.
    user_id = 11

    answer = rag_service.answer_question(
        db=db,
        user_id=user_id,
        question=request.question,
        limit=request.limit,
    )

    return QuestionResponse(
        answer=answer
    )