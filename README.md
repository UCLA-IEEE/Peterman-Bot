# Occupancy Sensor
Python script that runs on a Raspberry Pi inside of student group, UCLA IEEE's, lab. Scans wifi network every 5 seconds to check if any officers are in the lab. If members of the club message the bot on Slack, it responds with a list of officers available in the lab.

![Screenshot](http://rpeterman.me/app/static/petermanbot.png)

## Problem
IEEE at UCLA, the EE and CS student organization on campus, has a lab that is only open when officers are in the lab for assistance. Although the lab is regularly open on weekdays from 10AM-6PM, members often wonder whether officers are keeping the lab open during irregular hours/weekends, or whether specific officers such as project leads are in the lab. Therefore, this bot serves as a solution to that problem, and notifies members of exactly which officers are in the lab.

## Technical Overview
How the look-up works:

1. Use arp-scan to ask router for mac addresses of devices connected to the router
2. Check if any MAC addresses matches with the ones on the list of officer mac addresses

How Slack Bot works:

Constantly pings Slack Python API for incomming messages and responds accordingly. Every 5 seconds the script performs a scan of the network
to update its records so the Slack messages contain the most up to date information.

## Basic Commands
```
whois - prints out a list of the people currently in the lab by look-up method
```
