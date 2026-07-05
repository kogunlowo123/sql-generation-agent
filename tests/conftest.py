"""Test configuration for SQL Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "sql-generation-agent", "category": "Data Engineering"}
