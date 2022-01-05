CREATE TABLE IF NOT EXISTS commands (
    name STRING PRIMARY KEY,
    action_type TINYINT NOT NULL,
    help STRING
);

CREATE TABLE IF NOT EXISTS contents (
    key STRING,
    action_type TINYINT NOT NULL,
    text STRING,
    attachment STRING,
    created_at datetime,
    updated_at datetime
);