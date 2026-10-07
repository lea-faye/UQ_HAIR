from jinja2 import Environment, FileSystemLoader
from helpers import sql_fetch


# When a purchase is made, the details will be emailed to the client
def email_receipt(purchase_id):
    e = Environment(loader=FileSystemLoader("templates"))
    template = e.get_template("receipt.html")

    # Client name and email, Product name,
    # Purchase quantity, total_price, date and time
    sql = """
    SELECT client.name AS c_name, email, product.name AS p_name,
    quantity, total_price, date, time
    FROM purchase
    JOIN client ON purchase.client_id = client.client_id
    JOIN product ON purchase.product_id = product.product_id
    WHERE purchase_id = ?;
    """

    receipt_data = sql_fetch(sql, purchase_id)
    email = receipt_data[0]["email"]

    output = template.render(purchase=receipt_data[0])
    with open(f"emails/purchase_{purchase_id}.html", "w") as f:
        f.write(output)
        print(f"Sending email to {email}")


# Appointments on a certain date will be emailed to the client
def email_appointment(date):
    e = Environment(loader=FileSystemLoader("templates"))
    template = e.get_template("appointments.html")


# CLient name and email
# Appointment date, time and staff member name
sql = """
SELECT client.name AS c_name, email, date, time, staff.name AS s_name
FROM appointment
JOIN client ON appointment.client_id = client.client_id
JOIN staff ON appointment.staff_id = staff.staff_id
WHERE date = ?
"""

appointment_data = sql_fetch(sql, date)
email = receipt_data[0]["email"]

output = template.render(appointment=receipt_data[0])
with open(f"email/appointment_{appointment_id}.html", "w") as f:
    f.write(output)
    print(f"Sending email to {email}")

email_appointment(2026-04-07)

# Details about the items with the listed ids will be put in an advertising email to send to all


def email_advert(item_ids):
    e = Environment(loader=FileSystemLoader("templates"))
    template = e.get_template("advert.html")
