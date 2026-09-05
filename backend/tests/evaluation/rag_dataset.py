RAG_EVALUATION_DATASET = [
    {
        "question": "How many days of annual leave do employees receive?",
        "expected_answer": (
            "Employees receive twenty days of annual leave."
        ),
        "relevant_chunk_ids": [1],
    },
    {
        "question": "How do employees request vacation?",
        "expected_answer": (
            "Employees request vacation through the HR portal."
        ),
        "relevant_chunk_ids": [2],
    },
    {
        "question": "What database is used for relational database storage?",
        "expected_answer": (
            "PostgreSQL is used for relational database storage."
        ),
        "relevant_chunk_ids": [3],
    },
]

{
    "question": "How many sick days do employees receive?",
    "expected_answer": None,
    "relevant_chunk_ids": [],
}