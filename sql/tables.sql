CREATE TABLE IF NOT EXISTS commands (
    id INT AUTOINCREMENT,
    name STRING PRIMARY KEY,
    action_type TINYINT NOT NULL,
    help STRING,
    admin_only BOOLEAN NOT NULL DEFAULT false,
    text STRING,
    attachment STRING,
    custom_key STRING
);

CREATE TABLE IF NOT EXISTS contents (
    key STRING,
    command_id INT NOT NULL DEFAULT 0,
    text STRING,
    attachment STRING,
    created_at datetime DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS admins (
    user_id INT PRIMARY KEY,
    group_id INT,
    created_at datetime,
    updated_at datetime
);

