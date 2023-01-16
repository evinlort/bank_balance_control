CREATE TABLE IF NOT EXISTS history_of_balances (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    category_id INTEGER NOT NULL,
    previous_balance NUMERIC NOT NULL,

    CONSTRAINT FK_history_of_balance_1 FOREIGN KEY(category_id) REFERENCES categories(id)
);