
# Project Chimera: Frontend Design (Minimal)

## 1. Overview
Although the full UI implementation is out of scope for Task 1, this document defines the minimal frontend screens, user flows, and component hierarchy required for future integration with backend APIs and agent skills.

The goal is to provide clear guidance for developers or designers who may implement a UI in later phases.

---

## 2. Screens

### 2.1 Dashboard
- Purpose: Central hub for monitoring agent activity and content status.
- Key Elements:
  - Summary of trending topics fetched (`skill_trend_fetcher`)
  - Recent generated content (`skill_content_generator`)
  - Content approval queue for human oversight (`skill_publisher_content`)
  - System logs / agent actions

### 2.2 Content Approval Screen
- Purpose: Allow human reviewers to approve, reject, or edit content.
- Key Elements:
  - List of pending content items
  - Preview of generated content
  - Approval / Reject buttons
  - Optional comments field
- Linked Backend API: `skills.skill_publisher_content.publish()`

### 2.3 Agent Activity Screen
- Purpose: Monitor agent runtime behavior and logs.
- Key Elements:
  - Agent status (Idle, Running, Error)
  - Actions executed with timestamp
  - Spec references for each action
- Linked Backend API: `skills.skill_trend_fetcher.fetch_trends()`, `skills.skill_content_generator.generate()`

---

## 3. User Flows

### 3.1 Generating Content
1. User logs into Dashboard.
2. Agent fetches trending topics.
3. Agent generates content automatically.
4. Content is sent to Content Approval Screen if human-in-the-loop is required.
5. User approves or edits content.
6. Approved content is published via the publisher skill.

### 3.2 Monitoring Agent
1. User opens Agent Activity Screen.
2. Agent logs are displayed in real-time.
3. Users can click on an action to see spec references and reasoning.

---

## 4. Component Hierarchy

```

Dashboard
│
├─ TrendingTopicsWidget
│
├─ GeneratedContentList
│
├─ ApprovalQueueWidget
│
└─ AgentActivityPanel
├─ ActionLog
└─ SpecReferenceViewer

```

---

## 5. API Mappings

| UI Component             | Backend Skill / API                 | Notes |
|--------------------------|------------------------------------|-------|
| TrendingTopicsWidget      | `skill_trend_fetcher.fetch_trends()` | Fetches and displays trending topics |
| GeneratedContentList      | `skill_content_generator.generate()` | Displays AI-generated content |
| ApprovalQueueWidget       | `skill_publisher_content.publish()` | Handles human approval flow |
| AgentActivityPanel        | Logging endpoints in MCP          | Shows real-time agent actions |

---

## 6. Notes
- This frontend is minimal and mostly for visualization and human-in-the-loop interaction.
- Screens are placeholders and will be expanded in future phases.
- All components assume backend APIs and agent skills are operational.
```

