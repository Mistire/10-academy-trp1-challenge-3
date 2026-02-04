"""Demo script to simulate an MCP handshake and write a confirmed connection log."""
from mcp_sense import on_mcp_handshake_success


if __name__ == "__main__":
    on_mcp_handshake_success(
        server_id="mcp-server-twitter",
        client_id="agent-chimera-001",
        transport="stdio",
        handshake_id="demo-0001",
        extra={"version": "0.1-demo"},
    )
    print("Wrote demo handshake to logs/mcp-sense-connections.log")
