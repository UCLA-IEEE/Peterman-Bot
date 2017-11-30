# Peterman Bot

Python script that interacts with the Slack Python API to receive commands from
users. It runs on a Raspberry Pi within the IEEE at UCLA lab, and is connected
to a local network so that it can scan for mac addresses that are connected to
the network.

IEEE at UCLA, an EE and CS student organization on campus, has a lab that is
only open when officers are in the lab for assistance. Although the lab is
regularly open on weekdays from 10AM-6PM, members often wonder whether officers
are keeping the lab open during irregular hours/weekends, or whether specific
officers such as project leads are in the lab. This bot serves as an aid to that
problem, and notifies members of which officers are in the lab.

## Setting up a development environment

Clone the repo and navigate into it.

Make sure you have the following dependencies installed. If you're developing on
MacOSX, you can install these with Homebrew.\
python3\
pip3\
arp-scan

Place a `config.json` file (obtained from owner) within the `config` directory

Run `make install` to install this project's dependencies and initialize virtual
environments

Run `make run` to start the bot

Message bot on the slack channel to test its response.

## Supported Commands

```
whois        - prints out a list of the people currently in the lab by look-up method
whoshould    - prints out a list of people who should be in lab according to a
               a lab hours spreadsheet
```
