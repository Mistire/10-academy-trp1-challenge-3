# Feature Specification: Project Chimera Foundation

**Feature Branch**: `001-project-chimera`  
**Created**: 2026-02-06  
**Status**: Draft  
**Input**: "Build the factory that builds the autonomous influencer."

## User Scenarios & Testing

### User Story 1 - Goal-Driven Decomposition (Priority: P1)
As a Network Operator, I want to define a high-level goal in natural language (e.g., "Promote Ethiopian coffee culture to Gen Z") so that the Planner Agent can decompose it into a DAG of actionable tasks (research, creative, distribution).

**Why this priority**: Essential for Fractal Orchestration. Without goal decomposition, the system remains a sequence of manual triggers.

**Independent Test**: Provide a natural language goal and assert that a valid JSON DAG of tasks is produced by the Planner node.

**Acceptance Scenarios**:
1. **Given** a valid natural language goal, **When** processed by the Planner, **Then** a structured list of tasks with correct dependencies is generated.
2. **Given** an ambiguous goal, **When** processed by the Planner, **Then** the Agent requests clarification through the HITL queue.

---

### User Story 2 - Self-Aware Execution & Solvency (Priority: P1)
As a Chimera Agent, I need to check my financial solvency (via `get_balance`) and soul-alignment (SOUL.md) before executing any task to ensure I remain autonomous and on-persona.

**Why this priority**: Enforces "Management by Exception" and prevents "persona drift" or financial exhaustion.

**Independent Test**: Mock a task that violates SOUL.md and assert that the Judge node rejects it. Verify that a task costing 10 USDC is blocked if the wallet has < 12 USDC (including buffer).

**Acceptance Scenarios**:
1. **Given** a task that requires on-chain funds, **When** checked against the wallet, **Then** execution only proceeds if balance > cost + safety buffer. Enforced by the CFO Judge.
2. **Given** a content generation task, **When** checked against SOUL.md, **Then** the output MUST maintain voice consistency (Judge validation).

---

### User Story 3 - Traceable Handshakes via MCP (Priority: P2)
As a Lead Architect, I want every internal decision and external tool call logged via **Tenx MCP Sense** so that I can audit the agent's reasoning during the 3-day challenge.

**Why this priority**: Mandatory for the "Orchestrator" grade and long-term audibility.

**Independent Test**: Trigger a tool call (e.g., `fetch_trends`) and verify a corresponding entry exists in the MCP Sense logs.

**Acceptance Scenarios**:
1. **Given** a successful MCP tool execution, **When** checking the flight recorder, **Then** a `connection_confirmed` event is present with full input/output metadata.

## Requirements

### Functional Requirements
- **FR-001**: System MUST utilize a hierarchical swarm (Planner -> Worker -> Judge).
- **FR-002**: Agents SHALL NOT respond to inputs without passing through a Semantic Filter (Relevance > 0.75).
- **FR-003**: The Planner MUST emit a Directed Acyclic Graph (DAG) for all multi-step goals.
- **FR-004**: The system MUST implement an "Honesty Directive" overriding persona for AI disclosure (e.g., "I am a virtual persona synthesized by Project Chimera.").
- **FR-005**: All creative assets MUST include a `character_reference_id` for visual consistency.

### Non-Functional Requirements
- **NFR-001**: End-to-end response time for high-priority interactions SHALL NOT exceed 10 seconds.
- **NFR-002**: Python code MUST maintain 100% type coverage (Strict MyPy).
- **NFR-003**: Every feature MUST be backed by a failing test in `tests/` before implementation (True TDD).
- **NFR-004**: Multi-tenancy MUST ensure memory and wallet isolation between agents.

### Key Entities
- **Planner**: Role responsible for strategy and DAG generation.
- **Worker**: Role responsible for atomic execution via MCP Tools.
- **Judge**: Governor role for safety, persona, and quality gates (includes CFO Judge).
- **SOUL**: Immutable configuration defining the Agent's identity.

## Success Criteria
- **SC-001**: 100% of "Handshakes" are traceable in MCP Sense.
- **SC-002**: 90% of user-journey tasks are completed without human intervention (Fractal Orchestration).
- **SC-003**: Latency for goal-to-DAG decomposition is < 5 seconds.
