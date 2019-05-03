.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: check
check:
	python3 setup.py flake8

.PHONY: test
test:
	python3 setup.py test
