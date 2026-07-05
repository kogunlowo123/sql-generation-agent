"""SQL Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_sql():
    """Test Generate SQL from a natural language question using schema context."""
    tools = AgentTools()
    result = await tools.generate_sql(question="test", schema="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_query():
    """Test Validate SQL syntax and schema references before execution."""
    tools = AgentTools()
    result = await tools.validate_query(query="test", schema="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_explain_query():
    """Test Generate human-readable explanation of a SQL query and its plan."""
    tools = AgentTools()
    result = await tools.explain_query(query="test", dialect="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_query():
    """Test Suggest optimizations for a slow SQL query."""
    tools = AgentTools()
    result = await tools.optimize_query(query="test", execution_plan="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.sql_generation_agent_agent import SqlGenerationAgentAgent
    agent = SqlGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
