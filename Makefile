install:
	pip install -r requirements.txt

run:
	python -B main.py

log:
	touch log.txt
	chown $USER log.txt
	(python -B main.py) >> log.txt 2>&1

clean:
	rm log.txt

help:
	@echo "Available Targets:"
	@echo "- install    Install project dependencies"
	@echo "- run        Starts Peterman Bot"
	@echo "- log        Starts Peterman Bot and logs output to log.txt"
	@echo "- clean      Cleans up the source directory"
