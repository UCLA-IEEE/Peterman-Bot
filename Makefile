ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

install:
	pip3 install virtualenv
	mkdir venv
	virtualenv venv
	$(ROOT_DIR)/venv/bin/pip install -r requirements.txt

run:
	$(ROOT_DIR)/venv/bin/python -B main.py

log:
	(python -B main.py) >> log.txt 2>&1

clean:
	rm log.txt

help:
	@echo "Available Targets:"
	@echo "- install    Install project dependencies"
	@echo "- run        Starts Peterman Bot"
	@echo "- log        Starts Peterman Bot and logs output to log.txt"
	@echo "- clean      Cleans up the source directory"
