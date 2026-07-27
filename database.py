create_staff = """
CREATE TABLE IF EXISTS staff (
    staff_if INTERGER PRIMARY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT, 
    email TEXT UNIQUE,
    pay_rate REAL,
    bank_acc TEXT,
);
"""

create_client = """
CREATE TABLE IF EXISTS client (
    client_id INTERGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    discount INTERGER, 
);
"""

create_product = """
CREATE TABLE IF EXISTS product (
    product_id INTERGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL,
    image BLOB,
    stock INTERGER,
);
"""

create_appointment = """
CREATE TABLE IF EXISTS appointment (
    appointment_id INTERGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    staff_id INTERGER NOT NULL,
    client_id INTERGER NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client (client_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
);
"""

create_purchase = """
CREATE TABLE IF EXISTS purchase (
    purchase_id INTERGER PRIMARY KEY AUTOINCREMENT,
    product_id INTERGER NOT NULL,
    client_id INTERGER NOT NULL,
    total_price REAL NOT NULL,
    quantity INTERGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES client (client_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product (product_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
);
"""