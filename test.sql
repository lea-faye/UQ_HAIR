CREATE TABLE
    IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT NOT NULL
    );

INSERT INTO
    users (username, email)
VALUES
    ("burnt_salami", "adam@gmail.com");