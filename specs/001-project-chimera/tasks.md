# Task List: Project Chimera Foundation

**Status**: Draft  
**Reference**: [technical.md](technical.md)

## Phase 1: Swarm Infrastructure (The "Skeleton")
- [ ] **T-1.0**: Initialize Python project structure (`planner/`, `worker/`, `judge/`).
- [ ] **T-1.1**: Define Pydantic models for `Task`, `Result`, and `DAG`.
- [ ] **T-1.2**: Implement Redis-based task queue using standard `ConnectionPool`.
- [ ] **T-1.3**: Bootstrap empty `tests/test_swarm.py` for TDD validation.

## Phase 2: MCP Integration (The "Nervous System")
- [ ] **T-2.0**: Implement `MCPClient` with Stdio transport.
- [ ] **T-2.1**: Implement `fetch_trends` tool handler.
- [ ] **T-2.2**: Integrate `Tenx MCP Sense` logger into all tool handshakes.
- [ ] **T-2.3**: Establish Context Assembler (Redis episodic + Weaviate semantic).

## Phase 3: Agentic Commerce (The "Fuel")
- [ ] **T-3.0**: Configure `CdpEvmWalletProvider` via environment variables.
- [ ] **T-3.1**: Implement `@budget_check` decorator for transaction safety.
- [ ] **T-3.2**: Implement `get_balance` and `send_payment` tools.

## Phase 4: Quality & Governance (The "Brain")
- [ ] **T-4.0**: Implement confidence-based HITL escalation logic (Judge node).
- [ ] **T-4.1**: Implement "Honesty Directive" in base reasoning prompt.
- [ ] **T-4.2**: Verify full project compliance via `specify check`.
