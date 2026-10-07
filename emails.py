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
 
 
# Details about the items with the listed ids will be put in an advertising email to send to all
def email_advert(item_ids):
    e = Environment(loader=FileSystemLoader("templates"))
    template = e.get_template("advert.html")