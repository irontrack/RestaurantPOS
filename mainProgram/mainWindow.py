from PyQt5 import QtCore, QtGui, QtWidgets
from loginPage import loginWidget
from userSelectionPage import userSelectWidget
from orderPage import orderWidget

class Ui_mainWindow(QtWidgets.QMainWindow):
    def setup(self):
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
        
        self.stackedWidget.setCurrentIndex(2)
        self.setCentralWidget(self.stackedWidget)
        
        
    