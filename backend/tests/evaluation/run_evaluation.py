from tests.evaluation.rag_dataset import (
    RAG_EVALUATION_DATASET,
)


def run_evaluation():

    for test_case in RAG_EVALUATION_DATASET:

        print("\nQUESTION:")
        print(test_case["question"])

        print("\nEXPECTED:")
        print(test_case["expected_answer"])

        print("\nRELEVANT CHUNKS:")
        print(test_case["relevant_chunk_ids"])


if __name__ == "__main__":
    run_evaluation()