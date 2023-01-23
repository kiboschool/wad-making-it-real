# Product Interface
import sqlite3

conn = sqlite3.connect('products.db')
conn.row_factory = sqlite3.Row

def select_all_products():
    cur = conn.execute("SELECT * FROM products")
    return cur.fetchall()

def select_product_by_id(_id):
    cur = conn.execute("SELECT * FROM products WHERE id = ?", [_id])
    return cur.fetchone()

def products_cheaper_than(price):
    cur = conn.execute("SELECT * FROM products WHERE price < ?", [price])
    return cur.fetchall()

def add_product(name, price, quantity):
    product = {'name': name, 'price': price, 'quantity': quantity}
    conn.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?);", [name, price, quantity]) 
    conn.commit()
    return product

def product_details(product):
    return f"{product['name']}: ${product['price']}. {product['quantity']} left in stock"

def product_overview(product):
    return f"{product['id']}    {product['name']}"
