from helpers import sql_commit

create_staff = """
CREATE TABLE IF NOT EXISTS staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT, 
    email TEXT UNIQUE,
    pay_rate REAL,
    bank_acc TEXT
);
"""

create_client = """
CREATE TABLE IF NOT EXISTS client (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    discount INTEGER
);
"""

create_product = """
CREATE TABLE IF NOT EXISTS product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL,
    image BLOB,
    stock INTEGER
);
"""

create_appointment = """
CREATE TABLE IF NOT EXISTS appointment (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    staff_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client (client_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

create_purchase = """
CREATE TABLE IF NOT EXISTS purchase (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    total_price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES client (client_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product (product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

staff = (
    ("Hannah Bean", "123-456-7890", "hannah.bean@hearth.com", 90.00, "676-456 987278333"),
    ("Marly Papa", "098-765-4321", "marly.papa@hearth.com", 100.00, "656-486 787367282"),
    ("Caleb Underhill", "673-782-8178", "caleb.underhill@hearth.com", 85.00, "666-444 782739201")
)

client = (
    ("Matt Night", "767-9818-1234", "matt.night@farm.com", 1),
    ("Shai Hobby", "625-728-1234", "shai.hobby@tunes.com", 0),
    ("Nanny Fire", "819-462-9180", "nanny.fire@coffee.com", 0)
)

products = (
    ("Guava Hair Mask", 62, 5),
    ("Shampoo No.1 L'Hydratation", 77, 10),
    ("Conditioner No.1 L'Hydratation", 89.5, 0)
)
 
appointments = (
    ("2026-03-20", "13:00:00", 2, 1),
    ("2026-04-07", "10:30:00", 3, 1),
    ("2026-04-07", "11:00:00", 1, 2)
)
 
purchases = (
    (2, 1, 69.3, 1, "2026-01-02", "10:25:30"),
    (3, 2, 179, 2, "2026-01-02", "10:26:30")
)

insert_staff = """
INSERT INTO staff (name, phone, email, pay_rate, bank_acc)
VALUES (?, ?, ?, ?, ?)
"""

insert_client = """
INSERT INTO client (name, phone, email, discount)
VALUES (?, ?, ?, ?)
"""

insert_product = """
INSERT INTO product (name, price, stock)
VALUES (?, ?, ?)
""" 

insert_appointment = """
INSERT INTO appointment (date, time, staff_id, client_id)
VALUES (?, ?, ?, ?)
"""

insert_purchase = """
INSERT INTO purchase (product_id, client_id, total_price, quantity, date, time)
VALUES (?, ?, ?, ?, ?, ?)
"""

def create_database():
    sql_commit(create_staff)
    sql_commit(create_client)
    sql_commit(create_product)
    sql_commit(create_appointment)
    sql_commit(create_purchase)
    sql_commit(insert_staff, staff)
    sql_commit(insert_client, client)
    sql_commit(insert_product, products)
    sql_commit(insert_appointment, appointments)
    sql_commit(insert_purchase, purchases)
    
create_database()