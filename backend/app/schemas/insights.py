from pydantic import BaseModel, Field


class ClassificationResult(BaseModel):
    category: str = Field(
        min_length=1,
        max_length=100,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )


class DocumentInsightsResponse(BaseModel):
    key_points: list[str] = Field(
        default_factory=list,
        max_length=10,
    )

    keywords: list[str] = Field(
        default_factory=list,
        max_length=15,
    )

    classification: ClassificationResult