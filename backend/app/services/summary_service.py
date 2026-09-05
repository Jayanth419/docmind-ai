from app.services.openrouter_service import OpenRouterService


class SummaryService:

    def __init__(self):
        self.openrouter_service = OpenRouterService()

    def build_chunk_summary_prompt(self, text: str) -> str:
        return f"""
You are a document summarization assistant.

Summarize the following document section.

Rules:
- Use only the information provided.
- Do not invent facts.
- Preserve important facts, numbers, dates, names, and decisions.
- Remove unnecessary repetition.
- Keep the summary concise.
- Do not add information that is not present in the text.

Document section:
----------------
{text}
----------------

Summary:
"""

    def build_final_summary_prompt(self, summaries: list[str]) -> str:
        combined_summaries = "\n\n".join(
            f"Section {index + 1}:\n{summary}"
            for index, summary in enumerate(summaries)
        )

        return f"""
You are a document summarization assistant.

Create a final summary from the section summaries below.

Rules:
- Use only the provided information.
- Do not invent facts.
- Preserve important facts, numbers, dates, and decisions.
- Remove duplicate information.
- Organize the result clearly.
- Focus on the most important information.
- Do not mention that the summary was generated from sections.

Section summaries:
----------------
{combined_summaries}
----------------

Final Summary:
"""

    def summarize_chunk(self, text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        prompt = self.build_chunk_summary_prompt(text)

        return self.openrouter_service.generate_answer(prompt)

    def summarize_document(self, chunks: list[str]) -> str:
        if not chunks:
            raise ValueError("Document contains no text")

        summaries = []

        for chunk in chunks:
            if chunk and chunk.strip():
                summary = self.summarize_chunk(chunk)
                summaries.append(summary)

        if not summaries:
            raise ValueError("Document contains no usable text")

        if len(summaries) == 1:
            return summaries[0]

        final_prompt = self.build_final_summary_prompt(summaries)

        return self.openrouter_service.generate_answer(final_prompt)


summary_service = SummaryService()