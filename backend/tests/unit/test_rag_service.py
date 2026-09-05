from types import SimpleNamespace

from app.services.rag_service import RAGService


def test_build_context():

    service = RAGService()

    results = [
        (
            SimpleNamespace(
                id=1,
                document_id=10,
                page_number=1,
                text="Employees receive twenty days of annual leave.",
            ),
            0.12,
        ),
        (
            SimpleNamespace(
                id=2,
                document_id=10,
                page_number=2,
                text="Employees request vacation through the HR portal.",
            ),
            0.20,
        ),
    ]

    context = service.build_context(results)

    assert "Employees receive twenty days" in context
    assert "Employees request vacation" in context
    assert "Page: 1" in context
    assert "Page: 2" in context


def test_build_sources():

    service = RAGService()

    results = [
        (
            SimpleNamespace(
                id=1,
                document_id=10,
                page_number=3,
                text="Example content.",
            ),
            0.12,
        )
    ]

    sources = service.build_sources(results)

    assert sources == [
        {
            "document_id": 10,
            "chunk_id": 1,
            "page_number": 3,
        }
    ]