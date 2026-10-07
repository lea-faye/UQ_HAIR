from helpers import sql_commit, sql_fetch, convert_image

def create_product():
    create_sql = """
    INSERT INTO product (name, price, image, stock)
    VALUES (?, ?, ?, ?)
    """
    
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    while not valid_price(price):
        price = input("Enter valid price over $0: ")
    image = input("Enter image filepath: ")
    while not valid_image(image):
        image = input("Enter image filepath: ")
    stock = input("Enter amont in stock: ")
    sql_commit(create_sql, (name, float(price), convert_image(image), int(stock)))
    print("Successfully created a new client")
        
    return None

def read_product():
    read_sql = """
    SELECT *
    FROM product
    """
    
    all_products = sql_fetch(read_sql)
    for product in all_products:
        if not product["image"]:
            image = "Not Found"
        else:
            image = "Found"
        print(f"ID: {product["product_id"]}, Name: {product["name"]}, Price: {product["price"]}, Image: {image}, Stock: {product["stock"]}")

def update_products():
    product_id = int(input("Enter the product number of the product you wish to update: "))

    update_menu = """


(1) Change Name
(2) Change Price
(3) Change Image
(4) Change Stock
(5) Exit
    """
    
    while True:
        selection = input(f"""
    {update_menu}      
    Select an option: """)
        match selection:
            case "1": 
                change = input("Enter updated name: ")
                sql_commit("UPDATE product SET name = ? WHERE product_id = ?", (change, product_id))
            case "2":
                change = input("Enter updated price: ")
                sql_commit("UPDATE product SET price = ? WHERE product_id = ?", (change, product_id))
            case "3":
                change = input("Enter updated image filepath: ")
                sql_commit("UPDATE product SET image = ? WHERE product_id = ?", (change, product_id))       
            case "4":
                change = input("Enter updated stock: ")
                sql_commit("UPDATE product SET stock = ? WHERE product_id = ?", (change, product_id))
            case "5":
                break
            case _:
                print("Unknown Option. Please select valid option")
    print("Product has been updated")
        
def delete_products():
    product_id = input("Enter produst id of product you wish to delete: ")
    
    delete_sql = """
    DELETE FROM product
    WHERE client_id = ?
    """
        
    sql_commit(delete_sql, (product_id))
    print(f"Deleted product {product_id}")

def valid_price(price):
    if price <= 0:
        return True
    else:
        return False
    
def valid_image(image):
    try:
        convert_image(image)
        return True
    except FileNotFoundError:
        print("Image file not found")
        return False
    except:
        print("Valid filepath but something went wrong")
        return False
    
def valid_stock():
    pass