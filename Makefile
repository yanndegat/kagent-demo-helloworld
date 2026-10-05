PYTHON ?= python3

.PHONY: build test run clean

build:  ## byte-compile the sources (fails on a syntax error)
	$(PYTHON) -m py_compile hello.py tests/test_hello.py
	@echo "build ok"

test: build  ## run the unit tests
	$(PYTHON) -m unittest discover -s tests -t . -v

run:
	$(PYTHON) hello.py

clean:
	rm -rf __pycache__ tests/__pycache__
