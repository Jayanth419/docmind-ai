from tests.evaluation.metrics import hit_rate_at_k
from tests.evaluation.metrics import precision_at_k


def test_hit_rate_at_k():

    retrieved = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    relevant = [
        [2],
        [10],
        [8],
    ]

    result = hit_rate_at_k(
        retrieved_chunk_ids=retrieved,
        relevant_chunk_ids=relevant,
    )

    assert result == 2 / 3
    
def test_precision_at_k():

    retrieved = [1, 2, 3, 4, 5]

    relevant = [1, 2]

    result = precision_at_k(
        retrieved_chunk_ids=retrieved,
        relevant_chunk_ids=relevant,
        k=5,
    )

    assert result == 0.4