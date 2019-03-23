from PyQt5 import QtCore, QtGui, QtWidgets
from loginPage import loginWidget
from userSelectionPage import userSelectWidget
from orderPage import orderWidget
from dataFields import user,menuItem,tableOrder
from dataBase import posDatabase

class Ui_mainWindow(QtWidgets.QMainWindow):
    def setup(self):
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
        users = self.dataBase.getAllUsers()
        for item in users:
            id,pin,first,last,ad = item
            temp = user(first,last,pin,ad)
            self.users.append(temp)
            
        #connect login page buttons
        self.loginWidget.buttons["enter_btn"].clicked.connect(self.login)
            
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
                else:
                    # else pop up message box "invalid pin"
                    QtWidgets.QMessageBox.about(self,"Error","Invalid input: please try again")
                    self.loginWidget.lineEdit.clear()
                    
                
    