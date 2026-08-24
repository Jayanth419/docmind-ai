from pathlib import Path
from uuid import uuid4


class StorageService:

    def __init__(self, storage_dir: Path):
        self.storage_dir = storage_dir

    def save_file(
        self,
        file,
        extension: str,
        max_size:int,
    ) -> tuple[str, Path,int]:

        file_id = uuid4().hex

        stored_filename = (
            f"{file_id}{extension}"
        )

        self.storage_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = (
            self.storage_dir /
            stored_filename
        )
        total_size = 0

        try:
            with file_path.open("wb") as buffer:

                while chunk := file.file.read(
                    1024 * 1024
                ):

                    total_size += len(chunk)

                    if total_size > max_size:
                        raise ValueError(
                            "File exceeds maximum size"
                        )

                    buffer.write(chunk)

        except Exception:
            if file_path.exists():
                file_path.unlink()

            raise

        return (
            stored_filename,
            file_path,
            total_size,
        )