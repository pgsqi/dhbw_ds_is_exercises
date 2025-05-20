from faker import Faker
import random

fake = Faker()

with open("init.sql", "w") as f:
    f.write("""
    CREATE TABLE customers (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        iban TEXT
    );
    """)

    for _ in range(1000):
        name = fake.name().replace("'", "")
        email = fake.email()
        iban = fake.iban()
        f.write(f"INSERT INTO customers (name, email, iban) VALUES ('{name}', '{email}', '{iban}');\n")
