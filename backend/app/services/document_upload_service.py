from pathlib import Path

from fastapi import UploadFile

from app.database.models import Document
from app.services.storage_service import StorageService


ALLOWED_FILE_TYPES = {
    "application/pdf": ".pdf",
    "text/plain": ".txt",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
}

MAX_FILE_SIZE = 10 * 1024 * 1024


def upload_document(
    db,
    storage: StorageService,
    user_id: int,
    file: UploadFile,
):
    if not file.filename:
        raise ValueError("File name is required")

    extension = ALLOWED_FILE_TYPES.get(
        file.content_type
    )

    if not extension:
        raise ValueError("Unsupported file type")

    file_path = None

    try:
        (
            stored_filename,
            file_path,
            file_size,
        ) = storage.save_file(
            file=file,
            extension=extension,
            max_size=MAX_FILE_SIZE,
        )

        document = Document(
            user_id=user_id,
            title=Path(file.filename).stem,
            description="Uploaded document",
            file_name=file.filename,
            stored_file_name=stored_filename,
            file_path=str(file_path),
            mime_type=file.content_type,
            file_size=file_size,
            status="uploaded",
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        if file_path and file_path.exists():
            file_path.unlink()

        raise