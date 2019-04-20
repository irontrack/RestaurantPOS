import datetime

class user():
    def __init__(self,first_name,last_name,pin,admin):
        self.first_name = first_name
        self.last_name = last_name
        self.administrator = admin
        self.pin = pin
    
        
#    menuItem: each object is a menu item
class menuItem():
    def __init__(self, name, cost, index = 0):
        self.name = name
        self.cost = cost
        self.index = index
    def __str__(self):
        return '{0:=<20s}  {1:>5.2f}'.format(self.name,self.cost)

#    tableOrder is a class that stores the order's owner, menuItems ordered, and several
#    other important attributes for use by program 
class tableOrder():
    def __init__(self, m_user):
        self.menuItems = []
        self.timeOpened = str(datetime.datetime.now())
        self.timeClosed = False
        self.m_split = 1
        self.m_table = 0
        self.m_guests = 1
        self.m_user = m_user
        self.m_subTotal = 0
        self.orderNumber = 0
    def close(self):
        if not self.timeClosed:
            self.timeClosed = str(datetime.datetime.now())
    def subTotal(self):
        return sum(m.cost for m in self.menuItems)
        
    def add_menuItem(self, menuItem):
        self.menuItems.append(menuItem)
        self.m_subTotal = self.subTotal()
        
        
if __name__ == "__main__":
    u = user("jesse","harper",1234)
    o = tableOrder(user)
    o.close()
    print(o.timeOpened)
    print(o.timeClosed)