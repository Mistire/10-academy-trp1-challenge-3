"""Demo script to simulate an MCP handshake and write a confirmed connection log."""
from mcp_sense import emit_handshakes_from_mcp_config
import os


if __name__ == "__main__":
    # Use .vscode/mcp.json by default; override with MCP_CONFIG env var
    cfg = os.environ.get("MCP_CONFIG", ".vscode/mcp.json")
    agent = os.environ.get("MCP_AGENT_ID", "agent-chimera-demo")
    prefix = os.environ.get("MCP_HANDSHAKE_PREFIX", "demo")

    try:
        n = emit_handshakes_from_mcp_config(config_path=cfg, agent_id=agent, handshake_prefix=prefix)
        print(f"Wrote {n} handshake entries to logs/mcp-sense-connections.log")
    except FileNotFoundError as e:
        print(str(e))
        raise
