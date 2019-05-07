install:
	pipenv install

test: install
	pipenv run tox

build: install
	pipenv run python setup.py sdist bdist_wheel

clean:
	rm -rf build dist django_filter_addons.egg-info

.PHONY: install test build clean
