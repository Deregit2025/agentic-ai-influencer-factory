
# ===================================================
# Project Chimera: Tooling & MCP Strategy
# File: research/tooling_strategy.md
# Purpose: Document all developer tools (MCP servers) and runtime agent skills
# ===================================================

# ------------------------
# Overview
# ------------------------
Project Chimera requires a clear separation between developer tooling (MCP servers) and agent runtime capabilities (Skills).  
This document outlines:

1. MCP Servers used for development, telemetry, and governance.  
2. Agent Skills that enable Chimera to perform autonomous influencer tasks.  

All tools and skills are designed to maintain **spec fidelity, traceability, and TDD alignment**.

# ------------------------
# Part A: Developer Tools (MCP Servers)
# ------------------------

| MCP Server Name           | Type | URL                                      | Enabled Tools | Enabled Prompts | Purpose                                      |
|---------------------------|------|------------------------------------------|---------------|----------------|----------------------------------------------|
| tenxfeedbackanalytics     | HTTP | https://mcppulse.10academy.org/proxy    | 3             | 1              | Telemetry, logging, analytics feedback      |

**Usage Guidelines:**  
- Only use MCP servers that are installed and running.  
- Verify server availability before executing dependent tasks.  
- All actions performed with MCP servers must be logged for traceability.  
- Do not attempt to use GitHub MCP tools since they are not installed in this environment.  

**Configuration Example (`.vscode/mcp.json`):**
```json
{
  "servers": {
    "tenxfeedbackanalytics": {
      "url": "https://mcppulse.10academy.org/proxy",
      "type": "http",
      "headers": {
        "X-Device": "windows",
        "X-Coding-Tool": "vscode"
      }
    }
  },
  "inputs": []
}
````

# ------------------------

# Part B: Agent Skills (Runtime Capabilities)

# ------------------------

Agent Skills are **reusable capability packages** that Chimera calls during runtime to achieve autonomous influencer objectives.

| Skill Name              | Purpose                                                   | Input                                   | Output                                |
| ----------------------- | --------------------------------------------------------- | --------------------------------------- | ------------------------------------- |
| skill_trend_fetcher     | Fetch trending topics from social media APIs              | `platform`, `region`, `limit`           | JSON array of trending topics         |
| skill_content_generator | Generate social media content based on trends             | `trend_data`, `tone`, `length`          | Formatted post content (text, images) |
| skill_publisher_content | Publish content to target channels with optional approval | `content`, `channel`, `approval_status` | Publication log, success/failure      |

**Skill Guidelines:**

* Each Skill must follow the **Input/Output contracts** defined in `technical.md`.
* Skills must not access MCP servers directly unless explicitly allowed.
* Logging and telemetry for each skill must be sent to `tenxfeedbackanalytics`.
* Skills must fail gracefully if specifications or input contracts are violated.

# ------------------------

# Part C: Tooling & Skills Alignment with Specs

# ------------------------

* All MCP server actions and agent skills **must reference specifications**:

  * `_meta.md` — high-level vision
  * `functional.md` — user stories
  * `technical.md` — API contracts, database schema
  * `openclaw_integration.md` — OpenClaw publishing (if applicable)

* **Traceability**: Every skill invocation should be logged to MCP with reference to the relevant spec.

* **TDD Alignment**: Skills will initially fail against the tests in `tests/` to define the "empty slot" for agents.

# ------------------------

# Summary

# ------------------------

This strategy ensures:

1. Clear separation between **development tooling** (MCP) and **runtime capabilities** (Skills).
2. Full **traceability and auditability** for agent actions.
3. Agents operate **safely, predictably, and spec-compliant**.

# ===================================================

# End of Tooling & MCP Strategy

# ===================================================

