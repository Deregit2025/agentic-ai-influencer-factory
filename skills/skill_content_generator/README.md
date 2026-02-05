
# Skill: Content Generator (`skill_content_generator`)

## Purpose
The Content Generator skill allows Chimera agents to autonomously create social media posts, captions, and video scripts based on trending topics or structured inputs. This skill ensures that the agent can generate engaging content without human intervention, while respecting platform norms and brand guidelines.

## Input
```json
{
  "trend_data": [
    {
      "title": "string",
      "url": "string",
      "engagement_score": "float",
      "timestamp": "ISO8601 datetime"
    }
  ],
  "platform": "string",       // e.g., "Twitter", "TikTok", "YouTube"
  "content_type": "string",   // e.g., "post", "video_script", "caption"
  "tone": "string"            // e.g., "informative", "funny", "formal"
}
````

## Output

```json
{
  "generated_content": [
    {
      "text": "string",
      "media_references": ["string"], // URLs or local paths
      "platform_optimized": "boolean"
    }
  ]
}
```

## Usage Notes

* Validate `platform` and `content_type` to avoid unsupported requests.
* Generated content should be concise, engaging, and platform-specific.
* Each generated content item must be passed to `skill_publisher_content` for approval or publishing.
* Ensure traceability for generated content to maintain auditability and compliance.

## MCP & Traceability

* Use `telemetry-mcp` to log inputs, outputs, and any errors during content generation.
* Include timestamps and agent IDs for all content generated.
* Track content success metrics after publishing to refine future generations.

## Example

```python
from skill_content_generator import generate_content

trend_data = [
    {
        "title": "AI Breakthrough in 2026",
        "url": "https://example.com/ai-news",
        "engagement_score": 92.5,
        "timestamp": "2026-02-05T10:00:00Z"
    }
]

input_data = {
    "trend_data": trend_data,
    "platform": "Twitter",
    "content_type": "post",
    "tone": "informative"
}

content = generate_content(input_data)
print(content)
```

