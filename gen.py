import sqlite3
from faker import Faker
fake = Faker()

conn = sqlite3.connect("products.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, quantity INTEGER);")

for i in range(200):
    cur.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?);", 
        (fake.bs(),
        fake.random_number(digits=3),
        fake.random_number(digits=2)
        )
    )

conn.commit()

