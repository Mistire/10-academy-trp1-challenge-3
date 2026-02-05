# Research: Tooling Strategy for Project Chimera

## 1. Developer MCP Tools (Build-Time)
These tools facilitate the development lifecycle and environmental traceability.

### 1.1 Git-MCP Server
- **Purpose**: Version control orchestration and commit traceability.
- **Workflow**: Auto-commit logs for significant architectural changes.

### 1.2 Filesystem-MCP Server
- **Purpose**: Low-latency file editing and project structure management.

### 1.3 Tenx MCP Sense (Telemetry)
- **Purpose**: The "Black Box" flight recorder.
- **Requirement**: MUST be active during all ideation and development phases.

## 2. Environment Configuration
- **Package Manager**: `uv` recommended for environment isolation.
- **Testing**: `pytest` + `pytest-asyncio` for TDD validation.
