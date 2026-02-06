.PHONY: setup test spec-check clean

# Standard setup: Install dependencies via uv
setup:
	@echo "Setting up Project Chimera environment..."
	uv sync --extra test
	@echo "Setup complete."

# Run tests in the local environment
test:
	@echo "Running tests..."
	uv run pytest tests/

# Run tests in a Docker container (standard orchestration)
docker-test:
	@echo "Building and running tests in Docker..."
	docker build -t chimera-governor .
	docker run --rm chimera-governor

# Verify if code aligns with specs using the GitHub Spec Kit
spec-check:
	@echo "Running official Spec Kit compliance check..."
	uv run specify check

# Clean up temporary build artifacts
clean:
	rm -rf .venv .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
