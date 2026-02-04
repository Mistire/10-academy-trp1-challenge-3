import json
from pathlib import Path

from mcp_sense import emit_handshakes_from_mcp_config


def test_emit_handshakes(tmp_path):
    cfg = tmp_path / ".vscode"
    cfg.mkdir()
    cfg_file = cfg / "mcp.json"
    cfg_file.write_text(json.dumps({
        "servers": {
            "tenxfeedbackanalytics": {
                "url": "https://mcppulse.10academy.org/proxy",
                "type": "http",
                "headers": {"X-Device": "linux"}
            },
            "local-test": {
                "url": "http://localhost:8080",
                "type": "http"
            }
        }
    }))

    n = emit_handshakes_from_mcp_config(config_path=str(cfg_file), agent_id="test-agent", handshake_prefix="testprefix", log_dir=str(tmp_path / "logs"))
    assert n == 2

    log_file = tmp_path / "logs" / "mcp-sense-connections.log"
    assert log_file.exists()
    content = log_file.read_text().strip().splitlines()
    # two lines written
    assert len(content) == 2
    last = json.loads(content[-1])
    assert last["client_id"] == "test-agent"
    assert "handshake_id" in last
