from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class DocumentCreate(BaseModel):
    # user_id: int

    title: str = Field(
        min_length=3,
        max_length=255,
    )

    description: str = Field(
        min_length=1,
        max_length=5000,
    )

    file_name: str | None = None
    
class DocumentUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=255,
    )

    description: str | None = Field(
        default=None,
        min_length=1,
        max_length=5000,
    )


class DocumentResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    file_name:str| None = None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
        )