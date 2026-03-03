CREATE DATABASE telegram_bot_db;

\c telegram_bot_db

DROP TABLE IF EXISTS jobs CASCADE;
DROP TABLE IF EXISTS link_stats CASCADE;
DROP TABLE IF EXISTS games CASCADE;
DROP TABLE IF EXISTS users CASCADE;


CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL,
    username    VARCHAR(100) NOT NULL
);

CREATE TABLE jobs (
    id        SERIAL PRIMARY KEY,
    title     TEXT NOT NULL,
    url       TEXT UNIQUE NOT NULL,
    source    VARCHAR(50) NOT NULL DEFAULT 'djinni',
    posted_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE games (
    id          SERIAL PRIMARY KEY,
    chat_id     BIGINT NOT NULL,
    mode        VARCHAR(3) NOT NULL,
    player_x_id BIGINT NOT NULL,
    player_o_id BIGINT,
    winner_id   BIGINT,
    created_at  TIMESTAMPTZ DEFAULT now(),
    finished_at TIMESTAMPTZ
);

CREATE TABLE link_stats (
    id        SERIAL PRIMARY KEY,
    user_id   BIGINT NOT NULL,
    username  VARCHAR(100),
    link_type VARCHAR(20) NOT NULL,
    sent_at   TIMESTAMPTZ DEFAULT now()
);
