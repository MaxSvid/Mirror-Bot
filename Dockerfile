# recommend to use docker ai CLI and light py version

FROM python:3.13-slim AS base

LABEL maintainer="Team DeFi Mirror: Max(https://t.me/mak_sjr) and Dmitriy(https://t.me/)"
LABEL author="mak_sjr"
LABEL version="1.0"
LABEL description="Official Mirror Website for DeFi Projects and Education Resources"

# Create non-root user

# Set working dir to the app folder
# In Linux it start with /home
WORKDIR /home/docker_user/app

# Python settings

# Copy and install dependencies
# This file depends on docker-compose to copy uv.lock

# Copy the project

# Host start
CMD []