import pytest

# The module does NOT exist yet.
# This import should fail until the AI agent implements it.
from skills.skill_trend_fetcher.trend_fetcher import fetch_trends


def test_fetch_trends_returns_list():
    """
    Contract Test:
    fetch_trends should return a list of trend objects.
    """
    trends = fetch_trends(source="linkedin", limit=5)

    assert isinstance(trends, list), "Expected fetch_trends to return a list"


def test_each_trend_has_required_fields():
    """
    Contract Test:
    Each trend item must conform to the API contract defined in technical.md
    """
    trends = fetch_trends(source="linkedin", limit=3)

    required_fields = {
        "skill_name",
        "source",
        "confidence_score",
        "timestamp"
    }

    for trend in trends:
        assert isinstance(trend, dict), "Each trend must be a dictionary"

        missing_fields = required_fields - trend.keys()
        assert not missing_fields, f"Missing required fields: {missing_fields}"


def test_confidence_score_is_valid_range():
    """
    Contract Test:
    confidence_score must be a float between 0.0 and 1.0
    """
    trends = fetch_trends(source="linkedin", limit=3)

    for trend in trends:
        score = trend["confidence_score"]
        assert isinstance(score, float), "confidence_score must be a float"
        assert 0.0 <= score <= 1.0, "confidence_score must be between 0.0 and 1.0"


def test_invalid_source_raises_error():
    """
    Contract Test:
    Invalid sources should raise a ValueError
    """
    with pytest.raises(ValueError):
        fetch_trends(source="unknown_source", limit=5)


def test_limit_must_be_positive_integer():
    """
    Contract Test:
    limit must be a positive integer
    """
    with pytest.raises(ValueError):
        fetch_trends(source="linkedin", limit=0)

    with pytest.raises(ValueError):
        fetch_trends(source="linkedin", limit=-1)

    with pytest.raises(TypeError):
        fetch_trends(source="linkedin", limit="five")
