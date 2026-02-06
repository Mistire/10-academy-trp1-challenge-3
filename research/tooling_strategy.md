# Research: Tooling Strategy for Project Chimera

## 1. Strategic Goal: Decoupling Development vs. Runtime
To maintain a professional agentic environment, we strictly separate **Developer Tools** (which help the human and co-pilot build the system) from **Agent Skills** (which the autonomous influencer uses at runtime).

## 2. Developer Tooling (Build-Time)
These tools facilitate the Spec-Driven Development (SDD) lifecycle and environmental traceability.

### 2.1 GitHub Spec Kit Framework
- **Status**: **MANDATORY**. All specifications must reside in feature-based subdirectories (e.g., `specs/001-project-chimera/`).
- **Governance**: Every implementation must be checked via `uv run specify check` for compliance with `.specify/memory/constitution.md`.
- **Workflow**: `specify init` -> `specify define` (Specify/Plan/Tasks) -> TDD Development.

### 2.2 Model Context Protocol (MCP) Servers
- **Git-MCP**: Version control orchestration and commit traceability. Enables the agent to manage feature branches based on spec updates.
- **Filesystem-MCP**: Precise, low-latency file operations. Edits must be validated against `specs/[FEATURE]/technical.md` before commitment.
- **Tenx MCP Sense**: **ACTIVE**. Telemetry flight-recorder for auditing every "Thinking" process and tool execution.

## 3. Runtime Skills Strategy
- **Isolation**: Skills are stateless Python modules located in `skills/`.
- **Interchangeability**: Standardized I/O contracts allow swapping provider implementations (e.g., OpenAI vs. Gemini) without logic breaks.
- **Verification**: Every Skill is guarded by a corresponding test in `tests/test_skills_interface.py`.

## 4. Environment Governance
- **Package Manager**: `uv` for fast, reproducible, lockfile-locked dependency management.
- **Spec Management**: Mandatory use of `uv run specify` for all lifecycle phases.
- **CI/CD**: GitHub Actions run `make test` and `specify check` on every push to verify absolute spec alignment and architectural integrity.
