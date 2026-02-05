
# Project Chimera: Autonomous AI Influencer Factory

![Project Chimera](https://img.shields.io/badge/status-in-progress-yellow)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Core Philosophies](#core-philosophies)
3. [Repository Structure](#repository-structure)
4. [Getting Started](#getting-started)
5. [Spec-Driven Development](#spec-driven-development)
6. [Agent Skills](#agent-skills)
7. [Tooling & MCP Servers](#tooling--mcp-servers)
8. [Testing Strategy](#testing-strategy)
9. [Containerization & CI/CD](#containerization--cicd)
10. [OpenClaw Integration](#openclaw-integration)
11. [Contribution Guidelines](#contribution-guidelines)
12. [License](#license)

---

## Project Overview
**Project Chimera** is a robust platform for building **Autonomous AI Influencers**—agents that can research trends, generate content, and manage engagement without human intervention.  
This repository is designed with **spec-driven development (SDD)** in mind, ensuring clarity, traceability, and safe agentic automation.

**Goals:**
- Translate business objectives into **executable intent**.
- Equip AI agents with **reusable Skills**.
- Ensure reliable infrastructure with **CI/CD, testing, and governance**.

---

## Core Philosophies
- **Spec-Driven Development (SDD):** Specs are the source of truth. No agent generates code without consulting them.
- **Traceability (MCP):** Every action is monitored via the Tenx MCP Sense server.
- **Agentic Skills vs Tools:** Distinguish reusable skills (runtime) from developer tools (MCP servers).
- **Commit Hygiene:** Commit early and often; commit history tells the story of evolving complexity.

---

## Repository Structure

```text
project-chimera/
│
├── specs/
│   ├── _meta.md
│   ├── functional.md
│   ├── technical.md
│   └── openclaw_integration.md
│
├── skills/
│   ├── skill_trend_fetcher/
│   │   └── README.md
│   ├── skill_content_generator/
│   │   └── README.md
│   └── skill_publisher_content/
│       └── README.md
│
├── tests/
│   ├── test_trend_fetcher.py
│   └── test_skills_interface.py
│
├── research/
│   └── tooling_strategy.md
│
├── .cursor/
│   └── rules
│
├── Dockerfile
├── Makefile
└── .github/
    └── workflows/main.yml
````

---

## Getting Started

### Prerequisites

* Python 3.11+
* `uv` environment manager
* GitHub Account & Tenx MCP access
* Docker & Make

### Setup

```bash
# Clone repository
git clone https://github.com/<your-org>/project-chimera.git
cd project-chimera

# Setup Python environment
uv sync
uv install

# Confirm MCP Sense connection
mcp:list server
```

---

## Spec-Driven Development

All development begins with **Specs**:

* `_meta.md`: Project vision, scope, and constraints.
* `functional.md`: User stories defining agent behavior.
* `technical.md`: API contracts, database ERD, and system architecture.
* `openclaw_integration.md`: OpenClaw network communication plan.

**Do:**

* Always read specs before implementing code.
* Keep specs up-to-date with design changes.

**Don’t:**

* Implement features without consulting specs.
* Rely on ad-hoc prompt-based agent behavior.

---

## Agent Skills

Agent capabilities are modularized in the `skills/` directory:

1. **skill_trend_fetcher** – Fetches trending topics from social platforms.
   **Input:** platform, category, timeframe
   **Output:** JSON list of trending topics

2. **skill_content_generator** – Generates content based on trends.
   **Input:** trend data, content type
   **Output:** Draft content (text/video)

3. **skill_publisher_content** – Publishes generated content to social channels.
   **Input:** content object, platform credentials
   **Output:** Publish status, post ID

Skills are defined via **Input/Output contracts** and **README.md** files.
Implementation is deferred until after failing tests are in place (TDD approach).

---

## Tooling & MCP Servers

* **Developer Tools (MCP):** `git-mcp`, `filesystem-mcp`, `tenxfeedbackanalytics`
* **Runtime Agent Skills:** `skill_trend_fetcher`, `skill_content_generator`, `skill_publisher_content`

**Rules for Agents:**

* Project context, prime directives, and traceability are enforced via `.cursor/rules`.

---

## Testing Strategy

* **Test-Driven Development (TDD)** is mandatory.
* Failing tests define “empty slots” for agents:

  * `test_trend_fetcher.py`
  * `test_skills_interface.py`

**Do:**

* Write tests before implementing code.
* Cover API input/output contracts and skill interfaces.

---

## Containerization & CI/CD

* **Dockerfile** encapsulates the environment.
* **Makefile** standardizes commands:

```bash
make setup       # Install dependencies
make test        # Run all tests in Docker
make spec-check  # Optional: Validate code aligns with specs
```

* **GitHub Actions** workflow runs tests on every push.
* **AI Review Policy:** `.coderabbit.yaml` ensures spec alignment and security checks.

---

## OpenClaw Integration

Project Chimera agents communicate their **status and availability** to the OpenClaw network via `openclaw_integration.md`.
This allows other agents to coordinate, query, and engage autonomously.

---

## Contribution Guidelines

* Follow **SDD**: always read and update specs.
* Use clear commit messages:

  * `chore(rules): ...`
  * `docs(skill): ...`
* Commit at least **2x/day**.
* Ensure MCP Sense telemetry is active for all changes.

---

## License

[MIT License](LICENSE)

---

*Project Chimera is part of a forward-deployed engineering initiative. Unauthorized use or modification is prohibited outside official channels.*


