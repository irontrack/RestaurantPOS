from PyQt5 import QtCore, QtGui, QtWidgets
from UiCore import Ui_MainDialog

class UiFunctional(Ui_MainDialog):
    def __init__(self):
        self.MainDialog = QtWidgets.QDialog()
        self.setupUi(self.MainDialog)
        
        #connect push buttons
        self.toGoOrder_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        self.appetizers_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.entrees_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.drinks_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(2))
        self.desserts_btn.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(3))
        self.finished_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UiFunctional()
    ui.MainDialog.show()
    sys.exit(app.exec_())