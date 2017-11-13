# Peterman Bot
Python script that runs on a Raspberry Pi inside IEEE at UCLA's lab. Scans wifi network every 10 seconds to check if any officers are in the lab. If members of the club message the bot on Slack, it responds with a list of officers available in the lab.

## Setting up a development environment
Dependencies to install with pip:  
slackclient  
subprocess

Clone the repo and navigate into it.  
Run `python -B main.py` to start Peterman bot.  
Message Peterman Bot on the slack channel to test its response.

## Problem
IEEE at UCLA, the EE and CS student organization on campus, has a lab that is only open when officers are in the lab for assistance. Although the lab is regularly open on weekdays from 10AM-6PM, members often wonder whether officers are keeping the lab open during irregular hours/weekends, or whether specific officers such as project leads are in the lab. This bot serves as an aid to that problem, and notifies members of which officers are in the lab.

## Technical Overview
How the look-up works:

1. Use arp-scan to ask router for mac addresses of devices connected to the router
2. Check if any MAC addresses matches with the ones on the list of officer mac addresses

How Slack Bot works:

Constantly pings Slack Python API for incoming messages and responds accordingly. Every 10 seconds the script performs a scan of the network
to update its records.

## Basic Commands
```
whois - prints out a list of the people currently in the lab by look-up method
```
