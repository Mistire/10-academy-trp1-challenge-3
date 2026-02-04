import json
import logging
import os
from datetime import datetime
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

    # Avoid adding multiple handlers if logger has been set up already
    if not logger.handlers:
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
    return datetime.utcnow().isoformat() + "Z"


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
