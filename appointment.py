from helpers import sql_commit, sql_fetch
from datetime import datetime
 
 
def create_appointment():
    client_id = input("Enter client id: ")
    date = input("Enter date YYYY-MM-DD: ")
    appointments = sql_fetch("SELECT staff_id, time FROM appointment WHERE date = ?", date)
    for row in appointments:
        print(f"{row["staff_id"]} - {row["time"]}")
 
    staff_id = input("Enter staff id: ")
    time = input("Enter time in HH:MM: ")
 
    create_sql = """
    INSERT INTO appointment (client_id, staff_id, date, time)
    VALUES (?, ?, ?, ?)
    """
    sql_commit(create_sql, (client_id, staff_id, date, time))
 
 
def read_appointment():
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")
 
    # Return the appointment id, staff name, client name, date and time - for appointments that are today or greater
    read_sql = """
    SELECT appointment_id, staff.name AS staff_name, client.name AS client_name, date, time
    FROM appointment
    JOIN staff ON appointment.staff_id = staff.staff_id
    JOIN client ON appointment.client_id = client.client_id
    WHERE date >= ?
    """
 
    appointments = sql_fetch(read_sql, date)
    for row in appointments:
        print(f"ID: {row["appointment_id"]} Staff: {row["staff_name"]} Client: {row["client_name"]} Date: {row["date"]} Time: {row["time"]}")
 
 
 
def update_appointment():
    appointment_id = input("Enter id of appointment you wish to update: ")
 
    update_menu = """
    (1) Change client
    (2) Change staff
    (3) Change date
    (4) Change time
    (5) Exit
    """
 
    while True:
        choice = input(update_menu)
        match choice:
            case "1":
                client_id = input("Enter new client_id: ")
                sql_commit("UPDATE appointment SET client_id = ? WHERE appointment_id = ?", (client_id, appointment_id))
            case "2":
                staff_id = input("Enter a new staff_id: ")
                sql_commit("UPDATE appointment SET staff_id = ? WHERE appointment_id = ?", (staff_id, appointment_id))
            case "3":
                date = input("Enter a new date in YYYY-MM-DD: ")
                sql_commit("UPDATE appointment SET date = ? WHERE appointment_id = ?", (date, appointment_id))
            case "4":
                time = input("Enter a new time in HH:MM: ")
                sql_commit("UPDATE appointment SET time = ? WHERE appointment_id = ?", (time, appointment_id))
            case "5":
                break
            case _:
                print("Unknown option. Pick from menu")
    print("Appointment updated")
    return None
 
 
def delete_appointment():
    delete_sql = """
    DELETE FROM appointment
    WHERE appointment_id = ?
    """
    appointment_id = input("Enter id of appointment you wish to cancel: ")    
    sql_commit(delete_sql, appointment_id)
 
    return None
 
 
# In the format YYYY-MM-DD
def valid_date(date):
    pass
 
 
# In the format HH:MM
def valid_time(time):
    pass