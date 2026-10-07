from authentication import authenticate
from database import create_database
from staff import create_staff, read_staff, update_staff, delete_staff
from client import create_client, read_client, update_client, delete_client
from product import create_product, read_product, update_products, delete_products
from appointment import create_appointment, read_appointment, update_appointment, delete_appointment
from purchase import create_purchase, read_purchase, update_purchase, delete_purchase
from analysis import low_stock, count_appointments, highest_rate, count_purchases, product_sold, daily_appointments, discount
import os
 
 
 
# Main menu
main_menu = """
--- MAIN MENU ---

(1) Create / reset database
(2) Manage staff
(3) Manage clients
(4) Manage products
(5) Manage appointments
(6) Manage purchases
(7) Data analysis
(8) Send emails
(9) Exit

Enter your Option: """
 
 
# Manage staff menu
staff_menu = """
--- STAFF MENU ---

(1) Add new staff member
(2) View current staff
(3) Update existing staff
(4) Delete staff member
(5) Exit

Enter your Option: """
 
# Manage client menu
client_menu = """
--- CLIENT MENU ---

(1) Add new client
(2) View current clients
(3) Update existing client
(4) Delete client
(5) Exit

Enter your Option: """
 
 
# Manage product menu
product_menu = """
--- PRODUCT MENU ---

(1) Add new product
(2) View current products
(3) Update existing product
(4) Delete product
(5) Exit

Enter your Option: """
 
 
# Manage appointment menu
appointment_menu = """
--- APPOINTMENT MENU ---

(1) Add new appointment
(2) View upcoming appointments
(3) Update existing appointment
(4) Cancel appointment
(5) Exit

Enter your Option: """
 
 
# Manage purchase menu
purchase_menu = """
--- PRODUCT MENU ---

(1) Add new purchase
(2) View purchases
(3) Update existing purchase
(4) Delete purchase
(5) Exit

Enter your Option: """
 
 
# Data analysis menu
analysis_menu = """
--- DATA ANALYSIS MENU ---

(1) Low stock
(2) Appointment count
(3) Highest paid staff
(4) Purchase count
(5) Products sold
(6) Daily appointment count
(7) Discount percentage
(8) Exit

Enter your Option: """
 
 
# Authenticate user
logged_in = authenticate()
 
 
 
# Keep allowing attempts until correct
while not logged_in:
    print("Password incorrect")
    logged_in = authenticate()
 
 
 
# Successful login
print("Welcome to the UQ Hair Information System")
 
 
while logged_in:
    # Display the main menu and wait for user input
    main_choice = input(main_menu)
    match main_choice:
        case "1":
            print("Resetting the database")
            if os.path.exists("uqhair.db"):
                os.remove("uqhair.db")
            create_database()
        case "2":
            while True:
                staff_choice = input(staff_menu)
                match staff_choice:
                    case "1":
                        create_staff()
                    case "2":
                        read_staff()
                    case "3":
                        update_staff()
                    case "4":
                        delete_staff()
                    case "5":
                        break
                    case _:
                        print("Not a valid option.")
        case "3":
            while True:
                client_choice = input(client_menu)
                match client_choice:
                    case "1":
                        create_client()
                    case "2":
                        read_client()
                    case "3":
                        update_client()
                    case "4":
                        delete_client()
                    case "5":
                        break
                    case _:
                        print("Not a valid option.")
        case "4":
            while True:
                product_choice = input(product_menu)
                match product_choice:
                    case "1":
                        create_product()
                    case "2":
                        read_product()
                    case "3":
                        update_products()
                    case "4":
                        delete_products()
                    case "5":
                        break
                    case _:
                        print("Not a valid option.")
        case "5":
            while True:
                appointment_choice = input(appointment_menu)
                match appointment_choice:
                    case "1":
                        create_appointment()
                    case "2":
                        read_appointment()
                    case "3":
                        update_appointment()
                    case "4":
                        delete_appointment()
                    case "5":
                        break
                    case _:
                        print("Not a valid option.")
        case "6":
            while True:
                purchase_choice = input(purchase_menu)
                match purchase_choice:
                    case "1":
                        create_purchase()
                    case "2":
                        read_purchase()
                    case "3":
                        update_purchase()
                    case "4":
                        delete_purchase()
                    case "5":
                        break
                    case _:
                        print("Not a valid option.")
        case "7":
            while True:
                analysis_menu = input(analysis_menu)
                match analysis_menu:
                    case "1":
                        low_stock()
                    case "2":
                        count_appointments()
                    case "3":
                        highest_rate()
                    case "4":
                        count_purchases()
                    case "5":
                        product_sold()
                    case "6":
                        daily_appointments()
                    case "7":
                        discount()
                    case "8":
                        break
                    case _:
                        print("Not a valid option.")