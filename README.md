# SQL Generation Agent

[![CI](https://github.com/kogunlowo123/sql-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/sql-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Natural language to SQL agent that translates business questions into optimized SQL queries, validates against schema, explains query plans, and supports dialect-specific generation for Postgres, BigQuery, Snowflake, and Redshift.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_sql` | Generate SQL from a natural language question using schema context |
| `validate_query` | Validate SQL syntax and schema references before execution |
| `explain_query` | Generate human-readable explanation of a SQL query and its plan |
| `optimize_query` | Suggest optimizations for a slow SQL query |
| `translate_dialect` | Translate SQL between dialects (e.g., Postgres to BigQuery) |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/sql/generate` | Generate SQL from natural language |
| `POST` | `/api/v1/sql/validate` | Validate SQL query |
| `POST` | `/api/v1/sql/explain` | Explain SQL query |
| `POST` | `/api/v1/sql/optimize` | Optimize SQL query |
| `POST` | `/api/v1/sql/translate` | Translate SQL dialect |

## Features

- Nl To Sql
- Query Optimization
- Schema Validation
- Dialect Support
- Query Explanation

## Integrations

- Postgresql
- Bigquery
- Snowflake
- Redshift
- Databricks

## Architecture

```
sql-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── sql_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Database Engines + Schema Catalog + LLM**

---

Built as part of the Enterprise AI Agent Platform.
