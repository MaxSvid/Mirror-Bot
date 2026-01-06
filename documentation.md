# Project Structure

# Telegram Multi-Purpose Bot

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

- [Python Classes and Objects](https://www.geeksforgeeks.org/python/python-classes-and-objects/) for config.py
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

# Docker Hub Links to learn

- [Official Image from Docker Hub: Postgres](https://hub.docker.com/_/postgres)

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)

- [postgres docker storage](https://hub.docker.com/_/postgres)

- [dpage/pgadmin4](https://hub.docker.com/r/dpage/pgadmin4/)

- [Understanding the Docker root USER Instruction from Dockerfile](https://www.docker.com/blog/understanding-the-docker-user-instruction/)

- [Running with Non-Root User and Syncing Host with Container Permissions](https://dev.to/izackv/running-a-docker-container-with-a-custom-non-root-user-syncing-host-and-container-permissions-26mb)


