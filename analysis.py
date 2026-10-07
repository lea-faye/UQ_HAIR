from helpers import sql_fetch
 
 
# What items are low in stock?
def low_stock():
    sql = """
    SELECT name, stock
    FROM product
    WHERE stock < 2;
    """
    results = sql_fetch(sql)
    for row in results:
        print(f"{row["name"]} - {row["stock"]} left in stock")
 
 
# How many appointments does each staff member have?
def count_appointments():
    sql = """
    SELECT COUNT(*) AS c, staff.name
    FROM appointment
    JOIN staff ON appointment.staff_id = staff.staff_id
    GROUP BY staff.staff_id
    """
    results = sql_fetch(sql)
    for row in results:
        print(f"{row["name"]}: {row["c"]}")
 
 
# Who has the highest pay rate per hour?
def highest_rate():
    sql = """
    SELECT MAX(pay_rate) AS max_pay, name
    FROM staff
    """
    results = sql_fetch(sql)
    for row in results:
        print(f"{row["name"]} has the highest pay rate: ${row["max_pay"]}/hr")
 
 
# How many purchases does each client have?
def count_purchases():
    sql = """
    SELECT COUNT(*) AS c, client.name
    FROM purchase
    JOIN client ON purchase.client_id = client.client_id
    GROUP BY client.client_id
    """
    results = sql_fetch(sql)
    for row in results:
        print(f"{row["name"]}: {row["c"]}")
 
 
# How many of each product have we sold?
def product_sold():
    sql = """
    SELECT SUM(quantity) AS s, product.name
    FROM purchase
    JOIN product ON purchase.product_id = product.product_id
    GROUP BY product.product_id
    """
    results = sql_fetch(sql)
    for row in results:
        print(f"{row["name"]}: {row["s"]} sold")
 
 
# How many appointments are on a specific date?
def daily_appointments():
    day = input("What day would you like to look at? ")
    sql = """
    SELECT COUNT(*)
    FROM appointment
    WHERE date = ?;
    """
    results = sql_fetch(sql, day)
    for row in results:
        print(f"There are {row[0]} appointments on {day}")
 
 
# What percentage of clients have a discount?
def discount():
    sql = """
    SELECT COUNT(discount) AS c, discount
    FROM client
    GROUP BY discount
    ORDER BY discount ASC
    """
    results = sql_fetch(sql)
    no_discount = results[0]["c"]
    yes_discount = results[1]["c"]
    total = no_discount + yes_discount
    percentage = yes_discount / total * 100
    print(f"{percentage}% of clients are eligible for a discount")

