# ADR 001: Database Selection

## Status
Proposed / Accepted

## Context
Project Chimera requires a backend database to support storage and retrieval of:
- Trend data fetched by the agent
- Generated content metadata
- User approval and safety-layer logs
- Audit and telemetry information

Requirements include:
- High-velocity ingestion
- Versioned storage
- Easy query and transformation for analytics
- Integration with autonomous agents that can read/write via API contracts

## Decision
We have chosen **MongoDB** for this project because:
- It supports flexible, schema-less storage suitable for evolving AI-generated content.
- Built-in replication, backup, and indexing for high availability.
- Compatibility with Python (via `pymongo`) and Node.js for potential microservices.
- Easy integration with agent runtime for ingest, transform, and query operations.

Alternatives considered:
1. **PostgreSQL** – strong relational integrity, but slower schema evolution for rapidly changing content.
2. **SQLite** – lightweight and simple, but not suitable for concurrent agent workloads.
3. **Redis** – fast in-memory caching, but not designed for durable long-term storage.

## Non-Goals
- This ADR does not define:
  - Exact schema design for all collections (handled in separate data spec)
  - Detailed backup schedule (handled in DB management spec)
  - Agent-specific ingestion scripts (defined in agent rules and data spec)

## Consequences
- Agents will rely on a MongoDB instance (local or containerized) for persistent storage.
- Schema evolution and migration must be tracked and versioned.
- Backup and restore strategies must be implemented per DB spec.
