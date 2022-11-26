DELETE FROM means_of_payments
WHERE (
    (name = 'cash')
    OR (name = 'credit_card')
    OR (name = 'debit_card')
    OR (name = 'checks')
    OR (name = 'electronic_funds_transfers')
);