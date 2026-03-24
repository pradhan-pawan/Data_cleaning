import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sales_analysis", "sales.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items;

CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER
);

CREATE TABLE sales (
    sales_id INTEGER PRIMARY KEY,
    customer_id INTEGER
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    sales_id INTEGER,
    item_id INTEGER,
    quantity INTEGER
);
""")


cursor.executemany("INSERT INTO customer VALUES (?, ?)", [
    (1, 21), (2, 23), (3, 35)
])

cursor.executemany("INSERT INTO sales VALUES (?, ?)", [
    (1, 1), (2, 1), (3, 2), (4, 3), (5, 3)
])

cursor.executemany("INSERT INTO items VALUES (?, ?)", [
    (1, 'x'), (2, 'y'), (3, 'z')
])

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", [
    (1, 1, 1, 5),
    (2, 2, 1, 5),
    (3, 3, 1, 1),
    (4, 3, 2, 1),
    (5, 3, 3, 1),
    (6, 4, 3, 1),
    (7, 5, 3, 1)
])

conn.commit()
conn.close()

print("Database created at:", db_path)