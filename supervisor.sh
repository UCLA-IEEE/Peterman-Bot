#!/bin/bash

touch log.txt
chown $USER log.txt

(python -B main.py) >> log.txt 2>&1