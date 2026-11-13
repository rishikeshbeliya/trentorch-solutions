def recommenders_top_k_filter(ids: list[int], scores: list[float], k: int) -> list[int]:
    """
    ids: unique candidate IDs.
    scores: scores[i] is the score for ids[i].
    k: number of top candidates to return.

    Sort by descending score, breaking ties by ascending ID. Return the
    first k IDs in that order.
    """
    # TODO: sort by (-score, id), then take the first k IDs.
    if k <= 0:
        return []
        
    pair = zip(ids, scores)
    sorted_pair = sorted (pair, key= lambda x: (-x[1], x[0]))
    return [top_k for top_k, _ in sorted_pair [:k]]
