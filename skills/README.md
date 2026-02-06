# Project Chimera: Agent Skills (Runtime)

This directory defines the modular capabilities (skills) utilized by Chimera agents during task execution. In accordance with Spec-Driven Development (SDD), these interfaces are the "Source of Truth" for agent actions.

## 1. `fetch_trends`
- **Purpose**: Ingest multimodal trend data via MCP news/social resources.
- **Input schema (JSON)**:
  ```json
  {
    "domain": "string (e.g., 'fashion', 'tech')",
    "geography": "string (ISO code)",
    "limit": "integer (max 10)"
  }
  ```
- **Output schema (JSON)**:
  ```json
  {
    "trends": [
      {
        "cluster_id": "string",
        "velocity": "float",
        "summary": "string"
      }
    ],
    "id": "uuid"
  }
  ```

## 2. `generate_multimodal`
- **Purpose**: Generates visual assets (images/videos) ensuring persona facial/style locking.
- **Input schema (JSON)**:
  ```json
  {
    "prompt": "string",
    "media_type": "enum ['image', 'video']",
    "persona_id": "string",
    "motion_intensity": "integer (0-10)"
  }
  ```
- **Output schema (JSON)**:
  ```json
  {
    "asset_url": "string (URI)",
    "confidence_score": "float",
    "verification_status": "enum ['approved', 'pending_review']"
  }
  ```

## 3. `monitor_finance`
- **Purpose**: Real-time solvency checks via Coinbase AgentKit. Mandatory gate for the CFO Judge.
- **Input schema (JSON)**:
  ```json
  {
    "action": "enum ['get_balance', 'validate_transaction']",
    "target_amount_usdc": "float (optional)"
  }
  ```
- **Output schema (JSON)**:
  ```json
  {
    "balance_usdc": "float",
    "allow_transaction": "boolean",
    "reasoning": "string"
  }
  ```
