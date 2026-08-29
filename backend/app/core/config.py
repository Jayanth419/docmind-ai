from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]

STORAGE_DIR = Path(
    os.getenv(
        "STORAGE_DIR",
        str(BASE_DIR / "storage"),
    )
)

DOCUMENT_STORAGE_DIR = STORAGE_DIR / "documents"
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not configured")

ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256",
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "30",
    )
)
# Embedding configuration

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "openai/text-embedding-3-small",
)

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY",
)

if not OPENROUTER_API_KEY:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not configured"
    )