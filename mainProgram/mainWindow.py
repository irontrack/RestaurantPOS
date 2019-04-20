from PyQt5 import QtCore, QtGui, QtWidgets
from loginPage import loginWidget
from userSelectionPage import userSelectWidget
from orderPage import orderWidget
from dataFields import user,menuItem,tableOrder
from dataBase import posDatabase

class Ui_mainWindow(QtWidgets.QMainWindow):
    def setup(self):
        
        #self.setStyleSheet('''QWidget {background-color: black} 
        #       QPushButton {background-color: red}
        #       ''')
        self.dataBase = posDatabase()
        self.setObjectName("mainWindow")
        self.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(self)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        
        # add loginWidget
        self.loginWidget = loginWidget(self.stackedWidget)
        self.loginWidget.setUp()
        self.stackedWidget.addWidget(self.loginWidget)
        
        # add userSelectWidget
        self.userSelectWidget = userSelectWidget(self.stackedWidget)
        self.userSelectWidget.setUp()
        self.stackedWidget.addWidget(self.userSelectWidget)
        
        # add orderWidget
        self.orderWidget = orderWidget(self.stackedWidget)
        self.orderWidget.setUp()
        self.stackedWidget.addWidget(self.orderWidget)
        
        self.stackedWidget.setCurrentIndex(0)
        self.setCentralWidget(self.stackedWidget)
        
        # create a list of users
        self.users = []
        self.currentUser = None
        users = self.dataBase.getAllUsers()
        for item in users:
            id,pin,first,last,ad = item
            temp = user(first,last,pin,ad)
            self.users.append(temp)
        # create list of open orders
        self.openOrders = []
            
        #connect login page buttons
        self.loginWidget.buttons["enter_btn"].clicked.connect(self.login)
        #connect userSelectWidget Buttons
        #connect newOrder button
        self.userSelectWidget.newTable_btn.clicked.connect(self.newTable)
        #connect modTable button
        self.userSelectWidget.modTable_btn.clicked.connect(self.modTable)
        #connect editOrder button
    def login(self):
        # get lineEdit text
        pin = self.loginWidget.lineEdit.text()
        if not pin.isnumeric():
            QtWidgets.QMessageBox.about(self,"Error","Invalid input: please try again")
            self.loginWidget.lineEdit.clear()
        else:    
            
            # search user pins for match
            for person in self.users:
                
                if person.pin == pin:
                    # if match found, switch screen to appropriate page
                    self.loginWidget.lineEdit.clear()
                    self.stackedWidget.setCurrentIndex(1)
                    self.currentUser = person
                    # for each openOrder attached to user, display
                    for table in self.openOrders:
                        if table.m_user.pin == pin:
                            self.userSelectWidget.listWidget.append(str(table))
                    # if admin is true, connect buttons for editing default settings
                else:
                    # else pop up message box "invalid pin"
                    QtWidgets.QMessageBox.about(self,"Error","Invalid input: please try again")
                    self.loginWidget.lineEdit.clear()
                    
    # definitions for the user selection screen buttons
    
    def newTable(self):
        self.stackedWidget.setCurrentIndex(2)
        self.orderWidget.currentOrder = tableOrder(self.currentUser)           
    def modTable(self):
        # check table selection
        # if selected table 
        # get order index
        i = self.userSelectWidget.listWidget.currentRow()
        # use index to load order to orderWidget.currentOrder
        self.orderWidget.currentOrder = self.openOrders(i)
        # show order
        self.orderWidget.showOrder(self.orderWidget.currentOrder)
        # change page
        self.stackedWidget.secCurrentIndex(2)
    def showTables(self):
        self.userSelectWidget.listWidget.clear()
        for table in self.openOrders:
            info = "Order Number " + str(table.orderNumber) + "     Server: " + table.m_user.name 
            self.userSelectWidget.listWidget.addItem(info)
            
            