'''
this module will demonstrate the ability to create a data base. The tables needed for the 
restaurant pos will created using this script. once created, methods for updating the database
will be created and a class for handling these will be created and stored in this file. 

'''

import sqlite3
from dataFields import user, menuItem, tableOrder

class posDatabase():
    def __init__(self):
        #Create connection
        self.conn = sqlite3.connect(":memory:")
        
        # Create a cursor
        self.c = self.conn.cursor()
        
        # Create users Table
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id integer PRIMARY KEY, 
            password text NOT NULL,
            first_name text NOT NULL,
            last_name text NOT NULL )
        
            ''')
        # commit this action
        self.conn.commit()
        
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS orders (
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
        self.conn.commit()
        
        # creates a sales table to keep track of individual items solds and the orders they
        # belong to.
        self.c.execute('''CREATE TABLE IF NOT EXISTS sales(
            sales_id integer PRIMARY KEY,
            item_id integer,
            order_id,
            FOREIGN KEY(item_id) REFERENCES items(item_id),
            FOREIGN KEY(order_id) REFERENCES orders(order_id))
            ''')
        self.conn.commit()
        
        # creates an items table for each menu item
        self.c.execute('''CREATE TABLE IF NOT EXISTS items(
            item_id integer PRIMARY KEY,
            price real NOT NULL,
            name text NOT NULL)
            ''')
        self.conn.commit()
        
    def __del__(self):    
        self.conn.close()
    def addNewUser(self,u):
        if isinstance(u,user):
            self.c.execute('''INSERT INTO users(
                password,first_name,last_name
                )
                VALUES (?,?,?)
                ''',(u.pin,u.first_name,u.last_name))
            self.conn.commit()
    def getUsers(self):
        self.c.execute(''' SELECT * FROM users
            ''')
        return self.c.fetchall()
    
if __name__ == '__main__':
    db = posDatabase()
    u = user("jesse", "harper", 123456)
    db.addNewUser(u)
    print(db.getUsers())
        
    








