# Project Chimera: Functional Specification

## 1. User Stories

### 1.1 For the Network Operator (Strategic Manager)
- **Goal Definition**: "As a Network Operator, I want to define a natural language goal (e.g., 'Promote the new summer fashion line in Ethiopia') so the agent can decompose it into tasks."
- **Fleet Monitoring**: "As a Network Operator, I want to view the real-time status of all active agents (Planning, Working, Judging, Sleeping) to ensure campaign health."
- **Safety Overrides**: "As a Network Operator, I want to review escalated tasks that fall below confidence thresholds to maintain brand safety."

### 1.2 For the Chimera Agent (Autonomous Entity)
- **Trend Discovery**: "As an Agent, I need to fetch news and social resources (e.g., `news://ethiopia/fashion/trends`) via MCP to identify emerging cultural trends."
- **Asset Generation**: "As an Agent, I need to use specialized generation tools (Ideogram for images, Luma for video) to produce matching campaign components."
- **Financial Autonomy**: "As an Agent, I need to check my wallet balance via Coinbase AgentKit before initiating cost-incurring tasks to remain solvent."

## 2. Behavioral Requirements (The "Agentic" Lifecycle)
- **FR 2.1: Semantic Filtering**: Agents SHALL NOT automatically respond to all inputs. Every ingestion must pass through a **Semantic Filter** (Gemini 3 Flash) with a configurable **Relevance Threshold (0.75)**.
- **FR 2.2: Persona Consistency**: All outputs MUST strictly adhere to the agent's defined `SOUL.md` (Backstory, Voice, Directives).
- **FR 2.3: Automated Disclosure**: Agents MUST prioritize a **"Honesty Directive"** to force a truthful, unambiguous disclosure if questioned about their AI nature (e.g., "I am a virtual persona created by AI.").
- **FR 2.4: Traceability**: Every mission-critical action and successful MCP handshake MUST be logged via **MCP Sense**.
- **FR 2.5: Trend Detection**: A background Worker SHALL analyze aggregated News Resources over 4-hour intervals to detect topic clusters and generate "Trend Alerts" for the Planner.

## 3. Creative Engine Requirements (Asset Generation)
- **FR 3.1: Character Consistency Lock**: Every image generation request MUST automatically inject a `character_reference_id` or LoRA (Low-Rank Adaptation) identifier to maintain influencer facial consistency.
- **FR 3.2: Hybrid Video Strategy**:
    - **Tier 1 (Routine)**: Static Image + Motion Brush (Image-to-Video).
    - **Tier 2 (Hero)**: Full Text-to-Video (Runway/Luma).
- **FR 3.3: Judge Validation**: The Judge Node SHALL use a Vision-capable LLM to verify that generated images match the canonical persona *before* publication.

## 4. Economic Requirements
- **FR 4.1: Budget Check**: The Planner MUST call `get_balance` via CDP AgentKit before initiating any cost-incurring task.
- **FR 4.2: CFO Enforcement**: A CFO Sub-Agent (Judge) SHALL reject any transaction exceeding daily limits or matching suspicious patterns.
