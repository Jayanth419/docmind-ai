from pydantic import BaseModel
from datetime import datetime


class DocumentCreate(BaseModel):
    title: str
    description: str

class DocumentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class DocumentResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True