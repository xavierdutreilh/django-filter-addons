install:
	pipenv install

test: install
	pipenv run tox

.PHONY: install test
