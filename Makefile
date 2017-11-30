ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV_NAME:=venv

install:
	mkdir $(VENV_NAME)
	virtualenv -p /usr/bin/python3 $(VENV_NAME)
	$(ROOT_DIR)/$(VENV_NAME)/bin/pip install -r requirements.txt

run:
	$(ROOT_DIR)/venv/bin/python -B main.py

production:
	$(ROOT_DIR)/venv/bin/python -B main.py &

log:
	($(ROOT_DIR)/venv/bin/python -B main.py) >> log.txt 2>&1

clean:
	rm log.txt

help:
	@echo "Available Targets:"
	@echo "- install    Install project dependencies"
	@echo "- run        Starts Peterman Bot"
	@echo "- production Starts Peterman Bot in the background"
	@echo "- log        Starts Peterman Bot and logs output to log.txt"
	@echo "- clean      Cleans up the source directory"
