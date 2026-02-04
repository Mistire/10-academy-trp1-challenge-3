# 10Academy Challenge 3 - MCP, Research, and Reporting

This repository contains the implementation of MCP integration, structured research, and reporting for 10Academy Challenge 3.

## Components

### 1. Model Context Protocol (MCP) Integration
Uses MCP to establish connections with analytics and feedback servers. Configuration can be found in `.vscode/mcp.json`.

### 2. MCP Sense
A structured logging utility situated in `mcp_sense/` for auditing "confirmed" MCP connection handshakes.
- **Verification**: Run `PYTHONPATH=. python3 scripts/mcp_handshake_demo.py` to simulate a handshake and view logs in `logs/mcp-sense-connections.log`.

### 3. Research
The `research/` directory contains systematic investigation and data gathering related to influencer analytics and feedback mechanisms.

### 4. Reporting
The `report/` directory holds the generated findings and analytics reports derived from the research and MCP data.

## Getting Started

### Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### Running Tests
Ensure `pytest` and `pytest-asyncio` are installed:
```bash
python3 -m pip install pytest pytest-asyncio
PYTHONPATH=. pytest
```
