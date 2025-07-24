.PHONY: docs
init:
	pip install -e ".[dev]"

lint:
	ruff check .

typecheck:
	mypy .

test:
	python3 -m pytest tests

coverage:
	python -m pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=fsm tests

all: lint typecheck test coverage
