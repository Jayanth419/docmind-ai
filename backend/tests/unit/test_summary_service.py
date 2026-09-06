from app.services.summary_service import SummaryService


def test_chunk_summary_prompt_contains_text():
    service = SummaryService()

    prompt = service.build_chunk_summary_prompt(
        "Employees receive twenty days of annual leave."
    )

    assert "twenty days" in prompt
    assert "Do not invent facts" in prompt


def test_final_summary_prompt_contains_summaries():
    service = SummaryService()

    prompt = service.build_final_summary_prompt(
        [
            "Employees receive twenty days of annual leave.",
            "Vacation requests are submitted through the HR portal.",
        ]
    )

    assert "twenty days" in prompt
    assert "HR portal" in prompt


def test_empty_document_raises_error():
    service = SummaryService()

    try:
        service.summarize_document([])
        assert False
    except ValueError as exc:
        assert str(exc) == "Document contains no text"


def test_summarize_document_uses_llm(mocker):
    service = SummaryService()

    mocker.patch.object(
        service.openrouter_service,
        "generate_answer",
        side_effect=[
            "Summary of section one.",
            "Summary of section two.",
            "Final document summary.",
        ],
    )

    result = service.summarize_document(
        [
            "Section one content.",
            "Section two content.",
        ]
    )

    assert result == "Final document summary."


def test_parse_structured_summary():
    service = SummaryService()

    response = """
    {
        "summary": "Employees receive annual leave.",
        "key_points": [
            "Employees receive 20 days of annual leave."
        ],
        "important_dates": [
            "January 2026"
        ],
        "important_numbers": [
            "20 days"
        ]
    }
    """

    result = service.parse_structured_summary(response)

    assert result.summary == "Employees receive annual leave."
    assert "20 days" in result.key_points[0]

def test_parse_invalid_json():
    service = SummaryService()

    response = "This is not JSON"

    try:
        service.parse_structured_summary(response)
        assert False
    except ValueError as exc:
        assert str(exc) == "LLM returned invalid JSON"

def test_parse_empty_response():
    service = SummaryService()

    try:
        service.parse_structured_summary("")
        assert False
    except ValueError as exc:
        assert str(exc) == "LLM returned an empty response"

def test_parse_invalid_schema():
    service = SummaryService()

    response = """
    {
        "summary": "Test",
        "key_points": "not a list",
        "important_dates": [],
        "important_numbers": []
    }
    """

    try:
        service.parse_structured_summary(response)
        assert False
    except Exception:
        assert True


