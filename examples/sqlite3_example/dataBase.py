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
            pin text UNIQUE NOT NULL,
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
        self.c.execute('''CREATE TABLE IF NOT EXISTS menu_items(
            item_id integer PRIMARY KEY,
            price real NOT NULL,
            name text UNIQUE NOT NULL)
            ''')
        self.conn.commit()
        
    def __del__(self):    
        self.conn.close()
    def addNewUser(self,u):
        if isinstance(u,user):
            self.c.execute('''INSERT INTO users(
                pin,first_name,last_name
                )
                VALUES (?,?,?)
                ''',(u.pin,u.first_name,u.last_name))
            self.conn.commit()
    def getAllUsers(self):
        self.c.execute(''' SELECT * FROM users
            ''')
        return self.c.fetchall()
        
    #    takes a user object and returns that user's user_id from the users table
    def getUserId(self,userObject):
        self.c.execute('''SELECT user_id FROM users 
            WHERE pin =? 
            ''',(userObject.pin,))
        return self.c.fetchone()[0]
    
    #    takes a list of orders and adds each order and sale to the database
    def addOrders(self,orders):
        
        for obj in orders:
            self.c.execute('''INSERT INTO orders(
                user_id,
                table_number,
                sales_subtotal,
                time_opened,
                time_closed,
                split,
                guest_count)
                VALUES(?,?,?,?,?,?,?
                )
                ''',(self.getUserId(obj.m_user),
                obj.m_table,
                obj.m_subTotal,
                obj.timeOpened,
                obj.timeClosed,
                obj.m_split,
                obj.m_guests))
            self.conn.commit()
            # get last order_id
            self.c.execute('''
                SELECT max(order_id) FROM orders
                ''')
            order_id = self.c.fetchone()[0]
            # insert all menu items sold into sales table
            # **IMPORTANT** 
            # ALL ITEMS MUST HAVE AN ID IN DATA BASE
            for item in obj.menuItems:
                self.c.execute('''SELECT item_id FROM menu_items
                WHERE name = ?
                    ''',(item.name,))
                item_id = self.c.fetchone()[0]
                self.c.execute('''INSERT INTO sales(
                item_id,
                order_id)
                VALUES(?,?)
                    
                    ''',(item_id,order_id))
                self.conn.commit()
    
    def addMenuItems(self,items):
        for item in items:
            try:
                self.c.execute('''INSERT INTO menu_items(price,name)
                    VALUES(?,?)
                    ''',(item['cost'],item['name']))
                self.conn.commit()
            except:
                return False
        return True            
        
        
if __name__ == '__main__':
    
    db = posDatabase()
    db.c.execute('''INSERT INTO menu_items(price,name)
        VALUES(0.99,"temp")
        ''')
    db.conn.commit()
    u = user("jesse","harper",1243456)
    db.addNewUser(u)
    id = db.getUserId(u)
    print(id)
    t = tableOrder(u)
    t.close()
    for i in range(0,5):
        item = menuItem("temp",0.99)
        t.add_menuItem(item)
    db.addOrders([t])
    db.c.execute('''SELECT * FROM orders
        ''')
    print(db.c.fetchall())
    db.c.execute('''SELECT * FROM sales
        ''')
    for q in db.c.fetchall():
        print(q)    
    








