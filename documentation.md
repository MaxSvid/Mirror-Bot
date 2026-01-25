# Project Structure

## Telegram Multi-Purpose Bot

Idea to design Telegram bot for private group chat.  
The bot combines **group moderation**, **GeminiAI API-powered chatting**, **content scraping**, **crypto alerts**, and **daily reports**, deployed using **Docker** on **VPS**.

---

## Features Overview

### GeminiAI Chat Mode
- Supports:
  - Mentions
  - Commands
  - Free chat (configurable)
- Rate-limited to control API

---

### Job Scraping & Daily Job Reports
- Scrape job listings from multiple job websites
- Extract:
  - Job title
  - Company
  - Location / Remote
  - Salary (if available)
  - Job link
- Filter by keywords (e.g. Python, Data, Web3)
- Generate **daily job reports** in chat

---

### Crypto Price Alerts
- Track crypto prices (BTC, ETH, etc.)
- User-defined alerts:
  - Above / below price thresholds
- Periodic summaries
- Alert notifications in group chat

---

## Architecture Overview

- PostgreSQL
Main database for storing user accounts, roles, and optional calculation history.
Needs work on System Architecture Section and Security Considerations Section (auth, hashing, roles)

- Docker & Docker Compose
Containerize the application and database PostgreSQL for consistent environments across development and production
Simple deployment to a VPS Linux Server

# Code Help

- UV Enviroment Guide Video --> https://www.youtube.com/watch?v=6pttmsBSi8M

- [Fast way to create useful .gitignore files for project](https://www.toptal.com/developers/gitignore)

- [__init__ in Python](https://www.geeksforgeeks.org/python/__init__-in-python/)

- [Python Classes and Objects](https://www.geeksforgeeks.org/python/python-classes-and-objects/) for config.py

- [Python dataclasses Module](https://www.w3schools.com/python/ref_module_dataclasses.asp)

- [asyncio in Python](https://www.geeksforgeeks.org/python/asyncio-in-python/)

## Requests Library, we are using HTTPX for asyncio

- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/latest/)

- [Exception Handling Of Python Requests Module](https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module/)

- [HTTPX client document](https://www.python-httpx.org/)

- [Getting Started with HTTPX](https://betterstack.com/community/guides/scaling-python/httpx-explained/)
---

# Git Commands Guide and Cheat Sheet

- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

- Adds a change files/folders in the working dir
```html
git add .
```

- Snapshot of the staged changes
```html
git commit -m "..."
```

- Targets the main branch final pushed
```html
git push origin main
```
# Aiogram Documentation

- [A finite-state machine (FSM) a mathematical model of computation.](https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/index.html)


# Docker Hub Links to learn

- [Official Image from Docker Hub: Postgres](https://hub.docker.com/_/postgres)

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)

- [postgres docker storage](https://hub.docker.com/_/postgres)

- [dpage/pgadmin4](https://hub.docker.com/r/dpage/pgadmin4/)

- [Understanding the Docker root USER Instruction from Dockerfile](https://www.docker.com/blog/understanding-the-docker-user-instruction/)

- [Running with Non-Root User and Syncing Host with Container Permissions](https://dev.to/izackv/running-a-docker-container-with-a-custom-non-root-user-syncing-host-and-container-permissions-26mb)

'''html
show_alert=True ---> shows message with ok 
'''

# keyboars.py file strucute

ReplyKeyboardMarkup -> 4 buttons menu on /start command
Idea not show the reply keyboard by default

Reply keyboard = global UI state
Inline keyboard = contextual UI

ReplyKeyboardMarkup:
- Persistent
- Saved by Telegram app
- Independent of bot online/offline state

InlineKeyboardMarkup:
- Not persistent
- Exists only under a specific message
- Disappears with the message context

ReplyKeyboardRemove:
- to remove / hide the keyboard properly

## Callback buttons for each keyboard option:

- gemini_options -> (text='Gemini Chat') inside button in ReplyKeyboardMarkup reply

- reports_options ->

- alerts_options ->

- settings_options -> 

```html
show_alert=True --> shows message with ok 
```
ONLY to ReplyKeyboardMarkup
```html
resize_keyboard=True,
input_field_placeholder='Choose the options...'
```


        "You are a friendly NPC in a small group chat of friends. "
        "Your tone is helpful and slightly witty. "
        "IMPORTANT: Your responses must never exceed 4 to 5 sentences. "
        "Be concise and get straight to the point."

## Added random auto replies on links
- [Python Random choice() Method](https://www.w3schools.com/python/ref_random_choice.asp) 

# Jobs Web Scraping

Basic idea and methods used for job scraping, currently focusing on [Djinni website](https://djinni.co/jobs/)

[Video to watch on Web Scraping Python](https://www.youtube.com/watch?v=fgFWo0sDApA)
[Simple Async Parcer Source Example](https://gitlab.com/cbs6230646/1609/pythonadvanced/05_06_threads_async_multiprocessing/-/blob/main/async_parcer.py?ref_type=heads)

- First you need to access Developer Tools on your browser
https://helpdeskgeek.com/wp-content/pictures/2020/07/Chrome-DevTools-Menu.png