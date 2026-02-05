import pytest
from typing import Any, Dict

# List of skills to validate
SKILLS = [
    "skill_trend_fetcher",
    "skill_content_generator",
    "skill_publisher_content"
]

# Define expected input/output schemas for each skill
EXPECTED_CONTRACTS = {
    "skill_trend_fetcher": {
        "input": {"topic": str, "region": str},
        "output": {"trends": list}  # List of trending topics
    },
    "skill_content_generator": {
        "input": {"trends": list},
        "output": {"content": str}  # Generated content string
    },
    "skill_publisher_content": {
        "input": {"content": str, "platform": str},
        "output": {"status": str, "post_id": str}  # Publishing result
    }
}

@pytest.mark.parametrize("skill", SKILLS)
def test_skill_exists(skill):
    """
    Check that each skill module exists.
    """
    module_path = f"skills.{skill}.{skill.split('_')[1]}"
    try:
        __import__(module_path)
    except ModuleNotFoundError:
        pytest.fail(f"{module_path} does not exist yet. This is expected in TDD Red stage.")

@pytest.mark.parametrize("skill", SKILLS)
def test_skill_input_output_contract(skill):
    """
    Check that each skill defines input/output according to spec.
    """
    contract = EXPECTED_CONTRACTS[skill]
    # Try importing the skill module
    module_path = f"skills.{skill}.{skill.split('_')[1]}"
    try:
        mod = __import__(module_path, fromlist=[""])
        # Check if module defines INPUT_SCHEMA and OUTPUT_SCHEMA
        assert hasattr(mod, "INPUT_SCHEMA"), f"{skill} must define INPUT_SCHEMA"
        assert hasattr(mod, "OUTPUT_SCHEMA"), f"{skill} must define OUTPUT_SCHEMA"

        # Validate schemas match expected types
        for key, typ in contract["input"].items():
            assert mod.INPUT_SCHEMA[key] == typ, f"{skill} INPUT_SCHEMA key '{key}' should be {typ}"
        for key, typ in contract["output"].items():
            assert mod.OUTPUT_SCHEMA[key] == typ, f"{skill} OUTPUT_SCHEMA key '{key}' should be {typ}"

    except ModuleNotFoundError:
        pytest.fail(f"{module_path} does not exist yet. This is expected in TDD Red stage.")
