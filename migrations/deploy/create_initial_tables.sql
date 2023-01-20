CREATE TABLE IF NOT EXISTS families (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS languages (
    id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS genders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS means_of_payments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    display_name VARCHAR(50) NOT NULL,
    allow_payments BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(70) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    gender_id INTEGER,
    day_of_birth DATE,
    password_hash text DEFAULT NULL,
    language_id INTEGER DEFAULT NULL,
    family_id INTEGER DEFAULT NULL,

    CONSTRAINT FK_users_families_1 FOREIGN KEY(family_id) REFERENCES families(id),
    CONSTRAINT FK_users_languages_1 FOREIGN KEY(language_id) REFERENCES languages(id),
    CONSTRAINT FK_users_genders_1 FOREIGN KEY(gender_id) REFERENCES genders(id)
);


CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    family_id SMALLINT NOT NULL,
    name VARCHAR(255) NOT NULL UNIQUE,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT FK_categories_families_1 FOREIGN KEY(family_id) REFERENCES families(id)
);

CREATE TABLE IF NOT EXISTS purchases (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sum NUMERIC NOT NULL,
    means_of_payment_id INTEGER NOT NULL,
    comment TEXT,
    number_of_payments SMALLINT NOT NULL DEFAULT 1,
    category_id INTEGER NOT NULL,
    payment_number SMALLINT NOT NULL DEFAULT 1,

    CONSTRAINT FK_purchases_users_1 FOREIGN KEY(user_id) REFERENCES users(id),
    CONSTRAINT FK_purchases_means_of_payments_1 FOREIGN KEY(means_of_payment_id) REFERENCES means_of_payments(id),
    CONSTRAINT FK_purchases_categories_1 FOREIGN KEY(category_id) REFERENCES categories(id)
);