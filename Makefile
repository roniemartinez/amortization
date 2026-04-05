.PHONY: install
install:
	uv sync

.PHONY: lint
lint:
	uv run pre-commit run --all-files

.PHONY: test
test:
	uv run pytest

.PHONY: tag
tag:
	VERSION=`uv run python -c "import tomllib; print(tomllib.load(open('pyproject.toml','rb'))['project']['version'])"`; \
	git tag -s -a $$VERSION -m "Release $$VERSION"; \
	echo "Tagged $$VERSION";
