# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

An async Telegram group bot built with aiogram 3. Supports command menus, inline keyboards, auto-reply triggers, PostgreSQL storage, and OpenRouter AI integration. Early-stage — DB and AI layers are stubs.

## Architecture & Patterns

**Entry point:** `main.py` — loads `.env`, builds `Bot` + `Dispatcher`, registers routers, starts long polling.

**Router registration order matters:** `handlers.router` is included before `replies.router`. aiogram evaluates filters top-down across routers, so more-specific handlers belong in `handlers.py`.

| File | Role |
|---|---|
| `bot/handlers.py` | Primary router — `/start`, inline-button callbacks, Settings menu |
| `bot/keyboards.py` | Inline keyboard builders consumed by handlers |
| `bot/replies.py` | Secondary router — auto-reply triggers (social-media links, phrases); stubs |
| `bot/database/connect.py` | DB connection helper — currently empty |
| `bot/openrouterai/openrouter.py` | OpenRouter API client — token validation helper, not yet wired to handlers |
| `bot/config.py` | Frozen `Settings` dataclass; reads env vars |

**State management:** aiogram FSM (`State` / `StatesGroup`) is available but no states are defined yet.

## Stack Best Practices

- Use `async`/`await` throughout — aiogram 3 is fully async; blocking calls will stall the event loop.
- Add new command handlers to `handlers.py` and auto-reply triggers to `replies.py`.
- Use psycopg3 async API (`await conn.execute(...)`) when implementing DB logic in `database/connect.py`.

## Anti-Patterns

- Do not register handlers directly on the `Dispatcher`; use routers and include them in `main.py`.
- Do not use the `requests` library for new features — the existing `openrouter.py` uses it, but prefer `aiohttp` or `httpx` for async code.
- Do not add tables directly to `init_DB/database.sql` without a migration plan; no migration tool is set up yet.

## Data Models

No ORM or schema defined yet. `init_DB/database.sql` only contains `CREATE DATABASE tg_bot_mirror`. Table definitions and a migration strategy are pending.

`Settings` (frozen dataclass in `bot/config.py`):
- `BOT_TOKEN` — Telegram bot token
- `OPENROUTER_API_KEY` — OpenRouter API key

## Security & Configuration

All secrets are loaded from `.env` via `load_dotenv()` — this file must exist before running. Required vars:

```
BOT_TOKEN=
OPENROUTER_API_KEY=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=5432
POSTGRES_PORT_HOST=5434   # external port when using Docker
```

`compose.local.yaml` defines `bot`, `bot_database`, and `pgadmin` on an external `db_network`. The compose file is incomplete (bot build and DB image are placeholders).

## Commands & Scripts

```bash
uv sync                  # Install dependencies from uv.lock
uv run python main.py    # Run the bot
uv run ruff check .      # Lint
uv run ruff format .     # Format
```

## Git Workflow
- Always create a feature branch before making changes
- Branch naming: feature/description or fix/description  
- Commit messages must be descriptive and concise
- Never push directly to main
- Always run `uv run ruff check .` before committing