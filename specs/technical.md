# Project Chimera: Technical Specification

## 1. System Architecture: FastRender Swarm
Project Chimera utilizes a hierarchical, role-based swarm architecture:

### 1.1 Swarm Roles
- **Planner Node**: Goals -> TaskQueue (Redis DAG).
- **Worker Node**: Stateless execution via MCP Tools.
- **Judge Node**: QA + Safety + Optimistic Concurrency Control (OCC).

## 2. Database Schemas

### 2.1 Relation DB (PostgreSQL) - "The Ledger"
```sql
CREATE TABLE campaigns (
    id UUID PRIMARY KEY,
    owner_id UUID NOT NULL,
    goal_text TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    budget_limit_usdc DECIMAL(12, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE agents (
    id UUID PRIMARY KEY,
    campaign_id UUID REFERENCES campaigns(id),
    persona_id VARCHAR(50) UNIQUE, -- Links to SOUL.md
    wallet_address TEXT UNIQUE,
    current_state VARCHAR(20) DEFAULT 'idle',
    last_heartbeat TIMESTAMP
);

CREATE TABLE audit_logs (
    id BIGSERIAL PRIMARY KEY,
    agent_id UUID REFERENCES agents(id),
    action_type VARCHAR(50), -- 'post', 'transaction', 'handshake'
    status VARCHAR(20),
    confidence_score FLOAT,
    payload JSONB,
    trace_id TEXT -- MCP Sense Correlation ID
);
```

### 2.2 Video & Media Metadata (NoSQL/JSONB) - "The Asset Ledger"
Designed for high-velocity ingestion of multimodal assets.
```sql
CREATE TABLE media_assets (
    id UUID PRIMARY KEY,
    agent_id UUID REFERENCES agents(id),
    task_id UUID, -- Links to the generation task
    media_type VARCHAR(10), -- 'image', 'video'
    s3_url TEXT NOT NULL,
    metadata JSONB, -- Stores technical props: duration, bitrate, style_idx, seed
    engagement_stats JSONB DEFAULT '{}', -- view_count, likes, shares
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2.3 Vector DB (Weaviate) - "Semantic Memory"
- **Class**: `AgentMemory`
- **Properties**:
    - `content` (text): The raw memory/interaction.
    - `agent_id` (string/uuid): Owner filter.
    - `timestamp` (date): Temporal context.
    - `importance` (float): Relevance score for high-level retrieval.

## 3. API & Tool Contracts

### 3.1 Agent-to-Agent Communication (OpenClaw)
For inter-agent negotiation or capability discovery.
```json
{
  "sender_id": "agent-alpha",
  "receiver_id": "agent-sigma",
  "protocol_version": "1.0",
  "message_type": "request_collab | fetch_status | broadcast_availability",
  "payload": {
    "status": "ready",
    "open_mcp_ports": ["trends_01", "finance_01"],
    "current_mission": "lifestyle_branding_v2"
  }
}
```

### 3.2 Agent Task Contract (Redis Payload)
```json
{
  "task_id": "uuid-v4",
  "task_type": "generate_content | fetch_trends | execute_transaction",
  "status": "pending | review | complete",
  "priority": 1,
  "config": {
    "platform": "twitter",
    "budget_cap": 5.0
  },
  "context_refs": {
    "soul_id": "persona-chimera-alpha",
    "memory_indices": ["mem_001", "mem_102"]
  }
}
```

### 3.2 MCP Tool Contract: Social Post
```json
{
  "name": "publish_media",
  "input_schema": {
    "type": "object",
    "properties": {
      "platform": { "enum": ["twitter", "instagram"] },
      "caption": { "type": "string", "minLength": 1 },
      "media_urls": { "type": "array", "items": { "type": "string" } },
      "ai_label": { "type": "boolean", "default": true }
    },
    "required": ["platform", "caption"]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "post_id": { "type": "string" },
      "status": { "const": "success" }
    }
  }
}
```

### 3.3 MCP Tool Contract: Financial Transfer
```json
{
  "name": "cdp_native_transfer",
  "input_schema": {
    "type": "object",
    "properties": {
      "to_address": { "type": "string", "pattern": "^0x[a-fA-F0-9]{40}$" },
      "amount": { "type": "number", "minimum": 0.01 },
      "asset_id": { "type": "string", "default": "usdc" }
    },
    "required": ["to_address", "amount"]
  }
}
```

## 4. Safety & Governance
- **Confidence Tiers**: >0.9 (Auto), 0.7-0.9 (Async HITL), <0.7 (Retry).
- **OCC Logic**: Before commit, check `UPDATE agents SET state_version = state_version + 1 WHERE id = ? AND state_version = ?`.
