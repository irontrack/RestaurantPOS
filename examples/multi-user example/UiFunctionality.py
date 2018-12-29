from PyQt5 import QtCore, QtGui, QtWidgets
from UiCore import Ui_MainDialog
from dataFields import user,menuItem,tableOrder
class UiFunctional(Ui_MainDialog):
    def __init__(self):
        self.MainDialog = QtWidgets.QDialog()
        self.setupUi(self.MainDialog)
        self.m_orders = []
        self.m_users = []
        self.createUsers()
        
        #connect user select push buttons
        self.toGoOrder_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        self.newTable_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        
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
        
        #connect order push buttons
        self.appetizers_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.entrees_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.drinks_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(2))
        self.desserts_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(3))
        self.finished_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        
    def createUsers(self):
        mainUser = user("john","123456")
        self.m_users.append(mainUser)
    def cancel_pushed(self):
        self.lineEdit.clear()
        self.stackedWidget.setCurrentIndex(0)
        
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = UiFunctional()
    ui.MainDialog.show()
    sys.exit(app.exec_())