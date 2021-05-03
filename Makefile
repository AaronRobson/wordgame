.DEFAULT_GOAL := all

.PHONY: all
all: check test build

.PHONY: install-packages
install-packages:
	pip3 install --upgrade \
	  -r dev-requirements.txt \
	  -r requirements.txt

.PHONY: clean
clean:
	rm -rf dist build */*.egg-info *.egg-info

.PHONY: check
check:
	flake8

.PHONY: test
test:
	python3 setup.py test

.PHONY: build
build: clean
	python3 setup.py sdist bdist_wheel
