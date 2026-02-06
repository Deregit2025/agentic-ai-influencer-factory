from datetime import datetime
from typing import List, Dict

ALLOWED_SOURCES = {"linkedin", "twitter", "github"}


def fetch_trends(source: str, limit: int) -> List[Dict]:
    """Return a list of synthetic trend objects for the given source.

    This implementation is a simple, deterministic stub used by contract
    tests. It validates inputs and returns `limit` dictionaries containing
    the required fields.
    """
    if not isinstance(source, str):
        raise TypeError("source must be a string")

    src = source.lower()
    if src not in ALLOWED_SOURCES:
        raise ValueError(f"Unknown source: {source}")

    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit <= 0:
        raise ValueError("limit must be a positive integer")

    trends = []
    for i in range(limit):
        # produce a confidence score in (0,1) inclusive
        score = float((i + 1) / (limit + 1))

        trends.append({
            "skill_name": f"Skill {i+1}",
            "source": src,
            "confidence_score": float(round(score, 6)),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        })

    return trends
