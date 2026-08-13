from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to DocMind AI"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_get_document():
    response = client.get("/documents/4")

    assert response.status_code == 200

    assert response.json()["id"] == 4


def test_create_document():
    response = client.post(
        "/documents",
        json={
            "title": "Python Notes",
            "description": "Learning Python"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Python Notes"
    assert data["description"] == "Learning Python"


def test_invalid_document():
    response = client.post(
        "/documents",
        json={
            "title": "Missing description"
        }
    )

    assert response.status_code == 422

def test_create_document_invalid_title():
    response = client.post(
        "/documents",
        json={
            "title": "A",
            "description": "Testing validation",
        },
    )

    assert response.status_code == 422

def test_get_missing_document():
    response = client.get(
        "/documents/999999"
    )

    assert response.status_code == 404