from helpers import sql_commit, sql_fetch

def create_staff():
    create_sql = """
    INSERT INTO staff (name, phone, email, pay_rate, bank_acc)
    VALUES (?, ?, ?, ?, ?)
    """
    
    name = input("Enter staff name: ")
    phone = input("Enter phone number: ")
    while not valid_phone(phone):
        phone = input("Phone Number not valid, enter again: ")
    email = input("Enter email address: ")
    while not valid_email(email):
        email = input("Email must have @, enter again: ")
    pay_rate = input("Enter pay rate in $/hr: ")
    while not valid_pay(pay_rate):
        pay_rate = input("Please enter a valid payrate: ")
    bank_acc = input("Enter BSB and account number: ")
    
    sql_commit(create_sql, (name, phone, email, pay_rate, bank_acc))
    print("Successfully created new staff member")
    
    return None

    
def read_staff():
    read_sql = """
    SELECT *
    FROM staff
    """
    
    all_staff = sql_fetch(read_sql)
    for staff_member in all_staff:
        print(f"ID: {staff_member["staff_id"]:2} | Name: {staff_member["name"]:15} | Phone:  {staff_member["phone"]:15} | Email: {staff_member["email"]:30} | Pay Rate: ${staff_member["pay_rate"]:8.2f}/hr | Bank Account: {staff_member["bank_acc"]}")
    

def update_staff(): 
    staff_id = int(input("Enter the staff number of the staff you wish to update: "))
    read_sql = """
    SELECT *
    FROM staff
    WHERE staff_id = ?
    """
    updating_staff = sql_fetch(read_sql, (staff_id))[0]
    
    update_menu = f"""
--- UPDATING STAFF MEMBER: '{updating_staff['name']}' ----

Current Details for {updating_staff['name']}:
    Phone:        {updating_staff['phone']}
    Email:        {updating_staff['email']}
    Pay Rate:     {updating_staff['pay_rate']}
    Bank Details: {updating_staff['bank_acc']}

-- UPDATE OPTIONS --
(1) Change Name
(2) Change Phone Number
(3) Change Email
(4) Change Pay Rate
(5) Change Bank Details
(6) Exit
    """
    
    while True:
        selection = input(f"""
    {update_menu}      
Select an option: """)
        match selection:
            case "1":
                change = input("Enter updated name: ")
                sql_commit("UPDATE staff SET name = ? WHERE staff_id = ?", (change, staff_id))
            case "2":
                change = input("Enter updated phone number: ")
                while not valid_phone(change):
                    change = input("Phone Number not valid, enter again: ")
                sql_commit("UPDATE staff SET phone = ? WHERE staff_id = ?", (change, staff_id))
            case "3":
                change = input("Enter updated email: ")
                while not valid_email(change):
                    change = input("Email must have @, enter again: ")
                sql_commit("UPDATE staff SET email = ? WHERE staff_id = ?", (change, staff_id))
            case "4":
                change = input("Enter updated pay rate in $/hr: ")
                while not valid_pay(change):
                    change = input("Please enter valid payrate in $/hr: ")
                sql_commit("UPDATE staff SET pay_rate = ? WHERE staff_id = ?", (change, staff_id))
            case "5":
                change = input("Enter updated BSB and account number: ")
                sql_commit("UPDATE staff SET bank_acc = ? WHERE staff_id = ?", (change, staff_id))
            case "6":
                break
            case _:
                print("Unknown Option. Please select valid option")
    print(f"{updating_staff['name']}'s profile has been updated")

def delete_staff():
    staff_id = input("Enter staff id of member you wish to delete: ")
    
    read_sql = """
        SELECT *
        FROM staff
        WHERE staff_id = ?
        """
    deleted_staff = sql_fetch(read_sql, (staff_id))[0]

    delete_sql = """
    DELETE FROM staff
    WHERE staff_id = ?
    """
    
    sql_commit(delete_sql, (staff_id))
    print(f"Deleted staff member '{deleted_staff['name']}'")

# Data Validation

def valid_email(email):
    if email.count("@") == 1:
        return True
    else:
        return False
    
def valid_phone(phone):
    if len(phone) >= 8 and len(phone) <= 15:
        if phone[0] == "+":
            phone = phone[1:]
        if phone.isdecimal():
            return True
        else:
            return False
    else:
        return False

def valid_pay(pay_rate):
    try:
        float(pay_rate)
        if float(pay_rate) > 0:
            return True
        else:
            return False
    except ValueError:
        return False