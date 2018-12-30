from PyQt5 import QtCore, QtGui, QtWidgets
from UiCore import Ui_MainDialog
from dataFields import user,menuItem,tableOrder
class UiFunctional(Ui_MainDialog):
    def __init__(self):
        self.mainDialog = QtWidgets.QDialog()
        self.setupUi(self.mainDialog)
        self.m_orders = []
        self.m_users = []
        self.createUsers()
        self.currentUser = None
        self.currentOrder = None
        
        #connect user select push buttons
        self.toGoOrder_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
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
        self.appetizers_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.Chips_btn.clicked.connect(lambda:self.addItem("Chips",3.99))
        self.entrees_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.drinks_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(2))
        self.desserts_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(3))
        self.CancelOrder_btn.clicked.connect(self.cancelOrder_pushed)
        self.finished_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
    
    def modTable_pushed(self):
        if self.listWidget.count() == 0:
            QtWidgets.QMessageBox.about(self.mainDialog,"warning","No Orders to Modify")
        else:
            index = self.listWidget.currentRow()
            self.currentOrder == self.m_orders[index]
            self.currentUser == self.currentOrder.m_user
            self.stackedWidget.setCurrentIndex(2)
        
            
           
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
            self.stackedWidget.setCurrentIndex(2)
            self.currentOrder = tableOrder(self.currentUser)
        elif pin == self.currentUser.pin:
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
        self.listWidget_2.addItem(str(m_menuItem))
        self.listWidget_2.setCurrentRow(index + 1) 
            
        
    
   
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = UiFunctional()
    ui.mainDialog.show()
    sys.exit(app.exec_())