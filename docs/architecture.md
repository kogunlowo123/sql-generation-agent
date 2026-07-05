# SQL Generation Agent Architecture

Natural language to SQL agent that translates business questions into optimized SQL queries, validates against schema, explains query plans, and supports dialect-specific generation for Postgres, BigQuery, Snowflake, and Redshift.

## Domain Tools

- **generate_sql**: Generate SQL from a natural language question using schema context
- **validate_query**: Validate SQL syntax and schema references before execution
- **explain_query**: Generate human-readable explanation of a SQL query and its plan
- **optimize_query**: Suggest optimizations for a slow SQL query
- **translate_dialect**: Translate SQL between dialects (e.g., Postgres to BigQuery)