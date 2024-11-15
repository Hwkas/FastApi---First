format:
	ruff check --select I --fix && ruff format

run-dev:
	uvicorn src.main:app --reload