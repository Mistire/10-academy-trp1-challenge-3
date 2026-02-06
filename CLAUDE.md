# Project Chimera: AI Agent Rules & Context

## 1. Project Context
"This is Project Chimera, an autonomous influencer system."
The system relies on Spec-Driven Development (SDD), MCP traceability, and a hierarchical swarm architecture (Planner -> Worker -> Judge).

## 2. The Prime Directive
> [!IMPORTANT]
> **NEVER generate code without checking the `specs/` directory first.**
> All implementations MUST align with:
> - `.specify/memory/constitution.md`: The governing "Golden" rules.
> - `specs/[FEATURE]/_meta.md`: Feature vision and constraints.
> - `specs/[FEATURE]/functional.md`: User scenarios and agent behaviors.
> - `specs/[FEATURE]/technical.md`: Technical plan and tool contracts.

## 3. Rules of Engagement & Traceability
*   **Traceability**: Every plan and mission-critical action must be explained before execution (Explain your plan before writing code).
*   **Logging**: Every major architectural decision or handshake success must be logged using the Project's MCP Sense mechanisms.
*   **MCP Usage**: Always prefer using MCP tools for external interactions.

## 4. Development Standards
*   **Python**: Use `PYTHONPATH=.` for execution. Maintain strict typing (Pydantic/MyPy).
*   **Schemas**: Adhere to the defined JSON schemas in `specs/technical.md`.
*   **Fluency**: Call trigger logging tools in `.agent/scripts/` at the end of work or when patterns are detected.
*   **Tooling**: Use `uv run specify` for spec management and compliance checks.
*   **Workflow**: Specify -> Plan -> Tasks -> Implement.
