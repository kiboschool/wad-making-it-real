# Product Interface

mock_data = [
    {'id': 1, 'name': 'Product 1', 'price': 9.99, 'quantity': 10},
    {'id': 2, 'name': 'Product 2', 'price': 19.99, 'quantity': 5},
    {'id': 3, 'name': 'Product 3', 'price': 29.99, 'quantity': 2},
    {'id': 4, 'name': 'Product 4', 'price': 39.99, 'quantity': 8},
    {'id': 5, 'name': 'Product 5', 'price': 49.99, 'quantity': 15},
    {'id': 6, 'name': 'Product 6', 'price': 59.99, 'quantity': 20},
]

def select_all_products():
    return mock_data

def select_product_by_id(_id):
    return next(product for product in mock_data if product['id'] == _id)

def products_cheaper_than(price):
    return [product for product in mock_data if product['price'] < price]

def add_product(name, price, quantity):
    product = {'id': len(mock_data) + 1, 'name': name, 'price': price, 'quantity': quantity}
    mock_data.append(product)
    return product

def product_details(product):
    return f"{product['name']}: ${product['price']}. {product['quantity']} left in stock"

def product_overview(product):
    return f"{product['id']}    {product['name']}"
