import pytest
import os
from unittest.mock import MagicMock

# Global Fixtures and Mocks for Project Chimera TDD

@pytest.fixture(autouse=True)
def mock_settings():
    """Sets up mandatory environment variables for testing."""
    os.environ["GEMINI_API_KEY"] = "mock-key"
    os.environ["CDP_API_KEY_NAME"] = "mock-name"
    os.environ["CDP_API_KEY_PRIVATE_KEY"] = "mock-private-key"
    yield
    # Clean up is not strictly necessary for tests but good practice
    os.environ.pop("GEMINI_API_KEY", None)

@pytest.fixture
def mock_gemini():
    """Mocks the Google Generative AI (Gemini) response objects."""
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Mocked AI response text"
    mock_model.generate_content.return_value = mock_response
    return mock_model

@pytest.fixture
def mock_agentkit():
    """Mocks Coinbase AgentKit Wallet and Tool interfaces."""
    mock_wallet = MagicMock()
    mock_wallet.get_address.return_value = "0xMockAddress"
    mock_wallet.get_balance.return_value = 100.0
    
    mock_action = MagicMock()
    mock_action.transaction_hash = "0xMockHash"
    mock_action.status = "confirmed"
    
    return {
        "wallet": mock_wallet,
        "action": mock_action
    }

@pytest.fixture
def mock_redis():
    """Mocks Redis for task queue testing."""
    mock_conn = MagicMock()
    mock_conn.ping.return_value = True
    return mock_conn

@pytest.fixture
def mock_weaviate():
    """Mocks Weaviate for semantic memory testing."""
    mock_client = MagicMock()
    mock_client.is_live.return_value = True
    return mock_client
