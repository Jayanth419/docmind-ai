from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# def test_root():
#     response = client.get("/")

#     assert response.status_code == 200

#     assert response.json() == {
#         "message": "Welcome to DocMind AI"
#     }


# def test_health():
#     response = client.get("/health")

#     assert response.status_code == 200

#     assert response.json()["status"] == "healthy"


# def test_get_document():
#     response = client.get("/documents/27")

#     assert response.status_code == 200

#     assert response.json()["id"] == 4


# # def test_create_document():
# #     response = client.post(
# #         "/documents",
# #         json={
# #             "title": "Python Notes",
# #             "description": "Learning Python"
# #         }
# #     )

# #     assert response.status_code == 201

# #     data = response.json()

# #     assert data["title"] == "Python Notes"
# #     assert data["description"] == "Learning Python"


# def test_invalid_document():
#     response = client.post(
#         "/documents",
#         json={
#             "title": "Missing description"
#         }
#     )

#     assert response.status_code == 422

# def test_create_document_invalid_title():
#     response = client.post(
#         "/documents",
#         json={
#             "title": "A",
#             "description": "Testing validation",
#         },
#     )

#     assert response.status_code == 422

# def test_get_missing_document():
#     response = client.get(
#         "/documents/999999"
#     )

#     assert response.status_code == 404

# def test_create_user(client):
#     response = client.post(
#         "/users",
#         json={
#             "email": "testuser@example.com",
#             "full_name": "Test User",
#         },
#     )

#     assert response.status_code == 201

#     data = response.json()

#     assert data["email"] == "testuser@example.com"
#     assert data["full_name"] == "Test User"

# def test_duplicate_user_email(client):
#     payload = {
#         "email": "duplicate@example.com",
#         "full_name": "Duplicate User",
#     }

#     first = client.post(
#         "/users",
#         json=payload,
#     )

#     assert first.status_code == 201

#     second = client.post(
#         "/users",
#         json=payload,
#     )

#     assert second.status_code == 409

# def test_document_ownership(client):
#     response = client.get(
#         "/documents?user_id=1"
#     )

#     assert response.status_code == 200

#     documents = response.json()

#     for document in documents:
#         assert document["user_id"] == 1

def test_login_success(client):
    client.post(
        "/users",
        json={
            "email": "jayanth@example.com",
            "full_name": "Jayanth",
            "password": "Test@123",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "jayanth@example.com",
            "password": "Test@123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    client.post(
        "/users",
        json={
            "email": "wrong@example.com",
            "full_name": "Wrong Password User",
            "password": "StrongPassword123!",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "wrong@example.com",
            "password": "WrongPassword!",
        },
    )

    assert response.status_code == 401