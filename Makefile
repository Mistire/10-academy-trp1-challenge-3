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

# Placeholder for spec-check logic (optional but recommended)
spec-check:
	@echo "Comparing code items against specs/ directory..."
	@# In a real scenario, this would trigger a script that uses LLM or static analysis
	@# to verify if current function signatures match functional.md/technical.md
	@ls specs/ | grep -q . || (echo "Error: specs/ directory is empty!" && exit 1)
	@echo "Spec-check passed (Basic structure verification)."

# Clean up temporary build artifacts
clean:
	rm -rf .venv .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
