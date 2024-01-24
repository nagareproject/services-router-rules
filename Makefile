DOC_OUTPUT_DIR ?= doc/_build

.PHONY: doc tests

clean:
	@rm -rf build dist
	@rm -rf nagare/*.egg-info
	@find nagare \( -name '*.py[co]' -o -name '__pycache__' \) -delete
	@rm -rf doc/_build/*

install-dev: clean
	python -m pip install -e '.[dev']
	git init
	python -m pre_commit install
	python -m pre_commit autoupdate

tests:
	python -m pytest nagare

qa:
	python -m ruff nagare
	python -m ruff format --check nagare
	# $(MAKE) tests

qa-fix:
	python -m ruff --fix nagare
	python -m ruff format nagare

doc:
	python -m sphinx.cmd.build -b html doc ${DOC_OUTPUT_DIR}

wheel:
	python -m pip wheel -w dist --no-deps .
