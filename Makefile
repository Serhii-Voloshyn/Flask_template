#
# Makefile for rfadjustments
#
.PHONY: flake
flake:
	flake8

.PHONY: check-types
check-types:
	pyre --source-directory service_api --search-path . check

.PHONY: check
check: check-types flake

.PHONY: coverage
coverage: flake
	coverage run --rcfile=.coveragerc venv/bin/py.test -v tests/
	coverage report --rcfile=.coveragerc

.PHONY: run-dev
run-dev:
	python manage.py runserver