# Database & Data Management Specifications

**Project:** Project Chimera  
**Purpose:** Define the complete lifecycle for data ingestion, transformation, storage, and archival so autonomous agents can implement DB operations safely and consistently.  

---

## 1. Overview

Project Chimera relies on structured and unstructured data for trend analysis, content generation, and publishing workflows. To ensure full reproducibility, traceability, and agent autonomy, all database operations must follow the specifications below.

**Goals:**
- Maintain integrity and consistency of data.
- Enable autonomous agents to ingest, transform, and store data.
- Ensure robust backup, archival, and retention strategies.
- Support high-velocity metadata processing and versioning.

---

## 2. Lifecycle Stages

### 2.1 Data Ingestion
- **Sources:** APIs (social media trends), CSV/JSON uploads, scraped web content.
- **Validation:** Check schema compliance, type validation, and required fields.
- **Error Handling:** Log invalid entries to MCP with error code and reason.
- **Location:** Raw data stored in `/data/raw/` with timestamped filenames.
- **Agent Skill Mapping:** `skill_data_ingest`

**Example Ingestion Flow:**
1. Fetch source data.
2. Validate against schema defined in `schemas/`.
3. Store validated data in `/data/raw/`.
4. Log ingestion metrics.

---

### 2.2 Data Transformation
- **Operations:** Cleaning, normalization, feature extraction, enrichment.
- **Tools:** Pandas, Numpy, custom scripts.
- **Output:** Transformed datasets stored in `/data/processed/`.
- **Agent Skill Mapping:** `skill_data_transform`

**Transformation Steps:**
1. Load raw data.
2. Apply cleaning and normalization.
3. Feature engineering or content preparation.
4. Validate transformed dataset.
5. Store in `/data/processed/` with versioning.

---

### 2.3 Storage
- **Database:** MongoDB (primary), optionally SQLite for local testing.
- **Collections/Tables:** Trends, Content, Metadata, Agent Logs.
- **Schema Migration:** Maintain versioned JSON/YAML schemas in `schemas/`.
- **Agent Skill Mapping:** `skill_db_store`

**Storage Rules:**
- Every insert/update must include timestamp and source reference.
- Use unique IDs for deduplication.
- Enforce referential integrity where applicable.

---

### 2.4 Backup & Restore
- **Backup Frequency:** Daily full backup, hourly incremental for high-velocity datasets.
- **Storage:** `/backups/` or cloud storage (S3, GCP bucket) if configured.
- **Restore:** Scripted restore flow for full or partial datasets.
- **Agent Skill Mapping:** `skill_db_backup`

**Backup Steps:**
1. Dump database or collection to backup folder.
2. Compress and version by timestamp.
3. Verify checksum.
4. Log backup operation.

---

### 2.5 Archival & Retention
- **Retention Policy:** Keep processed datasets for 1 year, raw datasets for 6 months.
- **Archival Format:** Compressed CSV/JSON with metadata.
- **Deletion:** Soft delete first, permanent deletion after retention period.
- **Agent Skill Mapping:** `skill_data_archive`

**Archival Steps:**
1. Identify data exceeding retention period.
2. Move to `/archive/` folder with timestamp.
3. Log archival metadata.

---

### 2.6 Querying & Access
- **Access Rules:** Read-only for agents unless explicitly allowed for transformations or migrations.
- **Latency & Performance:** Queries must complete within 5s for datasets <10k records.
- **Agent Skill Mapping:** `skill_data_query`

---

### 2.7 High-Velocity Metadata
- **Handling:** Batch updates every 5 minutes, indexed for search.
- **Versioning:** Include version ID, timestamp, and source reference.
- **Agent Skill Mapping:** `skill_metadata_manager`

---

### 3. Scripts & Automation
- `scripts/db_ingest.py` → ingestion pipeline  
- `scripts/db_transform.py` → transformation pipeline  
- `scripts/db_store.py` → database insertion  
- `scripts/db_backup.py` → backup & restore  
- `scripts/db_archive.py` → archival & retention  

> Agents should call these scripts following the rules in `.cursor/rules` and log all actions to MCP.

---

### 4. Governance & Traceability
- Every DB operation must log:
  - Action type (ingest, transform, store, backup, archive)
  - Timestamp
  - Agent responsible
  - Source dataset or script
- All logs must be sent to MCP for auditing.

---

### 5. References
- `schemas/` → JSON/YAML schemas for validation  
- `.cursor/rules` → agent behavior and skill mapping  
- `specs/security.md` → access control and secrets management  
- `Makefile` → automation of scripts execution  

---

**End of DB Management Specifications**
