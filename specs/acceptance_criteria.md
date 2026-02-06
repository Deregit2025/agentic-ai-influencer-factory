
* Use **Gherkin syntax** (Given/When/Then)
* Map each criterion to **agent skills / backend APIs**
* Include any relevant **quantitative or performance thresholds**

Here’s a template you can paste into your file:

```markdown
# Project Chimera: Acceptance Criteria

## 1. Trend Fetching

**Feature:** Fetch trending topics

**Scenario:** Agent successfully fetches trending topics from API
```

Given the agent is active
When it executes `skill_trend_fetcher.fetch_trends()`
Then it should return at least 5 trending topics
And each topic must be validated against the API contract

```

**Scenario:** Handling API errors
```

Given the trend API is unavailable
When the agent executes `skill_trend_fetcher.fetch_trends()`
Then it should log an error to MCP
And retry after 30 seconds

```

---

## 2. Content Generation

**Feature:** Generate social media content

**Scenario:** Agent generates content for a trending topic
```

Given a list of trending topics
When the agent executes `skill_content_generator.generate()`
Then content must be generated in the required format
And include a reference to the topic and spec section

```

**Scenario:** Handling invalid input
```

Given a trending topic with invalid characters
When the agent executes `skill_content_generator.generate()`
Then it should sanitize the input
And log the action in MCP

```

---

## 3. Content Approval & Publishing

**Feature:** Human-in-the-loop content approval

**Scenario:** Human approves content
```

Given content is pending approval
When a human clicks "Approve"
Then `skill_publisher_content.publish()` is executed
And content is posted to the target channel

```

**Scenario:** Human rejects content
```

Given content is pending approval
When a human clicks "Reject"
Then content is logged as rejected
And agent updates status in MCP

```

---

## 4. Agent Monitoring

**Feature:** Track agent activity

**Scenario:** Agent logs actions
```

Given the agent is running
When it performs a task
Then each action is logged with timestamp and spec reference
And human reviewers can view it in Agent Activity Screen

```

---

## Notes:
- Every acceptance criterion is **linked to an agent skill / backend API**.  
- Quantitative thresholds:
  - Trend fetch: minimum 5 topics per fetch  
  - Retry on failure: 30 seconds  
- All logs and actions are **auditable via MCP server**.
