'''
Created on Dec 16, 2018
class: Order_list inherits the Order_list_ui
    adds functionality to the GUI
@author: jesse
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from Order_list_ui import Ui_OrderWidget as Ui

class Order_list(Ui):
   def __init__(self,Dialog):
       self.setupUi(Dialog)
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderWidget = QtWidgets.QDialog()
    orderList = Order_list(OrderWidget)
    OrderWidget.show()
    sys.exit(app.exec_()) 