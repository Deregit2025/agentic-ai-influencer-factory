"""
Agent Rules Module
------------------
This module defines project-specific rules for autonomous agents within
the "Agentic AI" prototype (Project Chimera). 

Purpose:
- Enforce spec-first development
- Maintain traceability from agent actions to requirements
- Define logging, forbidden actions, and allowed resource usage

References:
- Specs: ../specs/_meta.md
- Technical Docs: ../specs/technical.md
- Security: ../specs/security.md
"""

from typing import List, Dict
import logging

# Configure agent logging
logging.basicConfig(
    filename="logs/agent_actions.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------------------
# Agent Forbidden Actions
# ---------------------------
FORBIDDEN_ACTIONS = [
    "delete_system_files",
    "access_external_network",
    "exfiltrate_secrets",
]

# ---------------------------
# Resource Limits
# ---------------------------
RESOURCE_LIMITS = {
    "cpu_percent": 50,
    "memory_mb": 512,
    "max_execution_seconds": 30
}

# ---------------------------
# Spec-First Rules
# ---------------------------
SPEC_RULES = {
    "enforce_spec_first": True,
    "spec_files": ["../specs/_meta.md", "../specs/functional.md", "../specs/technical.md"]
}

# ---------------------------
# Action Logging & Validation
# ---------------------------
def log_agent_action(agent_name: str, action: str, status: str, notes: str = ""):
    """
    Logs agent actions with status and optional notes.
    """
    if action in FORBIDDEN_ACTIONS:
        status = "FORBIDDEN"
        notes += " | Attempted forbidden action."
    logging.info(f"Agent: {agent_name} | Action: {action} | Status: {status} | Notes: {notes}")


def validate_action(action: str) -> bool:
    """
    Returns True if the action is allowed, False if forbidden.
    """
    if action in FORBIDDEN_ACTIONS:
        logging.warning(f"Forbidden action attempted: {action}")
        return False
    return True

# ---------------------------
# Example Agent Usage
# ---------------------------
if __name__ == "__main__":
    # Sample usage
    log_agent_action("agent_001", "access_database", "SUCCESS")
    log_agent_action("agent_001", "delete_system_files", "FAILED")
