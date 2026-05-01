import sqlite3
from operator import truediv
from tkinter.constants import PROJECTING

conn = sqlite3.connect('NorthShoreLogistics.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS shipments (
shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
order_id INTEGER FOREIGNKEY references order_details(order_id) ,
vehicle_id INTEGER FOREIGNKEY references vehicle(vehicle_id) ,
warehouse_id INTEGER FOREIGNKEY references warehouse(warehouse_id) 
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS shipment_route (
shipment_id INTEGER FOREIGNKEY references shipments(shipment_id),
route_id INTEGER FOREIGNKEY references routes(route_id),
estimated_arival DATE,
actual_arival DATE,
satus STRING
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS route (
route_id INTEGER PRIMARY KEY AUTOINCREMENT,
start_location STRING,
end_location STRING,
distance INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS vehicle (
vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
plate_number INTEGER,
type STRING,
capacity INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS warehouse (
warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
address STRING,
capacity INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS order_details (
order_id INTEGER PRIMARY KEY AUTOINCREMENT,
placement_date DATE,
item_type STRING
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS customer_info (
order_id INTEGER FOREIGNKEY references orders(order_id),
first_name STRING,
last_name STRING,
phone_number INTEGER,
email STRING
)
""")

conn.commit()

c.execute("INSERT INTO shipments VALUES (12213123312,4324212323223,33232311234,441212312415)")

c.execute("INSERT INTO shipment_route VALUES (131211311, 121123312, 11/03/23, 23/03/23, 'shipped')")

c.execute("INSERT INTO route VALUES (132211313, 'new york', 'london', 5500) ")

c.execute("INSERT INTO vehicle VALUES (312313323, 11223334455, 'BOAT', 1000)")

c.execute("INSERT INTO warehouse VALUES (24123144,'brighton street',10000)")

c.execute("INSERT INTO order_details VALUES (212321231,09/03/23,'LUXURY')")

c.execute("INSERT INTO customer_info VALUES (212133222,'adam', 'forest',4444444, 'a@.ru')")


password = "NorthShore"
passCheck =False
while passCheck == False:
    passinp = input("Enter password: ")
    if passinp == password:
        passCheck = True
        run = True
    else:
        print("Passwords do not match")

while run == True:

    choice = input("would you like to retrieve, delete or insert? (a,b,c)")
    if choice == "a":
        table = input("Enter the table name")
        c.execute(f"""
        SELECT *
        FROM {table}
        """)
        all = c.fetchall()
        print(all)
        conn.commit()

    if choice == "b":
        id = input("Enter shipment_id:")
        c.execute(f"""
        DELETE 
        FROM shipments 
        WHERE shipment_id = {id}
        """)
        conn.commit()

    if choice == "c":
        table = input("Enter the table name")
        values = input("Enter the values")
        c.execute(f"""
        INSERT INTO {table}
        VALUES ({values})
        """)
        conn.commit()







