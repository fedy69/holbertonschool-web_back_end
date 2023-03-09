-- Creates a table called users
--If the table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);