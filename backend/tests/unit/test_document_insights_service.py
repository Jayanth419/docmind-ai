from app.services.document_insights_service import (
    DocumentInsightsService,
)


def test_build_prompt_contains_text():
    service = DocumentInsightsService()

    prompt = service.build_prompt(
        "Employees receive 20 days of annual leave."
    )

    assert "20 days" in prompt
    assert "Do not invent facts." in prompt
    assert "Return ONLY valid JSON." in prompt

def test_parse_valid_response():
    service = DocumentInsightsService()

    response = """
    {
        "key_points": [
            "Employees receive 20 days of annual leave."
        ],
        "keywords": [
            "annual leave"
        ],
        "classification": {
            "category": "HR Policy",
            "confidence": 0.95
        }
    }
    """

    result = service.parse_response(response)

    assert result.key_points == [
        "Employees receive 20 days of annual leave."
    ]

    assert result.keywords == [
        "annual leave"
    ]

    assert result.classification.category == "HR Policy"
    assert result.classification.confidence == 0.95

def test_parse_invalid_json():
    service = DocumentInsightsService()

    response = "This is not JSON"

    try:
        service.parse_response(response)
        assert False
    except ValueError as exc:
        assert str(exc) == "LLM returned invalid JSON"


def test_analyze_empty_text():
    service = DocumentInsightsService()

    try:
        service.analyze("")
        assert False
    except ValueError as exc:
        assert str(exc) == "Text cannot be empty"

def test_invalid_confidence():
    service = DocumentInsightsService()

    response = """
    {
        "key_points": [],
        "keywords": [],
        "classification": {
            "category": "HR Policy",
            "confidence": 1.5
        }
    }
    """

    try:
        service.parse_response(response)
        assert False
    except Exception:
        assert True

def test_analyze_document(mocker):
    service = DocumentInsightsService()

    mocker.patch.object(
        service.openrouter_service,
        "generate_answer",
        return_value="""
        {
            "key_points": [
                "Employees receive 20 days of annual leave."
            ],
            "keywords": [
                "annual leave",
                "HR portal"
            ],
            "classification": {
                "category": "HR Policy",
                "confidence": 0.95
            }
        }
        """,
    )

    result = service.analyze(
        "Employees receive 20 days of annual leave."
    )

    assert len(result.key_points) == 1
    assert "annual leave" in result.keywords
    assert result.classification.category == "HR Policy"