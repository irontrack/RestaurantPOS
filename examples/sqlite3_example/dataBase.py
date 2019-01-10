'''
this module will demonstrate the ability to create a data base. The tables needed for the 
restaurant pos will created using this script. once created, methods for updating the database
will be created and a class for handling these will be created and stored in this file. 

'''

import sqlite3

#Create connection
conn = sqlite3.connect(":memory:")

# Create a cursor
c = conn.cursor()

# Create users Table
c.execute('''CREATE TABLE users (
    user_id integer PRIMARY KEY, 
    password text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL )

    ''')
# commit this action
conn.commit()


c.execute('''CREATE TABLE IF NOT EXISTS orders (
    order_id integer PRIMARY KEY,
    user_id integer NOT NULL,
    table_number integer,
    sales_subtotal real,
    time_opened text,
    time_closed text,
    split integer,
    guest_count,
    FOREIGN KEY(user_id) REFERENCES users(user_id))
    ''')

# commit this action
conn.commit()

# creates a sales table to keep track of individual items solds and the orders they
# belong to.
c.execute('''CREATE TABLE IF NOT EXISTS sales(
    sales_id integer PRIMARY KEY,
    item_id integer,
    order_id,
    FOREIGN KEY(item_id) REFERENCES items(item_id),
    FOREIGN KEY(order_id) REFERENCES orders(order_id))
    ''')
conn.commit()

# creates an items table for each menu item
c.execute('''CREATE TABLE IF NOT EXISTS items(
    item_id integer PRIMARY KEY,
    price real NOT NULL,
    name text NOT NULL)
    ''')
conn.commit()


conn.close()








