import json
import logging
import os
from datetime import datetime, timezone
from typing import Optional, Dict

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "mcp-sense-connections.log"


def setup_logger(log_dir: Optional[str] = None, log_file: Optional[str] = None) -> logging.Logger:
    """Set up a structured JSON logger writing to the MCP sense log file.

    Returns a logger instance.
    """
    log_dir = log_dir or DEFAULT_LOG_DIR
    log_file = log_file or DEFAULT_LOG_FILE
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, log_file)

    logger = logging.getLogger("mcp.sense")
    logger.setLevel(logging.INFO)

    # If handlers already exist, check if they match the desired path
    if logger.handlers:
        existing_file_handler = next((h for h in logger.handlers if isinstance(h, logging.FileHandler)), None)
        if existing_file_handler and existing_file_handler.baseFilename == os.path.abspath(path):
            return logger
        
        # Paths differ, clear old handlers to re-setup for new path (common in tests)
        for handler in list(logger.handlers):
            logger.removeHandler(handler)
            handler.close()

    handler = logging.FileHandler(path)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)

    # also log to stdout for local development
    stream = logging.StreamHandler()
    stream.setLevel(logging.INFO)
    stream.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(stream)

    return logger


def _now_iso() -> str:
    """Get current timestamp in ISO format with UTC Z suffix."""
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def on_mcp_handshake_success(
    server_id: str,
    client_id: str,
    transport: str,
    handshake_id: Optional[str] = None,
    extra: Optional[Dict] = None,
    log_dir: Optional[str] = None,
    log_file: Optional[str] = None,
) -> None:
    """Emit a structured 'connection_confirmed' JSON log entry.

    This should be called by MCP Server and MCP Host after a successful discovery/handshake.
    """
    logger = setup_logger(log_dir=log_dir, log_file=log_file)
    entry = {
        "event": "connection_confirmed",
        "server_id": server_id,
        "client_id": client_id,
        "transport": transport,
        "handshake_id": handshake_id,
        "timestamp": _now_iso(),
        "extra": extra or {},
    }
    logger.info(json.dumps(entry))


def emit_handshakes_from_mcp_config(
    config_path: str = ".vscode/mcp.json",
    agent_id: str = "agent-chimera-demo",
    handshake_prefix: Optional[str] = None,
    log_dir: Optional[str] = None,
    log_file: Optional[str] = None,
) -> int:
    """Read an MCP config file and emit a connection_confirmed entry per server.

    Returns the number of handshakes emitted.
    """
    import json as _json
    from pathlib import Path as _Path

    cfg_path = _Path(config_path)
    if not cfg_path.exists():
        raise FileNotFoundError(f"MCP config not found at {config_path}")

    data = _json.loads(cfg_path.read_text())
    servers = data.get("servers", {})
    count = 0
    for name, meta in servers.items():
        transport = meta.get("type") or meta.get("transport") or "unknown"
        handshake_id = None
        if handshake_prefix:
            handshake_id = f"{handshake_prefix}-{name}"
        else:
            handshake_id = f"auto-{name}-{_now_iso()}"

        on_mcp_handshake_success(
            server_id=name,
            client_id=agent_id,
            transport=transport,
            handshake_id=handshake_id,
            extra={"url": meta.get("url"), "headers": meta.get("headers")},
            log_dir=log_dir,
            log_file=log_file,
        )
        count += 1

    return count
