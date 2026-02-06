# Project Chimera Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
The specification is the "Golden" source of truth. No code exists without a corresponding spec ratified in the `specs/` directory. Ambiguity is treated as a bug. We use the GitHub Spec Kit framework for all lifecycle management.

### II. Traceability & Observability (MCP)
Every internal "thought," architectural decision, and external "handshake" must be captured/logged via **Tenx MCP Sense**. The system must remain audit-ready and observable at all times.

### III. Fractal Orchestration (FastRender Swarm)
We utilize a Hierarchical Swarm pattern (Planner -> Worker -> Judge). Operation is "Fractal"—a single human Super-Orchestrator directs AI Managers who supervise specialized Worker swarms. This enables "Management by Exception."

### IV. Agentic Commerce & Economic Agency
Agents are persistent, goal-directed digital entities with non-custodial wallets (Coinbase AgentKit). They MUST manage their own P&L and seek approval from the "CFO Judge" for all on-chain transactions.

### V. Self-Healing & Management by Exception
Workflows must include automated triage to detect and resolve operational errors (API timeouts, 404s). Escalation to the human occurs ONLY when automated recovery fails or risk exceeds the HITL threshold.

### VI. Tiered Memory & Context Assembly
Agents utilize a multi-tiered memory architecture:
- **Short-Term (Episodic)**: High-speed Redis cache.
- **Long-Term (Semantic)**: Weaviate vector database.
The system MUST assemble context strictly from these buffers before reasoning.

### VII. Honesty & AI Disclosure
Agents must prioritize a "Honesty Directive" to provide truthful, unambiguous disclosure if questioned about their AI nature.
- **FR-004**: The system MUST implement an "Honesty Directive" overriding persona for AI disclosure (e.g., "I am a virtual persona synthesized by Project Chimera.").

## Governance & Safety Tiers
- **CFO Judge**: Mandatory quality gate for all cost-incurring tasks. Enforces daily spend limits.
- **HITL Verification**: 
    - Confidence > 0.9: Auto-Approve.
    - 0.7 < Confidence < 0.9: Async Human Review.
    - Confidence < 0.7: Auto-Reject/Retry.
- **Sensitive Topics**: Politics, Health, and Finance ALWAYS require HITL approval.

## Development Workflow
1. **Specify**: Define functional intent in `specs/[FEATURE]/functional.md`.
2. **Plan**: Define technical implementation in `specs/[FEATURE]/technical.md`.
3. **Tasks**: Break down into `specs/[FEATURE]/tasks.md`.
4. **Implement**: Build against the failing tests in `tests/`.

## Governance
This Constitution supersedes all other engineering practices. Amendments require a formal migration plan and ratification. Complexity in implementation must be justified against these principles.

**Version**: 1.1.0 | **Ratified**: 2026-02-06 | **Last Amended**: 2026-02-06
