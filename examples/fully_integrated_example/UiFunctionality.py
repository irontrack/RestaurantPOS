from PyQt5 import QtCore, QtGui, QtWidgets
from UiCoreTest import Ui_MainWindow
from dataFields import user,menuItem,tableOrder
class UiFunctional(Ui_MainWindow):
    def __init__(self):
        self.mainDialog = QtWidgets.QMainWindow()
        self.setupUi(self.mainDialog)
        self.m_orders = []
        self.m_users = []
        self.createUsers()
        self.currentUser = None
        self.currentOrder = None
        self.modTable = False
        
        #connect user select push buttons
        self.toGoOrder_btn.clicked.connect(self.toGoOrder_pushed)
        self.newTable_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.modifyTable_btn.clicked.connect(self.modTable_pushed)
        
        #connect login push buttons
        self.one_btn.clicked.connect(lambda:self.lineEdit.insert("1"))
        self.two_btn.clicked.connect(lambda:self.lineEdit.insert("2"))
        self.three_btn.clicked.connect(lambda:self.lineEdit.insert("3"))
        self.four_btn.clicked.connect(lambda:self.lineEdit.insert("4"))
        self.five_btn.clicked.connect(lambda:self.lineEdit.insert("5"))
        self.six_btn.clicked.connect(lambda:self.lineEdit.insert("6"))
        self.seven_btn.clicked.connect(lambda:self.lineEdit.insert("7"))
        self.eight_btn.clicked.connect(lambda:self.lineEdit.insert("8"))
        self.nine_btn.clicked.connect(lambda:self.lineEdit.insert("9"))
        self.zero_btn.clicked.connect(lambda:self.lineEdit.insert("0"))
        self.Cancel_btn.clicked.connect(self.cancel_pushed)
        self.clear_btn.clicked.connect(self.lineEdit.clear)
        self.enter_btn.clicked.connect(lambda:self.enter_pushed(self.lineEdit.text()))
        
        #connect order push buttons
        
        # connect appetizer buttons
        self.Appetizers_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.Chips_btn.clicked.connect(lambda:self.addItem("Chips ",3.99))
        self.Guacamole_btn.clicked.connect(lambda:self.addItem("Guacamole ",5.99))
        self.Toastadas_btn.clicked.connect(lambda:self.addItem("Toastadas ",5.99))
        # connect entrees buttons
        self.Entrees_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.Burrito_btn.clicked.connect(lambda:self.addItem("Burrito", 8.99))
        self.Tacos_btn.clicked.connect(lambda:self.addItem("Tacos", 6.99))
        self.Salad_btn.clicked.connect(lambda:self.addItem("Salad", 8.99))
        # connect drinks buttons
        self.Drinks_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(2))
        self.Horchata_btn.clicked.connect(lambda:self.addItem("Horchata", 2.99))
        self.Cerveza_btn.clicked.connect(lambda:self.addItem("Cerveza", 4.99))
        self.Jarritos_btn.clicked.connect(lambda:self.addItem("Jarritos", 1.99))
        #connect desserts buttons        
        self.desserts_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(3))
        self.Churro_btn.clicked.connect(lambda:self.addItem("Churro",2.99))
        self.Flan_btn.clicked.connect(lambda:self.addItem("Flan",4.99))
        #connect final order menu buttons
        self.CancelOrder_btn.clicked.connect(self.cancelOrder_pushed)
        self.finished_btn.clicked.connect(self.finished_pushed)
        self.remove_btn.clicked.connect(self.remove_pushed)
        
    def toGoOrder_pushed(self):
        newOrder = tableOrder(self.m_users[0])
        self.currentOrder = newOrder
        self.currentUser = self.m_users[0]
        self.stackedWidget.setCurrentIndex(2)
        
    def modTable_pushed(self):
        if self.listWidget.count() == 0:
            QtWidgets.QMessageBox.about(self.mainDialog,"warning","No Orders to Modify")
        else:
            index = self.listWidget.currentRow()
            self.currentOrder = self.m_orders[index]
            self.currentUser = self.currentOrder.m_user
            self.stackedWidget.setCurrentIndex(2)
            self.modTable = True
            for item in self.currentOrder.menuItems:
                self.listWidget_2.addItem(str(item))
        
            
           
    def createUsers(self):
        toGo = user("toGo","111111")
        mainUser = user("john","123456")
        self.m_users.append(toGo)
        self.m_users.append(mainUser)
        
    def cancel_pushed(self):
        self.lineEdit.clear()
        self.stackedWidget.setCurrentIndex(0)
        self.currentUser = None
        self.currentOrder = None
    def cancelOrder_pushed(self):
        self.currentUser = None
        self.currentOrder = None
        self.listWidget_2.clear()
        self.stackedWidget.setCurrentIndex(0)
    def enter_pushed(self,pin):
        if self.currentOrder == None and self.isUser(pin):
            self.currentUser = self.addUser(pin) 
            self.lineEdit.clear()
            self.stackedWidget.setCurrentIndex(2)
            self.currentOrder = tableOrder(self.currentUser)
        elif pin == self.currentUser.pin:
            self.lineEdit.clear()
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.lineEdit.clear()
            QtWidgets.QMessageBox.about(self.mainDialog,"warning","This Pin Is Invalid")
    def isUser(self,pin):
        for u in self.m_users:
            if u.pin == pin:
                return True
        return False
    def  addUser(self,pin):
        for u in self.m_users:
            if u.pin == pin:
                return u
    def addItem(self,m_name,m_cost):
        index = self.listWidget_2.currentRow()
        m_menuItem = menuItem(m_name,m_cost,index)
        self.currentOrder.menuItems.append(m_menuItem)
        self.listWidget_2.insertItem(index,str(m_menuItem))
        self.listWidget_2.setCurrentRow(index + 1)
        temp = self.currentOrder.subTotal()
        if self.listWidget_2.count() == len(self.currentOrder.menuItems):
            self.listWidget_2.addItem("=========================")
            self.listWidget_2.addItem(f"Sub-Total ======= {temp}")
        else:
            index = self.listWidget_2.count() - 1
            self.listWidget_2.takeItem(index)
            self.listWidget_2.addItem(f"Sub-Total ======= {temp}") 
            
    def remove_pushed(self):    
        index = self.listWidget_2.currentRow()
        if index < self.listWidget_2.count() and not len(self.currentOrder.menuItems) == 0:
            del self.currentOrder.menuItems[index]
            self.listWidget_2.takeItem(index)
            self.listWidget_2.setCurrentRow(index - 1)
        temp = self.currentOrder.subTotal()
        if self.listWidget_2.count() == len(self.currentOrder.menuItems):
            self.listWidget_2.addItem("=========================")
            self.listWidget_2.addItem(f"Sub-Total ======= {temp}")
        elif len(self.currentOrder.menuItems) == 0:
            self.listWidget_2.clear()
        else:
            index = self.listWidget_2.count() - 1
            self.listWidget_2.takeItem(index)
            self.listWidget_2.addItem(f"Sub-Total ======= {temp}")
    def finished_pushed(self):
        if self.listWidget_2.count() == 0:
            self.cancelOrder_pushed()
        else:
            if not self.modTable: 
                newOrder = self.currentOrder
                self.currentUser.tableOrders.append(newOrder)
                self.m_orders.append(self.currentOrder)
                numberOfOrders = len(self.m_orders)
                self.listWidget.addItem(str(f"order number {numberOfOrders}"))
            else:
                index = self.listWidget.currentRow()
                self.m_orders[index] = self.currentOrder
                self.modTable = False    
            self.listWidget_2.clear()
            self.currentOrder = None
            self.currentUser = None
            self.stackedWidget.setCurrentIndex(0)
   
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = UiFunctional()
    ui.mainDialog.show()
    sys.exit(app.exec_())