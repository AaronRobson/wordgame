# wordgame
[![Build Status](https://travis-ci.org/AaronRobson/wordgame.svg?branch=master)](https://travis-ci.org/AaronRobson/wordgame)
[![CircleCI](https://circleci.com/gh/AaronRobson/wordgame.svg?style=svg)](https://circleci.com/gh/AaronRobson/wordgame)
[![Coverage Status](https://coveralls.io/repos/github/AaronRobson/wordgame/badge.svg?branch=master)](https://coveralls.io/github/AaronRobson/wordgame?branch=master)

A solver for wordgames such as scrabble and countdown

## Install locally
```bash
python3 -m pip install . --user
```

## Run program
```bash
python3 -m wordgame fdofieasg --game countdown --maximum-number-of-results 10
```
Which should result in words such as `offside`.

## Run both linting and unit testing
To run both linting and unit tests run the following.
```bash
make
```
This consists of the following steps.

### Run linting
```bash
python3 setup.py flake8
```

### Run unit tests
```bash
python3 -m unittest
```
or
```bash
python3 setup.py test
```

## Word list
[words.txt](words.txt)

### Source https://www.instructables.com/id/Python-and-Word-Lists/
