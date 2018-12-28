# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        self.loginPin = '8675309'
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(690, 536)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(LoginDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('dial pin')
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.four_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four_btn.sizePolicy().hasHeightForWidth())
        self.four_btn.setSizePolicy(sizePolicy)
        self.four_btn.setObjectName("four_btn")
        self.four_btn.clicked.connect(lambda: self.num_btn('4'))
        self.gridLayout.addWidget(self.four_btn, 1, 0, 1, 1)
        self.five_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five_btn.sizePolicy().hasHeightForWidth())
        self.five_btn.setSizePolicy(sizePolicy)
        self.five_btn.setObjectName("five_btn")
        self.five_btn.clicked.connect(lambda: self.num_btn('5'))
        self.gridLayout.addWidget(self.five_btn, 1, 1, 1, 1)
        self.six_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six_btn.sizePolicy().hasHeightForWidth())
        self.six_btn.setSizePolicy(sizePolicy)
        self.six_btn.setObjectName("six_btn")
        self.six_btn.clicked.connect(lambda: self.num_btn('6'))
        self.gridLayout.addWidget(self.six_btn, 1, 2, 1, 1)
        self.one_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_btn.sizePolicy().hasHeightForWidth())
        self.one_btn.setSizePolicy(sizePolicy)
        self.one_btn.setObjectName("one_btn")
        self.one_btn.clicked.connect(lambda: self.num_btn('1'))
        self.gridLayout.addWidget(self.one_btn, 2, 0, 1, 1)
        self.two_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_btn.sizePolicy().hasHeightForWidth())
        self.two_btn.setSizePolicy(sizePolicy)
        self.two_btn.setObjectName("two_btn")
        self.two_btn.clicked.connect(lambda: self.num_btn('2'))
        self.gridLayout.addWidget(self.two_btn, 2, 1, 1, 1)
        self.zero_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_btn.sizePolicy().hasHeightForWidth())
        self.zero_btn.setSizePolicy(sizePolicy)
        self.zero_btn.setObjectName("zero_btn")
        self.zero_btn.clicked.connect(lambda:self.num_btn('0'))
        self.gridLayout.addWidget(self.zero_btn, 3, 1, 1, 1)
        self.seven_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven_btn.sizePolicy().hasHeightForWidth())
        self.seven_btn.setSizePolicy(sizePolicy)
        self.seven_btn.setObjectName("seven_btn")
        self.seven_btn.clicked.connect(lambda: self.num_btn('7'))
        self.gridLayout.addWidget(self.seven_btn, 0, 0, 1, 1)
        self.eight_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight_btn.sizePolicy().hasHeightForWidth())
        self.eight_btn.setSizePolicy(sizePolicy)
        self.eight_btn.setObjectName("eight_btn")
        self.eight_btn.clicked.connect(lambda: self.num_btn('8'))
        self.gridLayout.addWidget(self.eight_btn, 0, 1, 1, 1)
        self.nine_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine_btn.sizePolicy().hasHeightForWidth())
        self.nine_btn.setSizePolicy(sizePolicy)
        self.nine_btn.setObjectName("nine_btn")
        self.nine_btn.clicked.connect(lambda: self.num_btn('9'))
        self.gridLayout.addWidget(self.nine_btn, 0, 2, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clr_btn)
        self.gridLayout.addWidget(self.clear_btn, 3, 0, 1, 1)
        self.three_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three_btn.sizePolicy().hasHeightForWidth())
        self.three_btn.setSizePolicy(sizePolicy)
        self.three_btn.setObjectName("three_btn")
        self.three_btn.clicked.connect(lambda: self.num_btn('3'))
        self.gridLayout.addWidget(self.three_btn, 2, 2, 1, 1)
        self.enter_btn = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_btn.sizePolicy().hasHeightForWidth())
        self.enter_btn.setSizePolicy(sizePolicy)
        self.enter_btn.setObjectName("enter_btn")
        self.enter_btn.clicked.connect(self.ent_btn)
        self.gridLayout.addWidget(self.enter_btn, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
    def num_btn(self,num):
        self.lineEdit.insert(num)
    def ent_btn(self):
        testPin = self.lineEdit.text()
        if testPin == self.loginPin:
            self.lineEdit.setText('i got your number! thank you')
        else:
            self.lineEdit.setText('sorry, invalid')
    def clr_btn(self):
        self.lineEdit.clear()
    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.four_btn.setText(_translate("LoginDialog", "4"))
        self.five_btn.setText(_translate("LoginDialog", "5"))
        self.six_btn.setText(_translate("LoginDialog", "6"))
        self.one_btn.setText(_translate("LoginDialog", "1"))
        self.two_btn.setText(_translate("LoginDialog", "2"))
        self.zero_btn.setText(_translate("LoginDialog", "0"))
        self.seven_btn.setText(_translate("LoginDialog", "7"))
        self.eight_btn.setText(_translate("LoginDialog", "8"))
        self.nine_btn.setText(_translate("LoginDialog", "9"))
        self.clear_btn.setText(_translate("LoginDialog", "clear"))
        self.three_btn.setText(_translate("LoginDialog", "3"))
        self.enter_btn.setText(_translate("LoginDialog", "enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())
