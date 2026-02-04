# MCP Sense: Confirmed Connection Log

`mcp_sense` is a structured logging utility designed for auditing and monitoring "confirmed" MCP connections (handshakes) within the 10Academy Challenge project.

## Overview

It provides functions to emit JSON-formatted log entries whenever a successful handshake occurs between an MCP Client and an MCP Server. These logs are stored in `logs/mcp-sense-connections.log` by default.

## Features

- **Standardized Logs**: Each entry contains `event`, `server_id`, `client_id`, `transport`, `timestamp`, and `extra` data.
- **Config-Driven Emittance**: Can automatically emit handshakes based on an `mcp.json` configuration file.
- **Test-Friendly**: Logger setup handles changing directory paths during unit testing.

## Programmatic Usage

### 1. Manual Handshake Logging
Call `on_mcp_handshake_success` after a successful discovery or handshake.

```python
from mcp_sense import on_mcp_handshake_success

on_mcp_handshake_success(
    server_id="tenxfeedbackanalytics",
    client_id="agent-chimera-demo",
    transport="http",
    handshake_id="unique-id-123",
    extra={"url": "https://mcppulse.10academy.org/proxy"}
)
```

### 2. Batch Logging from Config
Use `emit_handshakes_from_mcp_config` to log all servers defined in a configuration file.

```python
from mcp_sense import emit_handshakes_from_mcp_config

# Automatically processes .vscode/mcp.json by default
emit_handshakes_from_mcp_config(agent_id="my-agent")
```

## Verification

### Using the Demo Script
A simulation script is provided to quickly generate and verify logs:
```bash
PYTHONPATH=. python3 scripts/mcp_handshake_demo.py
```

### Viewing Logs
You can monitor the log file in real-time:
```bash
tail -f logs/mcp-sense-connections.log
```

## Logs Schema

Each log line is a single JSON object:
- `event`: Always `"connection_confirmed"`.
- `server_id`: The ID of the MCP server.
- `client_id`: The ID of the client (agent).
- `transport`: The transport type (e.g., `stdio`, `http`).
- `timestamp`: ISO 8601 UTC timestamp.
- `handshake_id`: Unique identifier for the handshake.
- `extra`: Dictionary for additional metadata (URLs, headers, etc.).
