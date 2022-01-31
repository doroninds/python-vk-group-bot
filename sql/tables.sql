CREATE TABLE IF NOT EXISTS commands (
    name STRING PRIMARY KEY,
    action_type TINYINT NOT NULL,
    help STRING
);

CREATE TABLE IF NOT EXISTS contents (
    key STRING,
    text STRING,
    attachment STRING,
    created_at datetime,
    updated_at datetime
);

CREATE TABLE IF NOT EXISTS admins (
    user_id INT PRIMARY KEY,
    group_id INT,
    created_at datetime,
    updated_at datetime
);


ALTER TABLE commands ADD admin_only BOOLEAN NOT NULL DEFAULT false;
ALTER TABLE commands ADD text STRING;
ALTER TABLE commands ADD attachment STRING;
ALTER TABLE commands ADD id INT;
ALTER TABLE contents ADD command_id INT NOT NULL DEFAULT 0;
ALTER TABLE commands ADD custom_key STRING;