from PyQt5 import QtCore, QtGui, QtWidgets

class userSelectWidget(QtWidgets.QWidget):
    def setUp(self):
        # set up widget size policy
        
        self.setObjectName('userSelectWidget')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        # create vertical layout for the widget
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setObjectName('mainLayout')
        
        # set up top label
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
        
        # set up the frame for the user selection and order list
        self.mainFrame = QtWidgets.QFrame(self)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName('mainFrame')
        self.mainFrameLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.mainFrameLayout.setObjectName('mainFrameLayout')
        self.listWidget = QtWidgets.QListWidget(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.mainFrameLayout.addWidget(self.listWidget)
        
        # add spacer to mainFrame
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.mainFrameLayout.addItem(spacerItem)
        
        # add layout and menu section
        self.menuLayout = QtWidgets.QVBoxLayout()
        self.menuLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.menuLayout.setObjectName('menuLayout')
        # table button
        self.newTable_btn = QtWidgets.QPushButton(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTable_btn.sizePolicy().hasHeightForWidth())
        self.newTable_btn.setSizePolicy(sizePolicy)
        self.newTable_btn.setObjectName("newTable_btn")
        self.newTable_btn.setText('New Table')
        self.menuLayout.addWidget(self.newTable_btn)
        
        # modify button
        self.modTable_btn = QtWidgets.QPushButton(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTable_btn.sizePolicy().hasHeightForWidth())
        self.modTable_btn.setSizePolicy(sizePolicy)
        self.modTable_btn.setObjectName("modTable_btn")
        self.modTable_btn.setText('Modify Table')
        self.menuLayout.addWidget(self.modTable_btn)
        
        # To Go Order Button
        self.toGoOrders_btn = QtWidgets.QPushButton(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTable_btn.sizePolicy().hasHeightForWidth())
        self.toGoOrders_btn.setSizePolicy(sizePolicy)
        self.toGoOrders_btn.setObjectName("toGoOrders_btn")
        self.toGoOrders_btn.setText('To GO Orders')
        self.menuLayout.addWidget(self.toGoOrders_btn)
        
        self.mainFrameLayout.addLayout(self.menuLayout)
        
        #add mainFrame to mainLayout
        self.mainLayout.addWidget(self.mainFrame)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui = userSelectWidget()
    Ui.setUp()
    font = QtGui.QFont()
    font.setPointSize(14)
    Ui.setFont(font)
    Ui.show()
    sys.exit(app.exec_())
        