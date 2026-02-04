import json
from pathlib import Path

from mcp_sense import on_mcp_handshake_success


def test_writes_handshake_to_log(tmp_path):
    log_dir = tmp_path / "logs"
    on_mcp_handshake_success(
        server_id="test-server",
        client_id="test-client",
        transport="stdio",
        handshake_id="test-1",
        extra={"foo": "bar"},
        log_dir=str(log_dir),
    )

    log_file = log_dir / "mcp-sense-connections.log"
    assert log_file.exists(), "Log file was not created"

    content = log_file.read_text()
    assert "connection_confirmed" in content
    data = json.loads(content.strip().splitlines()[-1])
    assert data["server_id"] == "test-server"
    assert data["client_id"] == "test-client"
    assert data["handshake_id"] == "test-1"
