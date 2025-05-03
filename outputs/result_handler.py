def format_output(candidates: list) -> dict:
    # For now, return them directly — later, we can add filters/ranking
    return {
        "status": "success",
        "num_candidates": len(candidates),
        "candidates": candidates
    }
