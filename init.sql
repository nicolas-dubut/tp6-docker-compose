CREATE TABLE IF NOT EXISTS products (
   id SERIAL PRIMARY KEY,
   name TEXT NOT NULL,
   price NUMERIC NOT NULL
);
INSERT INTO products (name, price) VALUES ('Livre', 19.99), ('Stylo', 2.49), ('Fixe', 4.50);

