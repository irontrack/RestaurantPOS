from PyQt5 import QtCore, QtGui, QtWidgets


class user():
    def __init__(self,name,pin):
        self.name = name
        self.pin = pin
        self.tableOrders = []
    def add_tableOrder(self,listIndex):
        newTableOrder = tableOrder(listIndex)
        self.tableOrder.append(newTableOrder)
        
        
class menuItem():
    def __init__(self, name, cost, index = 0):
        self.name = name
        self.cost = cost
        self.index = index
    def __str__(self):
        return '{0:=<20s}  {1:>5.2f}'.format(self.name,self.cost)
class tableOrder():
    def __init__(self, m_user):
        self.menuItems = []
        self.m_user = m_user
        self.m_subTotal = 0
    def subTotal(self):
        return sum(m.cost for m in self.menuItems)
        
    def add_menuItem(self, menuItem):
        self.menuItems.append(menuItem)
        self.m_subTotal = self.subTotal()
        
        
if __name__ == "__main__":
    newTableOrder = tableOrder(0)
    for i in range(0,10):
        newItem = menuItem("taco",4.00,i)
        newTableOrder.add_menuItem(newItem)
    cost = newTableOrder.subTotal()
    print(cost)
        
        
        
        