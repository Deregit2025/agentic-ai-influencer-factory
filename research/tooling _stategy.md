
# Project Chimera: Tooling & MCP Strategy
# =========================================
# Author: [Your Name]
# Date: [Today’s Date]
# Purpose: Document the tools, MCP servers, and agent runtime skills strategy for Project Chimera.

## 1. Developer Tools (MCP Servers)
These tools help developers and co-pilot AI agents maintain professional standards, traceability, and governance.

| Tool Name          | Type             | Purpose / Use Case                                           | Notes / Configuration                                         |
|-------------------|-----------------|--------------------------------------------------------------|----------------------------------------------------------------|
| git-mcp           | Version Control  | Tracks all code and spec changes, enforces commit hygiene.  | Connects to Tenx MCP Sense for commit telemetry.             |
| filesystem-mcp    | File Operations  | Allows safe read/write access to project files.             | Ensures traceability for all file modifications.             |
| docker-mcp        | Build & Runtime  | Builds and runs containerized environment for testing.     | Ensures reproducible environment for CI/CD.                  |
| telemetry-mcp     | Logging/Telemetry| Streams agent actions, skill calls, and test outcomes.      | Essential for MCP Sense "Black Box" trace recording.         |
| spec-check-mcp    | Spec Verification| Checks that any proposed code aligns with `specs/`.        | Optional but recommended to reduce hallucinations.           |

### Rules & Dos / Don’ts for MCP Tools
**Dos:**  
- Always use git-mcp for commits, branch management, and merges.  
- Use filesystem-mcp for any script or skill file operations.  
- Ensure docker-mcp is used for all builds and tests before CI/CD pushes.  
- Log all agent actions via telemetry-mcp.  

**Don’ts:**  
- Do NOT bypass spec-check-mcp when proposing new features.  
- Never manually edit MCP telemetry logs.  
- Avoid running tests outside the Docker environment to prevent "works on my machine" issues.

---

## 2. Agent Skills (Runtime)
These Skills are runtime capabilities that Chimera agents will call to perform autonomous tasks. All Skills must have well-defined **Input/Output contracts**.

### 2.1 Skill: `skill_trend_fetcher`
**Purpose:** Fetch trending topics from social platforms or other trend sources.  
**Input:**  
```json
{
  "platform": "string",   // e.g., "Twitter", "TikTok", "YouTube"
  "category": "string",   // e.g., "technology", "finance"
  "limit": "integer"      // number of trends to fetch
}
````

**Output:**

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

**Notes:**

* Must validate the platform input.
* Results stored in the database via technical spec schema.

### 2.2 Skill: `skill_content_generator`

**Purpose:** Generate multimedia content (text, image, video) based on trends.
**Input:**

```json
{
  "trend": "string",
  "content_type": "string",   // "text", "image", "video"
  "tone": "string"            // "informative", "funny", "formal"
}
```

**Output:**

```json
{
  "content_id": "UUID",
  "content_url": "string",
  "metadata": {
    "length": "integer",
    "format": "string"
  }
}
```

**Notes:**

* Output must comply with OpenClaw integration specs if content is for publishing.
* Include traceable logs for all generated content.

### 2.3 Skill: `skill_publisher_content`

**Purpose:** Publish generated content to social networks or OpenClaw-enabled agent networks.
**Input:**

```json
{
  "content_id": "UUID",
  "platform": "string",
  "schedule_time": "ISO8601 datetime (optional)"
}
```

**Output:**

```json
{
  "status": "string",  // e.g., "success", "failed"
  "message": "string"  // detailed reason if failed
}
```

**Notes:**

* Must verify OpenClaw or platform availability before publishing.
* Logs must include timestamps, agent ID, and content references.

---

## 3. Recommended Workflow

1. Agent reads specs in `specs/`.
2. Calls appropriate Skill from `skills/` folder.
3. Uses MCP tools for logging, telemetry, and environment safety.
4. All results stored in the database and optionally pushed to OpenClaw network.
5. Human-in-the-loop approves or reviews content for safety-critical steps.

---

## 4. Rubric Alignment

| Rubric Dimension | Alignment Explanation                                     |
| ---------------- | --------------------------------------------------------- |
| Tooling & Skills | Clear separation between Developer MCPs & Runtime Skills. |
| Spec Fidelity    | Skills and MCP tools strictly reference specs.            |
| Testing Strategy | Skills designed for TDD: tests validate input/output.     |
| CI/CD            | Skills run in Docker with telemetry and automated tests.  |




