from helpers import sql_fetch, sql_commit
from datetime import datetime
 
 
def create_purchase():
    client_id = input("Enter client id: ")
    
    product_results = sql_fetch("SELECT * FROM product;")
    for product in product_results:
        print(f"ID: {product["product_id"]} Name: {product["name"]} Price: ${product["price"]} Stock: {product["stock"]}")
    
    product_id = input("Which product is being purchased?: ")
 
 
    purchased_product = sql_fetch("SELECT * FROM product WHERE product_id = ?;", product_id)
    quantity = input("How many do you wish to purchase?: ")
 
 
    while not valid_quantity(int(purchased_product[0]["stock"]), quantity):
        quantity = input("How many do you wish to purchase?: ")
    quantity = int(quantity)
 
 
    client = sql_fetch("SELECT discount FROM client WHERE client_id = ?;", client_id)
 
 
    if str(client[0]["discount"]) == "1":
        discount = 0.9
    else:
        discount = 1
 
 
    total_price = float(purchased_product[0]["price"]) * quantity * discount
 
 
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")
    time = today.strftime("%H:%M:%S")
 
 
    create_sql = """
    INSERT INTO purchase (product_id, client_id, quantity, total_price, date, time)
    VALUES (?, ?, ?, ?, ?, ?);
    """
 
 
    sql_commit(create_sql, (product_id, client_id, quantity, total_price, date, time))
 
 
    new_stock = purchased_product[0]["stock"] - quantity
    update_sql = """
    UPDATE product SET stock = ? WHERE product_id = ?;
    """
 
 
    sql_commit(update_sql, (new_stock, product_id))
 
 
    return None
 
 
 
def read_purchase():
 
 
    date = input("How far back do you want to see receipts?: ")
 
 
    read_sql = """
    SELECT purchase_id, product.name AS p_name, client.name AS c_name, quantity, total_price, date, time
    FROM purchase 
    JOIN product ON purchase.product_id = product.product_id
    JOIN client ON purchase.client_id = client.client_id
    WHERE date >= ?;
    """
 
 
    receipts = sql_fetch(read_sql, date)
 
 
    for receipt in receipts:
        print(f"Purchase ID: {receipt["purchase_id"]} Client: {receipt["c_name"]} Product: {receipt["p_name"]} Quantity: {receipt["quantity"]} Total Price: ${receipt["total_price"]} Date & Time: {receipt["date"]} - {receipt["time"]}")
 
 
    return None
 
 
 
def update_purchase():
    purchase_id = input("Enter id of purchase you want to update: ")
 
 
    update_menu = """
    (1) Change product
    (2) Change client
    (3) Change quantity
    (4) Change total price
    (5) Change date
    (6) Change time
    (7) Exit
    """
 
 
    while True:
        update_choice = input(update_menu)
        match update_choice:
            case "1":
                product_id = input("Enter a new product_id: ")
                sql_commit("UPDATE purchase SET product_id = ? WHERE purchase_id = ?;", (product_id, purchase_id))
            case "2":
                client_id = input("Enter a new client_id: ")
                sql_commit("UPDATE purchase SET client_id = ? WHERE purchase_id = ?;", (client_id, purchase_id))
            case "3":
                quantity = input("Enter a new quantity: ")
                sql_commit("UPDATE purchase SET quantity = ? WHERE purchase_id = ?;", (quantity, purchase_id))
            case "4":
                total_price = input("Enter a new total price: ")
                sql_commit("UPDATE purchase SET total_price = ? WHERE purchase_id = ?;", (total_price, purchase_id))
            case "5":
                date = input("Enter a new date: ")
                sql_commit("UPDATE purchase SET date = ? WHERE purchase_id = ?;", (date, purchase_id))
            case "6":
                time = input("Enter a new time: ")
                sql_commit("UPDATE purchase SET time = ? WHERE purchase_id = ?;", (time, purchase_id))
            case "7":
                break
            case _: 
                print("Not a valid option, pick from menu")
    return None
 
 
from helpers import sql_fetch, sql_commit
from datetime import datetime
 
 
def create_purchase():
    client_id = input("Enter client id: ")
 
    product_results = sql_fetch("SELECT * FROM product;")
    for product in product_results:
        print(f"ID: {product["product_id"]} Name: {product["name"]} Price: ${product["price"]} Stock: {product["stock"]}")
    
    product_id = input("Which product is being purchased?: ")
 
    purchased_product = sql_fetch("SELECT * FROM product WHERE product_id = ?;", product_id)
    quantity = input("How many do you wish to purchase?: ")
 
    while not valid_quantity(int(purchased_product[0]["stock"]), quantity):
        quantity = input("How many do you wish to purchase?: ")
    quantity = int(quantity)
 
    client = sql_fetch("SELECT discount FROM client WHERE client_id = ?;", client_id)
 
    if str(client[0]["discount"]) == "1":
        discount = 0.9
    else:
        discount = 1
 
    total_price = float(purchased_product[0]["price"]) * quantity * discount
 
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")
    time = today.strftime("%H:%M:%S")
 
    create_sql = """
    INSERT INTO purchase (product_id, client_id, quantity, total_price, date, time)
    VALUES (?, ?, ?, ?, ?, ?);
    """
 
    sql_commit(create_sql, (product_id, client_id, quantity, total_price, date, time))
 
    new_stock = purchased_product[0]["stock"] - quantity
    update_sql = """
    UPDATE product SET stock = ? WHERE product_id = ?;
    """
 
    sql_commit(update_sql, (new_stock, product_id))
 
    return None
 
 
def read_purchase():
    date = input("How far back do you want to see receipts?: ")
 
    read_sql = """
    SELECT purchase_id, product.name AS p_name, client.name AS c_name, quantity, total_price, date, time
    FROM purchase 
    JOIN product ON purchase.product_id = product.product_id
    JOIN client ON purchase.client_id = client.client_id
    WHERE date >= ?;
    """
    receipts = sql_fetch(read_sql, date)
    for receipt in receipts:
        print(f"Purchase ID: {receipt["purchase_id"]} Client: {receipt["c_name"]} Product: {receipt["p_name"]} Quantity: {receipt["quantity"]} Total Price: ${receipt["total_price"]} Date & Time: {receipt["date"]} - {receipt["time"]}")
    return None
 
 
def update_purchase():
    purchase_id = input("Enter id of purchase you want to update: ")
    update_menu = """
    (1) Change product
    (2) Change client
    (3) Change quantity
    (4) Change total price
    (5) Change date
    (6) Change time
    (7) Exit
    """
 
    while True:
        update_choice = input(update_menu)
        match update_choice:
            case "1":
                product_id = input("Enter a new product_id: ")
                sql_commit("UPDATE purchase SET product_id = ? WHERE product_id = ?;", (product_id, product_id))
            case "2":
                client_id = input("Enter a new client_id: ")
                sql_commit("UPDATE purchase SET client_id = ? WHERE product_id = ?;", (client_id, product_id))
            case "3":
                quantity = input("Enter a new quantity: ")
                sql_commit("UPDATE purchase SET quantity = ? WHERE product_id = ?;", (quantity, product_id))
            case "4":
                total_price = input("Enter a new total price: ")
                sql_commit("UPDATE purchase SET total_price = ? WHERE product_id = ?;", (total_price, product_id))
            case "5":
                date = input("Enter a new date: ")
                sql_commit("UPDATE purchase SET date = ? WHERE product_id = ?;", (date, product_id))
            case "6":
                time = input("Enter a new time: ")
                sql_commit("UPDATE purchase SET time = ? WHERE product_id = ?;", (time, product_id))
            case "7":
                break
            case _: 
                print("Not a valid option, pick from menu")
    return None
 
 
def delete_purchase():
    delete_sql = """
    DELETE FROM purchase
    WHERE purchase_id = ?;
    """
    purchase_id = input("Enter purchase id to delete: ")
    sql_commit(delete_sql, purchase_id)
 
    return None
 
 
# Data validation functions
def valid_quantity(stock, quantity):
    try:
        # Quantity must be an integer
        quantity = int(quantity)
 
        # Quantity must be less than or equal to stock
        return quantity <= stock
 
    except ValueError:
        print("Quantity must be an integer")
        return False
def delete_purchase():
    delete_sql = """
    DELETE FROM purchase
    WHERE purchase_id = ?;
    """
    purchase_id = input("Enter purchase id to delete: ")
    sql_commit(delete_sql, purchase_id)
    return None
 
 
# Data validation functions
def valid_quantity(stock, quantity):
    try:
        # Quantity must be an integer
        quantity = int(quantity)
 
        # Quantity must be less than or equal to stock
        return quantity <= stock
 
    except ValueError:
        print("Quantity must be an integer")
        return False 