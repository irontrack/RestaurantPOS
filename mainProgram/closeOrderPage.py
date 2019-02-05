from PyQt5 import QtCore, QtGui, QtWidgets


class closeOrderWidget(QtWidgets.QWidget):
    def setUp(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setObjectName("closeOrderWidget")
        
        #setup mainLayout
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        
        # set up top side label
        
    # set the top label for widget
        self.labelFrame = QtWidgets.QFrame(self)
        self.labelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelFrame.setObjectName("labelFrame")
        self.labelFrameLayout = QtWidgets.QHBoxLayout(self.labelFrame)
        self.labelFrameLayout.setObjectName("labelFrameLayout")
        self.label = QtWidgets.QLabel(self.labelFrame)
        self.label.setObjectName("label")
        self.label.setText("Printers In Networked Kitchens")
        self.labelFrameLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.mainLayout.addWidget(self.labelFrame)
        
        
        # set up order frame
        self.ordersFrame = QtWidgets.QFrame(self)
        self.ordersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ordersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ordersFrame.setObjectName("ordersFrame")
        self.ordersLayout = QtWidgets.QHBoxLayout(self.ordersFrame)
        self.ordersLayout.setObjectName('ordersFrameLayout')
        self.splitWidgets = [splitWidget(self)]
        self.splitWidgets[0].setUp()
        self.ordersLayout.addWidget(self.splitWidgets[0])
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.ordersLayout.addItem(spacerItem)
        self.ordersLayout.setStretch(0,1)
        self.ordersLayout.setStretch(1,3)
        self.mainLayout.addWidget(self.ordersFrame)
        
        # bottom menu section
        
        self.bottomFrame = QtWidgets.QFrame(self)
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName('bottomFrame')
        self.bottomFrameLayout = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.finished_btn = QtWidgets.QPushButton(self.bottomFrame)
        self.finished_btn.setObjectName('finished_btn')
        self.finished_btn.setText('Finished')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.finished_btn.setSizePolicy(sizePolicy)
        self.bottomFrameLayout.addWidget(self.finished_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomFrameLayout.addItem(spacerItem)
        self.print_btn = QtWidgets.QPushButton(self.bottomFrame)
        self.print_btn.setObjectName('print_btn')
        self.print_btn.setText('Print')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.print_btn.setSizePolicy(sizePolicy)
        self.bottomFrameLayout.addWidget(self.print_btn)
        self.printAll_btn = QtWidgets.QPushButton(self.bottomFrame)
        self.printAll_btn.setObjectName('printAll_btn')
        self.printAll_btn.setText('Print All')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.printAll_btn.setSizePolicy(sizePolicy)
        self.bottomFrameLayout.addWidget(self.printAll_btn)
        self.bottomFrameLayout.setStretch(0,1)
        self.bottomFrameLayout.setStretch(1,3)
        self.bottomFrameLayout.setStretch(2,1)
        self.bottomFrameLayout.setStretch(3,1)
        
        self.mainLayout.addWidget(self.bottomFrame)
        
        

class splitWidget(QtWidgets.QWidget):
    def setUp(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setObjectName('mainLayout')
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setObjectName('listWidget')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.mainLayout.addWidget(self.listWidget)
        
        #add buttons
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.close_btn = QtWidgets.QPushButton(self)
        self.close_btn.setObjectName('close_btn')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setText('Close')
        self.buttonLayout.addWidget(self.close_btn)
        
        self.remove_btn = QtWidgets.QPushButton(self)
        self.remove_btn.setObjectName('remove_btn')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.remove_btn.setSizePolicy(sizePolicy)
        self.remove_btn.setText('Remove')
        self.buttonLayout.addWidget(self.remove_btn)
        
        self.mainLayout.addLayout(self.buttonLayout)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sp = closeOrderWidget()
    sp.setUp()
    sp.show()
    sys.exit(app.exec_())  
        