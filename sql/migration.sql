-- commands definition

CREATE TABLE "commands" (name STRING PRIMARY KEY, action_type TINYINT NOT NULL, help STRING, admin_only BOOLEAN NOT NULL DEFAULT false, text STRING, attachment STRING, "id" INTEGER, custom_key STRING, "bind_id" INTEGER, success STRING, "fail" STRING, sort INTEGER DEFAULT 0 NOT NULL, icon VARCHAR);
-- contents definition

CREATE TABLE "contents" (key STRING, text STRING, attachment STRING, created_at datetime, updated_at datetime, command_id INTEGER DEFAULT 0 NOT NULL);

-- users definition

CREATE TABLE "users" (
    id INTEGER PRIMARY KEY NOT NULL,
    group_id INTEGER,
    level TINYINT NOT NULL DEFAULT 0
);

-- warnings definition

CREATE TABLE "warnings" (
    user_id INTEGER NOT NULL,
    group_id INTEGER,
    reason STRING,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expired_at datetime
);

CREATE TABLE "bans" (
    user_id INTEGER NOT NULL,
    group_id INTEGER,
    reason STRING,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);