from io import BytesIO


def test_upload_pdf(client, auth_headers):

    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "test.pdf",
                BytesIO(
                    b"%PDF-1.4 test content"
                ),
                "application/pdf",
            )
        },
        headers=auth_headers,
    )

    assert response.status_code == 201