-- EXECUTE THIS FILE TO CREATE PKMN.DB TABLES
-- RUN BASH COMMAND : sqlite3 2_Data/users.db < 1_Databases_Building/users/create_users_table.sql

CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    hashed_password TEXT
);

CREATE TABLE IF NOT EXISTS Tokens (
    username TEXT PRIMARY KEY,
    token TEXT
);