from pydantic import BaseModel, Field


class SummaryResponse(BaseModel):
    summary: str = Field(
        ...,
        description="Concise summary of the document",
    )

    key_points: list[str] = Field(
        default_factory=list,
        description="Important points from the document",
    )

    important_dates: list[str] = Field(
        default_factory=list,
        description="Important dates mentioned in the document",
    )

    important_numbers: list[str] = Field(
        default_factory=list,
        description="Important numerical information",
    )