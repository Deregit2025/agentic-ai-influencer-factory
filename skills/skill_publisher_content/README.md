
# Skill: Content Publisher (`skill_publisher_content`)

## Purpose
The Content Publisher skill enables Chimera agents to autonomously post content to social media platforms or internal channels. It ensures that generated content from `skill_content_generator` is correctly formatted, approved (if needed), and successfully published while logging all actions for traceability and compliance.

## Input
```json
{
  "content_items": [
    {
      "text": "string",
      "media_references": ["string"],
      "platform_optimized": "boolean"
    }
  ],
  "platform": "string",      // e.g., "Twitter", "TikTok", "YouTube"
  "schedule_time": "string", // ISO8601 datetime, optional: schedule future posts
  "approval_required": "boolean" // If True, request human approval before publishing
}
````

## Output

```json
{
  "published_items": [
    {
      "content_id": "string",
      "platform": "string",
      "status": "string",   // e.g., "published", "scheduled", "rejected"
      "timestamp": "ISO8601 datetime"
    }
  ]
}
```

## Usage Notes

* Validate platform credentials and API tokens before publishing.
* Ensure media references exist and are accessible.
* If `approval_required` is True, integrate with Human-in-the-Loop layer for approval before publishing.
* Log publishing results and failures to `telemetry-mcp` for auditing.

## MCP & Traceability

* Track all published content with timestamps, agent ID, and content ID.
* Capture API responses and errors for each publishing attempt.
* Maintain history of scheduled vs. immediate posts for reporting and analytics.

## Example

```python
from skill_publisher_content import publish_content

content_items = [
    {
        "text": "Breaking: AI just passed Turing Test! 🤖",
        "media_references": ["https://example.com/media/ai.jpg"],
        "platform_optimized": True
    }
]

input_data = {
    "content_items": content_items,
    "platform": "Twitter",
    "schedule_time": "2026-02-05T15:00:00Z",
    "approval_required": True
}

published = publish_content(input_data)
print(published)
```




