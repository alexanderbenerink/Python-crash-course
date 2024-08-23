CREATE TABLE IF NOT EXISTS rekeningen_TimBolhoeve (
    id SERIAL PRIMARY KEY,
    rekeninghouder text NOT NULL,
    rekeningnummer text NOT NULL,
    saldo real
);