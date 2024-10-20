install:
		poetry install

gendiff:
		poetry run gendiff

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml --debug

publish:
		poetry publish --dry-run

lint:
		poetry run flake8 gendiff

selfcheck:
		poetry check

check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build