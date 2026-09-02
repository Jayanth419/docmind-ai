from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):

    question: str = Field(
        min_length=1,
        max_length=2000,
    )

    limit: int = Field(
        default=5,
        ge=1,
        le=10,
    )


class SourceResponse(BaseModel):

    document_id: int
    chunk_id: int
    page_number: int | None


class QuestionResponse(BaseModel):

    answer: str
    sources: list[SourceResponse]