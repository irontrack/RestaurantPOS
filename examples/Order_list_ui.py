# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order_list.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrderWidget(object):
    def setupUi(self, OrderWidget):
        OrderWidget.setObjectName("OrderWidget")
        OrderWidget.resize(748, 568)
        self.horizontalLayout = QtWidgets.QHBoxLayout(OrderWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(OrderWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Beer = QtWidgets.QPushButton(OrderWidget)
        self.Beer.setObjectName("Beer")
        self.verticalLayout.addWidget(self.Beer)
        self.Burrito = QtWidgets.QPushButton(OrderWidget)
        self.Burrito.setObjectName("Burrito")
        self.verticalLayout.addWidget(self.Burrito)
        self.Taco = QtWidgets.QPushButton(OrderWidget)
        self.Taco.setObjectName("Taco")
        self.verticalLayout.addWidget(self.Taco)
        self.churro = QtWidgets.QPushButton(OrderWidget)
        self.churro.setObjectName("churro")
        self.verticalLayout.addWidget(self.churro)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.move_up = QtWidgets.QPushButton(OrderWidget)
        self.move_up.setObjectName("move_up")
        self.verticalLayout.addWidget(self.move_up)
        self.move_down = QtWidgets.QPushButton(OrderWidget)
        self.move_down.setObjectName("move_down")
        self.verticalLayout.addWidget(self.move_down)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.remove = QtWidgets.QPushButton(OrderWidget)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(OrderWidget)
        QtCore.QMetaObject.connectSlotsByName(OrderWidget)

    def retranslateUi(self, OrderWidget):
        _translate = QtCore.QCoreApplication.translate
        OrderWidget.setWindowTitle(_translate("OrderWidget", "Order Menu"))
        self.Beer.setText(_translate("OrderWidget", "Beer"))
        self.Burrito.setText(_translate("OrderWidget", "Burrito"))
        self.Taco.setText(_translate("OrderWidget", "Taco"))
        self.churro.setText(_translate("OrderWidget", "Churo"))
        self.move_up.setText(_translate("OrderWidget", "Move Up"))
        self.move_down.setText(_translate("OrderWidget", "Move Down"))
        self.remove.setText(_translate("OrderWidget", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderWidget = QtWidgets.QDialog()
    ui = Ui_OrderWidget()
    ui.setupUi(OrderWidget)
    OrderWidget.show()
    sys.exit(app.exec_())

