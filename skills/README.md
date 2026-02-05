# Project Chimera: Agent Skills (Runtime)

This directory defines the modular capabilities (skills) utilized by Chimera agents during task execution.

## 1. skill_fetch_trends
- **Description**: Fetches social and news data via configured MCP resources to identify viral topics.
- **Input Contract**: `{"topic_domain": "string", "limit": "int"}`
- **Output Contract**: `{"trends": [{"tag": "string", "relevance": "float"}], "id": "uuid"}`

## 2. skill_generate_multimodal
- **Description**: Orchestrates specialized generation servers (Ideogram, Luma) to produce campaign assets.
- **Input Contract**: `{"prompt": "string", "media_type": "image|video", "persona_id": "string"}`
- **Output Contract**: `{"asset_url": "string", "confidence_score": "float"}`

## 3. skill_monitor_finance
- **Description**: Interfaces with Coinbase AgentKit to check balances and validate budget limits.
- **Input Contract**: `{"check_type": "balance|budget_cap"}`
- **Output Contract**: `{"balance_usdc": "float", "is_solvent": "bool"}`
