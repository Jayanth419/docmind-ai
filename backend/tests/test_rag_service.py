from types import SimpleNamespace

from app.services.rag_service import RAGService


def test_build_context():

    service = RAGService()

    chunks = [
        SimpleNamespace(
            page_number=1,
            text="Employees receive 24 days of leave.",
        ),
        SimpleNamespace(
            page_number=2,
            text="Leave requests require manager approval.",
        ),
    ]

    context = service.build_context(chunks)

    assert "Employees receive 24 days of leave." in context
    assert "Leave requests require manager approval." in context
    assert "[Page 1]" in context
    assert "[Page 2]" in context


def test_build_prompt():

    service = RAGService()

    context = (
        "Employees receive 24 days of annual leave."
    )

    prompt = service.build_prompt(
        question="How many leave days?",
        context=context,
    )

    assert "How many leave days?" in prompt
    assert "24 days" in prompt
    assert "Do not invent facts." in prompt