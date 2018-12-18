'''
Created on Dec 16, 2018
class: Order_list inherits the Order_list_ui
    adds functionality to the GUI
@author: jesse
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
from Order_list_ui import Ui_OrderWidget 


class Order_list(Ui_OrderWidget):
    def __init__(self,Dialog):
        self.Dialog = Dialog
        self.setupUi(Dialog)
        self.Beer.clicked.connect(self.add_Beer)
        self.remove.clicked.connect(self.remove_item)
        self.churro.clicked.connect(self.add_Churro)
        self.Burrito.clicked.connect(self.add_Burrito)
        self.Taco.clicked.connect(self.add_Taco)
        self.moveUp.clicked.connect(self.move_up)
        self.moveDown.clicked.connect(self.move_down)
    def add_Beer(self):
        row = self.listWidget.currentRow()
        ok = QtWidgets.QMessageBox.question(self.Dialog,"message box","would you like to add Beer?")
        if ok == QtWidgets.QMessageBox.Yes:
            self.listWidget.insertItem(row + 1,"Beer")
            self.listWidget.setCurrentRow(row + 1)
    def add_Churro(self):
        row = self.listWidget.currentRow()
        ok = QtWidgets.QMessageBox.question(self.Dialog,"message box","would you like to add Churro?")
        if ok == QtWidgets.QMessageBox.Yes:
            self.listWidget.insertItem(row + 1,"Churro")
            self.listWidget.setCurrentRow(row + 1)
    def add_Burrito(self):
        row = self.listWidget.currentRow()
        ok = QtWidgets.QMessageBox.question(self.Dialog,"message box","would you like to add Burrito?")
        if ok == QtWidgets.QMessageBox.Yes:
            self.listWidget.insertItem(row + 1,"Burrito")
            self.listWidget.setCurrentRow(row + 1)
    def add_Taco(self):
        row = self.listWidget.currentRow()
        ok = QtWidgets.QMessageBox.question(self.Dialog,"message box","would you like to add Taco?")
        if ok == QtWidgets.QMessageBox.Yes:
            self.listWidget.insertItem(row + 1,"Taco")
            self.listWidget.setCurrentRow(row + 1)
            
    def remove_item(self):
        row = self.listWidget.currentRow()
        ok = QtWidgets.QMessageBox.question(self.Dialog,"message box","would you like to remove this item?")
        if ok == QtWidgets.QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item
    def move_up(self):
        row = self.listWidget.currentRow()
        if row > 0:
            item = self.listWidget.takeItem(row)
            row = row - 1
            self.listWidget.insertItem(row,item)
            self.listWidget.setCurrentRow(row)
    def move_down(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(row)
            row = row + 1
            self.listWidget.insertItem(row,item)
            self.listWidget.setCurrentRow(row)
                 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderWidget = QtWidgets.QDialog()
    orderList = Order_list(OrderWidget)
    OrderWidget.show()
    sys.exit(app.exec_()) 