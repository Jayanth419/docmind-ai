import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database.connection import SessionLocal



@pytest.fixture
def client():
    return TestClient(app)
@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()