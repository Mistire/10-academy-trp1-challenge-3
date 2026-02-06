# Technical Plan: Project Chimera Foundation

**Status**: Draft  
**Reference**: [functional.md](functional.md)

## 1. System Architecture
Project Chimera uses a **Hierarchical Swarm Architecture** to decouple strategy from execution.

### Swarm Role Assignments
- **Orchestrator (Human Super-Orchestrator)**: Strategic lead, HITL moderator.
- **Planner (Gemini 1.5 Pro)**: High-context model for goal decomposition and DAG generation.
- **Worker (Gemini 1.5 Flash)**: Low-latency model for atomic tool execution (MCP).
- **Judge (Gemini 1.5 Pro + Vision)**: Governor model for persona validation, safety, and P&L (CFO).

### MCP Tool: `generate_multimodal`
- **Input**: `{ "prompt": "string", "media_type": "string", "persona_id": "string", "motion_intensity": int }`
- **Output**: `{ "asset_url": "string", "confidence_score": float, "verification_status": "string" }`

### MCP Tool: `monitor_finance` (Wrapper for AgentKit)
- **Input**: `{ "action": "string", "target_amount_usdc": float }`
- **Output**: `{ "balance_usdc": float, "allow_transaction": bool, "reasoning": "string" }`

### MCP Tool: `get_balance` (Coinbase AgentKit)
- **Input**: `{ "agent_id": "string", "network": "base" }`
- **Output**: `{ "address": "0x...", "usdc_balance": float, "eth_balance": float }`

### MCP Tool: `send_payment` (Coinbase AgentKit)
- **Input**: `{ "to_address": "0x...", "amount_usdc": float, "memo": "string" }`
- **Output**: `{ "transaction_hash": "0x...", "status": "confirmed" }`

## 3. Orchestration & State Machine
The system utilizes **Redis** for the task queue and **Weaviate** for semantic memory.

1. **Ingestion**: Goal enters via Dashboard (UI 1.1).
2. **Decomposition**: Planner emits a JSON DAG of tasks.
3. **Budget Gate**: CFO Judge runs `get_balance` and locks required funds.
4. **Parallel Execution**: Workers pick up independent branches of the DAG.
5. **Quality Gate**: Judge validates outputs against SOUL.md.
6. **HITL Tiering**:
    - Confidence > 0.9: Publish immediately.
    - 0.7 - 0.9: Pause DAG, request human approval.
    - < 0.7: Reject, signal Planner to retry with "Retry Context."

## 4. Multi-Tiered Memory
- **Episodic**: Last 50 turns stored in Redis `agent:[id]:episodic`.
- **Semantic**: All turns archived in Weaviate. Context assembler retrieves 5 most relevant memories for every Planner call.

## 5. Non-Custodial Wallet Strategy
- **Provider**: Coinbase AgentKit (CdpEvmWalletProvider).
- **Security**: Private keys retrieved from `os.environ` (AWS Secrets Manager integration in Production).
- **Governance**: Every `send_payment` call MUST be wrapped in a `@budget_check` decorator.
