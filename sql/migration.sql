-- commands definition
CREATE TABLE "commands" (
    name STRING PRIMARY KEY,
    action_type TINYINT NOT NULL,
    help STRING,
    admin_only BOOLEAN NOT NULL DEFAULT false,
    text STRING,
    attachment STRING,
    "id" INTEGER,
    custom_key STRING,
    "bind_id" INTEGER
);
-- contents definition
CREATE TABLE "contents" (
    key STRING,
    text STRING,
    attachment STRING,
    created_at datetime,
    updated_at datetime,
    command_id INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE "users" (
    id INTEGER PRIMARY KEY NOT NULL,
    group_id INTEGER,
    is_admin BOOLEAN NOT NULL DEFAULT false
);

CREATE TABLE "warnings" (
    user_id INTEGER NOT NULL,
    group_id INTEGER,
    reason STRING,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expired_at datetime
);