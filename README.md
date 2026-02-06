# Project Chimera: The Autonomous Influencer Factory

**Version:** 1.0.0
**Mission:** *Architecting the system that builds the self-aware influencer of the future.*

---

## Overview

Project Chimera is an engineering-first platform for building **Autonomous AI Influencers**. These are not mere chatbots; they are persistent digital entities capable of:
- **Perception**: Analyzing news and high-velocity social trends via Model Context Protocol (MCP).
- **Reasoning**: Planning and decomposing complex goals into actionable tasks using an LLM-driven Swarm.
- **Creation**: Generating professional-grade multimodal assets (Ideogram, Luma, Runway).
- **Agency**: Managing on-chain financial resources and transactions via Coinbase AgentKit.

This repository serves as the **Lead Architect's Blueprint**, providing a "Golden" environment where agents can independently build, test, and deploy features.

---

## Core Philosophies

### 1. Spec-Driven Development (SDD)
In this project, ambiguity is considered a bug. We follow a strict SDD workflow:
- **Ratification**: No code is written until the Specification (in `specs/`) is approved.
- **Source of Truth**: The specs define the exact behavioral and technical bounds for the AI agents.
- **Rubric**: High score potential is achieved by keeping implementation and specification in perfect sync.

### 2. FastRender Swarm Architecture
The system operates on a hierarchical, role-based swarm pattern to ensure quality and throughput:
- **Planner**: The Strategist. Decomposes goals into a Directed Acyclic Graph (DAG) of tasks.
- **Worker**: The Executor. Stateless, atomic task execution via specialized MCP Tools.
- **Judge**: The Governor. Performs QA, validation, and enforces safety/persona consistency.

### 3. Traceability via MCP Sense
Every internal "thought" and external "handshake" is captured. We use **Tenx MCP Sense** as a flight recorder, ensuring that autonomous actions are audit-ready and observable.

---

### `specs/` - Feature-Based Specifications (GitHub Spec Kit)
Each feature (e.g., `001-project-chimera`) contains a full specification suite:
- **`_meta.md`**: Feature vision, constraints, and high-level goal.
- **`functional.md`**: User scenarios (SDD) and behavioral requirements.
- **`technical.md`**: Technical blueprints, swarm role assignments, and MCP contracts.
- **`tasks.md`**: Actionable checklist for implementation.

### `.specify/` - Framework Core
- **`memory/constitution.md`**: The supreme governing principles (Fractal Orchestration, Agentic Commerce).
- **`project.json`**: Project metadata for Spec Kit compliance.

### `SOUL.md` - The Persona DNA
Defines the immutable core of the Chimera Agent: **Backstory**, **Voice**, **Beliefs**, and **Hard Directives**.

### `skills/` - Agentic Capabilities
Modular "Skills" (runtime packages) with strict I/O contracts.

### `research/` - High-Level Strategy
Architectural and tooling deep-dives.

### `tests/` - The Safety Net (TDD)
Failing tests that define the contract for features before they are implemented.

### `.agent/` - Internal Governance
Contains the `instructions.md` and "Prime Directives" for AI coding assistants, ensuring they follow the project's specifications natively.

---

## Orchestration & Environment

This project is built for the modern AI-assisted workflow, utilizing **uv** for lightning-fast, reproducible dependency management and **Docker** for environment isolation.

### 1. Prerequisites
- [uv](https://github.com/astral-sh/uv) installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Docker (optional, for containerized testing)

### 2. Setup
Initialize the "Golden" environment and install all dependencies:
```bash
make setup
```

### 3. Verification (Local)
Run the TDD baseline to see current failing tests (defining the next implementation steps):
```bash
make test
```

### 4. Containerized Orchestration (CI-Ready)
Run the entire governance pipeline inside an isolated Docker container:
```bash
make docker-test
```

### 5. Spec Alignment Check
Verify that the current code items match the architectural blueprint in `specs/`:
```bash
make spec-check
```

---

## AI Governance & CI/CD

We enforce professional engineering standards through an automated governance pipeline:
- **GitHub Actions**: Every push triggers a `make test` run in a clean environment.
- **CodeRabbit**: An AI-driven review policy (configured in `.coderabbit.yaml`) that checks for:
  - Strict alignment with the **Master Specification**.
  - Use of **Optimistic Concurrency Control (OCC)**.
  - Adherence to the **10-second Latency NFR**.
  - **Persona Consistency** via SOUL.md.

---

*Project Chimera (FDE Challenge 3)*