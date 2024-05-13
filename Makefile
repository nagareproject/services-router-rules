.PHONY: doc tests

clean:
	@rm -rf build dist
	@rm -rf nagare/*.egg-info
	@find nagare \( -name '*.py[co]' -o -name '__pycache__' \) -delete
	@rm -rf doc/_build/*

upgrade-precommit:
	python -m pre_commit autoupdate

install: clean
	python -m pip install -e '.[dev']
	git init
	python -m pre_commit install

tests:
	python -m pytest nagare

qa:
	python -m ruff check nagare
	python -m ruff format --check nagare
	# $(MAKE) tests

qa-fix:
	python -m ruff check --fix nagare
	python -m ruff format nagare

doc:
	python -m sphinx.cmd.build -b html doc doc/_build

wheel:
	python -m pip wheel -w dist --no-deps .
