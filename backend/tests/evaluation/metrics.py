def hit_rate_at_k(
    retrieved_chunk_ids: list[list[int]],
    relevant_chunk_ids: list[list[int]],
) -> float:

    if not relevant_chunk_ids:
        return 0.0

    hits = 0

    for retrieved, relevant in zip(
        retrieved_chunk_ids,
        relevant_chunk_ids,
    ):

        if any(
            chunk_id in relevant
            for chunk_id in retrieved
        ):
            hits += 1

    return hits / len(relevant_chunk_ids)


def precision_at_k(
    retrieved_chunk_ids: list[int],
    relevant_chunk_ids: list[int],
    k: int,
) -> float:

    retrieved = retrieved_chunk_ids[:k]

    if not retrieved:
        return 0.0

    relevant_count = sum(
        chunk_id in relevant_chunk_ids
        for chunk_id in retrieved
    )

    return relevant_count / len(retrieved)