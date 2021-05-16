.PHONY: install
install:
	pip3 install -U poetry
	poetry install

.PHONY: style
style:
	poetry run autoflake --remove-all-unused-imports --in-place -r .
	poetry run isort --atomic .
	poetry run black --exclude setup.py .
	poetry run flake8 .

.PHONY: format
format: style

.PHONY: type
type:
	poetry run mypy --ignore-missing-imports tests amortization

.PHONY: test
test:
	poetry run pytest --cov=amortization --cov-report=xml --cov-report=html -vv

.PHONY: setup
setup:
	poetry run dephell deps convert
