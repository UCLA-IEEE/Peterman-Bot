ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV_NAME:=venv

install:
	mkdir $(VENV_NAME)
	virtualenv -p /usr/bin/python3 $(VENV_NAME)
	$(ROOT_DIR)/$(VENV_NAME)/bin/pip install -r requirements.txt

dev:
	$(ROOT_DIR)/$(VENV_NAME)/bin/python -B main.py

run:
	$(ROOT_DIR)/$(VENV_NAME)/bin/python main.py

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
