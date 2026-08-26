from app.services.text_cleaning_service import (
    TextCleaningService,
)


def test_clean_multiple_spaces():
    service = TextCleaningService()

    text = "Hello     World"

    result = service.clean(text)

    assert result == "Hello World"

def test_clean_line_endings():
    service = TextCleaningService()

    text = "Hello\r\nWorld\rTest"

    result = service.clean(text)

    assert result == "Hello\nWorld\nTest"

def test_clean_blank_lines():
    service = TextCleaningService()

    text = "Hello\n\n\n\nWorld"

    result = service.clean(text)

    assert result == "Hello\n\nWorld"

def test_clean_surrounding_whitespace():
    service = TextCleaningService()

    text = "   Hello World   "

    result = service.clean(text)

    assert result == "Hello World"

def test_clean_empty_text():
    service = TextCleaningService()
    text = "  "
    result = service.clean("")

    assert result == ""

def test_clean_preserves_meaningful_content():
    service = TextCleaningService()

    text = """
    Email: hello@example.com

    Salary: $50,000

    Section 3.2
    """

    result = service.clean(text)

    assert "hello@example.com" in result
    assert "$50,000" in result
    assert "Section 3.2" in result