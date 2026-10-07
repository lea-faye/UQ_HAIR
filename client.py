from helpers import sql_commit, sql_fetch
from staff import valid_email, valid_phone

def create_client():
    create_sql = """
    INSERT INTO client (name, phone, email, discount)
    VALUES (?, ?, ?, ?)
    """
    
    name = input("Enter client name: ")
    phone = input("Enter phone number: ")
    while not valid_phone(phone):
        phone = input("Phone Number not valid, enter again: ")
    email = input("Enter email address: ")
    while not valid_email(email):
        email = input("Email must have @, enter again: ")
    discount = input("Does this client get a discount? 0 for No, 1 for Yes: ")
    while not valid_discount(discount):
        discount = input("Please enter 0 for No and 1 for Yes")
    sql_commit(create_sql, (name, phone, email, int(discount)))
    print("Successfully created a new client")
        
    return None

def read_client():
    read_sql = """
    SELECT *
    FROM client
    """
    
    all_clients = sql_fetch(read_sql)
    
    for client in all_clients:
        if str(client["discount"]) == "0":
            discount = "No"
        else:
            discount = "Yes"
        print(f"ID: {client["client_id"]}, Name: {client["name"]} Phone:  {client["phone"]}, Email: {client["email"]}, Discount: {discount}")

def update_client():
    client_id = int(input("Enter the client number of the client you wish to update: "))
    read_sql = """
    SELECT *
    FROM staff
    WHERE staff_id = ?
    """
    updating_client = sql_fetch(read_sql, (client_id))[0]
    if str(updating_client["discount"]) == "0":
        discount = "No"
    else:
        discount = "Yes"
    update_menu = f"""
--- UPDATING STAFF MEMBER: '{updating_client['name']}' ----

Current Details for {updating_client['name']}:
    Phone:        {updating_client['phone']}
    Email:        {updating_client['email']}
    Discount:     {discount}

-- UPDATE OPTIONS --
(1) Change Name
(2) Change Phone Number
(3) Change Email
(4) Change Discount
(5) Exit
    """
    
    while True:
        selection = input(f"""
    {update_menu}      
    Select an option: """)
        match selection:
            case "1":
                change = input("Enter updated name: ")
                sql_commit("UPDATE client SET name = ? WHERE client_id = ?", (change, client_id))
            case "2":
                change = input("Enter updated phone number: ")
                while not valid_phone(change):
                    change = input("Phone Number not valid, enter again: ")
                sql_commit("UPDATE client SET phone = ? WHERE client_id = ?", (change, client_id))
            case "3":
                change = input("Enter updated email: ")
                while not valid_email(change):
                    change = input("Email must have @, enter again: ")
                sql_commit("UPDATE client SET email = ? WHERE client_id = ?", (change, client_id))
            case "4":
                change = input("Enter updated discount status: 0 = No, 1 = Yes ")
                while not valid_discount(change):
                    change = input("Enter 0 for No or 1 for Yes")
                sql_commit("UPDATE client SET discount = ? WHERE client_id = ?", (change, client_id))
            case "5":
                break
            case _:
                print("Unknown Option. Please select valid option")
    print(f"{updating_client['name']} has been updated")
        

def delete_client():
    client_id = input("Enter client id of member you wish to delete: ")

    read_sql = """
    SELECT *
    FROM staff
    WHERE staff_id = ?
    """
    deleting_client = sql_fetch(read_sql, (client_id))[0]  
    
    delete_sql = """
    DELETE FROM client
    WHERE client_id = ?
    """
        
    sql_commit(delete_sql, (client_id))
    print(f"Deleted Client: '{deleting_client['name']}'")
    
def valid_discount(discount):
    if discount in ["0", "1"]:
        return True
    else:
        return False