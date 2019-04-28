from PyQt5 import QtCore, QtGui, QtWidgets

class loginWidget(QtWidgets.QWidget):
    def setUp(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setObjectName("loginWidget")
        self.text = ''
        
        # set the top label for widget
        self.loginMainLayout = QtWidgets.QVBoxLayout(self)
        self.loginMainLayout.setObjectName("loginMainLayout")
        self.labelFrame = QtWidgets.QFrame(self)
        self.labelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelFrame.setObjectName("labelFrame")
        self.labelFrameLayout = QtWidgets.QHBoxLayout(self.labelFrame)
        self.labelFrameLayout.setObjectName("labelFrameLayout")
        self.loginLabel = QtWidgets.QLabel(self.labelFrame)
        self.loginLabel.setObjectName("loginLabel")
        self.loginLabel.setText("Printers IN Kitchen")
        self.labelFrameLayout.addWidget(self.loginLabel, 0, QtCore.Qt.AlignHCenter)
        self.loginMainLayout.addWidget(self.labelFrame)
        # set a spacer between label and text edit box
        spacerItem1 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.loginMainLayout.addItem(spacerItem1)
        
        # set up text edit box
        self.textEditFrame = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditFrame.sizePolicy().hasHeightForWidth())
        self.textEditFrame.setSizePolicy(sizePolicy)
        self.textEditFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEditFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEditFrame.setObjectName("textEditFrame")
        self.textEditLayout = QtWidgets.QVBoxLayout(self.textEditFrame)
        self.textEditLayout.setObjectName("textEditLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.textEditFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.textEditLayout.addWidget(self.lineEdit)
        
        
        # insert num pad
        self.buttons = {}
        self.buttonLayout = QtWidgets.QGridLayout()
        self.buttonLayout.setObjectName('buttonLayout')
        buttons = {'0': "zero_btn",'1':"one_btn",'2':"two_btn",'3':"three_btn",'4':"four_btn",'5':"five_btn",
                   '6':"six_btn",'7':"seven_btn",'8':"eight_btn",'9':"nine_btn"}
        for i in range(1,10):
            self.buttons[buttons[str(i)]] = QtWidgets.QPushButton(self.textEditFrame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.buttons[buttons[str(i)]].sizePolicy().hasHeightForWidth())
            self.buttons[buttons[str(i)]].setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(18)
            self.buttons[buttons[str(i)]].setFont(font)
            self.buttons[buttons[str(i)]].setObjectName(buttons[str(i)])
            self.buttons[buttons[str(i)]].setText(str(i))
            
            self.buttons[buttons[str(i)]].clicked.connect(self.updateEdit(i))
            
            #determine grid location
            col = (i - 1) % 3 
            row = 2 - int((i - 1)/3) 
            self.buttonLayout.addWidget(self.buttons[buttons[str(i)]], row, col, 1, 1)
        
        # add clear button
        self.buttons["clear_btn"] = QtWidgets.QPushButton(self.textEditFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons['clear_btn'].sizePolicy().hasHeightForWidth())
        self.buttons['clear_btn'].setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttons['clear_btn'].setFont(font)
        self.buttons['clear_btn'].setObjectName("clear_btn")
        self.buttons['clear_btn'].setText('clear')
        self.buttons['clear_btn'].clicked.connect(self.clearEdit)
        self.buttonLayout.addWidget(self.buttons['clear_btn'],3,0,1,1)
        
        # add 0 button
        self.buttons[buttons['0']] = QtWidgets.QPushButton(self.textEditFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons[buttons['0']].sizePolicy().hasHeightForWidth())
        self.buttons[buttons['0']].setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttons[buttons['0']].setFont(font)
        self.buttons[buttons['0']].setObjectName(buttons['0'])
        self.buttons[buttons['0']].setText('0')
        self.buttons[buttons['0']].clicked.connect(self.updateEdit(0))
        self.buttonLayout.addWidget(self.buttons[buttons['0']],3,1,1,1)
        
        # add enter button
        self.buttons["enter_btn"] = QtWidgets.QPushButton(self.textEditFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons["enter_btn"].sizePolicy().hasHeightForWidth())
        self.buttons["enter_btn"].setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttons["enter_btn"].setFont(font)
        self.buttons["enter_btn"].setObjectName("enter_btn")
        self.buttons["enter_btn"].setText('Enter')
        self.buttonLayout.addWidget(self.buttons["enter_btn"],3,2,1,1)
        
#         # add cancel button
#         self.buttons["cancel_btn"] = QtWidgets.QPushButton(self.textEditFrame)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.buttons["cancel_btn"].sizePolicy().hasHeightForWidth())
#         self.buttons["cancel_btn"].setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.buttons["cancel_btn"].setFont(font)
#         self.buttons["cancel_btn"].setObjectName("cancel_btn")
#         self.buttons["cancel_btn"].setText('cancel')
#         self.buttonLayout.addWidget(self.buttons["cancel_btn"],4,1,1,1)
        
        # add buttonLayout to textEditLayout
        self.textEditLayout.addLayout(self.buttonLayout)
        # set relative stretch on textEditLayout
        self.textEditLayout.setStretch(0, 1)
        self.textEditLayout.setStretch(1, 4)
        # insert the textEdit frame
        self.loginMainLayout.addWidget(self.textEditFrame)
        
        
    def updateEdit(self,n):
        def foo():
            self.text += str(n) 
            self.lineEdit.setText(self.text)
            
        return foo
    def clearEdit(self):
        self.lineEdit.clear()
        self.text = ''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = loginWidget()
    ui.setUp()
    ui.show()
    sys.exit(app.exec_())       