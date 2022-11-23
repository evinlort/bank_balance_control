CREATE TABLE IF NOT EXISTS families (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS languages (
    id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS genders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    gender_id INTEGER,
    day_of_birth DATE,
    password_hash text DEFAULT NULL,
    language_id SMALLINT DEFAULT NULL,
    family_id SMALLINT DEFAULT NULL,

    CONSTRAINT FK_users_families_1 FOREIGN KEY(family_id) REFERENCES families(id),
    CONSTRAINT FK_users_languages_1 FOREIGN KEY(language_id) REFERENCES languages(id),
    CONSTRAINT FK_users_genders_1 FOREIGN KEY(gender_id) REFERENCES genders(id)
);

