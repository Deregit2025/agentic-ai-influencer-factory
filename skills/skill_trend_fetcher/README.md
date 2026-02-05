
# Skill: Trend Fetcher (`skill_trend_fetcher`)

## Purpose
The Trend Fetcher skill allows Chimera agents to autonomously identify trending topics from various social platforms. This provides the agent with actionable insights for content creation.

## Input
```json
{
  "platform": "string",   // e.g., "Twitter", "TikTok", "YouTube"
  "category": "string",   // e.g., "technology", "finance"
  "limit": "integer"      // number of trends to fetch
}
````

## Output

```json
{
  "trends": [
    {
      "title": "string",
      "url": "string",
      "engagement_score": "float",
      "timestamp": "ISO8601 datetime"
    }
  ]
}
```

## Usage Notes

* Always validate `platform`; unsupported platforms should return a clear error.
* Fetch only the most recent trends to ensure content relevance.
* Trends fetched are intended to feed into `skill_content_generator`.
* Logging and telemetry must be implemented to ensure traceability of fetch attempts.

## MCP & Traceability

* Integrate with `telemetry-mcp` to log all API calls and outcomes.
* Track failures and exceptions to allow debugging and performance analysis.
* Ensure each fetch is associated with the requesting agent ID for auditing.

## Example

```python
from skill_trend_fetcher import fetch_trends

input_data = {
    "platform": "Twitter",
    "category": "technology",
    "limit": 5
}

trends = fetch_trends(input_data)
print(trends)
```


