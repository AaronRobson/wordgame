# wordgame
[![Build Status](https://travis-ci.org/AaronRobson/wordgame.svg?branch=master)](https://travis-ci.org/AaronRobson/wordgame)
[![CircleCI](https://circleci.com/gh/AaronRobson/wordgame.svg?style=svg)](https://circleci.com/gh/AaronRobson/wordgame)
[![Coverage Status](https://coveralls.io/repos/github/AaronRobson/wordgame/badge.svg?branch=master)](https://coveralls.io/github/AaronRobson/wordgame?branch=master)

A solver for wordgames such as scrabble and countdown

## Install

### Install from PyPi
```bash
pip3 install wordgame --upgrade --user
```

### Install locally
```bash
python3 -m pip install . --user
```

## Run program
```bash
python3 -m wordgame -n 10 fdofieasg
```
Which should result in words such as `offside`.

## Common operations
To run linting, unit tests and package building run the following.
```bash
make
```

### Run linting
```bash
make check
```
or
```bash
python3 setup.py flake8
```

### Run unit tests
```bash
make test
```
or
```bash
python3 -m unittest
```

### Packaging
```bash
make build
```
or
```bash
python3 setup.py sdist bdist_wheel
```

### Uploading
Ensure that the version number is distinct from the previous version.

#### Upload to test instance of PyPi
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

#### Upload to the proper PyPi
```bash
twine upload dist/*
```

## Word list
[words.txt](words.txt)

source: https://www.instructables.com/id/Python-and-Word-Lists/
