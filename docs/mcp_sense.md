# MCP Sense: Confirmed Connection Log

This module provides a simple structured logger for "confirmed" MCP connections (handshakes) used for auditing and MCP Sense dashboards.

Usage

- Programmatically call `on_mcp_handshake_success(server_id, client_id, transport, handshake_id, extra)` from your MCP Server or Host after a successful discovery/advertise/list_resources handshake.
- Logs are written as JSON lines to `logs/mcp-sense-connections.log` by default.

Example

```
from mcp_sense import on_mcp_handshake_success

on_mcp_handshake_success(
  server_id="mcp-server-twitter",
  client_id="agent-chimera-001",
  transport="stdio",
  handshake_id="abc-123",
  extra={"capabilities": ["post_tweet", "mentions"]}
)
```

Verification

- Tail the log: `tail -f logs/mcp-sense-connections.log`
- Each entry is a JSON object with at least: `event`, `server_id`, `client_id`, `transport`, `timestamp`.

Notes

- Include public keys or signed challenge IDs in `extra` if you require cryptographic proof in the log.
- Rotate and centralize logs in production (ELK, Loki, etc.).
