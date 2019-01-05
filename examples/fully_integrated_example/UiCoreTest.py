# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiCore.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from addButtons import addButtons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.user_select = QtWidgets.QWidget()
        self.user_select.setObjectName("user_select")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.user_select)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.user_select)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.user_select)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.newTable_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTable_btn.sizePolicy().hasHeightForWidth())
        self.newTable_btn.setSizePolicy(sizePolicy)
        self.newTable_btn.setObjectName("newTable_btn")
        self.verticalLayout_3.addWidget(self.newTable_btn)
        self.modifyTable_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyTable_btn.sizePolicy().hasHeightForWidth())
        self.modifyTable_btn.setSizePolicy(sizePolicy)
        self.modifyTable_btn.setObjectName("modifyTable_btn")
        self.verticalLayout_3.addWidget(self.modifyTable_btn)
        self.toGoOrder_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toGoOrder_btn.sizePolicy().hasHeightForWidth())
        self.toGoOrder_btn.setSizePolicy(sizePolicy)
        self.toGoOrder_btn.setObjectName("toGoOrder_btn")
        self.verticalLayout_3.addWidget(self.toGoOrder_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.user_select)
        self.login = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setObjectName("login")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.login)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.login)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem1)
        self.frame_4 = QtWidgets.QFrame(self.login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nine_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine_btn.sizePolicy().hasHeightForWidth())
        self.nine_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nine_btn.setFont(font)
        self.nine_btn.setObjectName("nine_btn")
        self.gridLayout.addWidget(self.nine_btn, 0, 2, 1, 1)
        self.four_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four_btn.sizePolicy().hasHeightForWidth())
        self.four_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.four_btn.setFont(font)
        self.four_btn.setObjectName("four_btn")
        self.gridLayout.addWidget(self.four_btn, 1, 0, 1, 1)
        self.five_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five_btn.sizePolicy().hasHeightForWidth())
        self.five_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.five_btn.setFont(font)
        self.five_btn.setObjectName("five_btn")
        self.gridLayout.addWidget(self.five_btn, 1, 1, 1, 1)
        self.six_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six_btn.sizePolicy().hasHeightForWidth())
        self.six_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.six_btn.setFont(font)
        self.six_btn.setObjectName("six_btn")
        self.gridLayout.addWidget(self.six_btn, 1, 2, 1, 1)
        self.two_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_btn.sizePolicy().hasHeightForWidth())
        self.two_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.two_btn.setFont(font)
        self.two_btn.setObjectName("two_btn")
        self.gridLayout.addWidget(self.two_btn, 2, 1, 1, 1)
        self.three_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three_btn.sizePolicy().hasHeightForWidth())
        self.three_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.three_btn.setFont(font)
        self.three_btn.setObjectName("three_btn")
        self.gridLayout.addWidget(self.three_btn, 2, 2, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout.addWidget(self.clear_btn, 3, 0, 1, 1)
        self.zero_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_btn.sizePolicy().hasHeightForWidth())
        self.zero_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zero_btn.setFont(font)
        self.zero_btn.setObjectName("zero_btn")
        self.gridLayout.addWidget(self.zero_btn, 3, 1, 1, 1)
        self.enter_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_btn.sizePolicy().hasHeightForWidth())
        self.enter_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.enter_btn.setFont(font)
        self.enter_btn.setObjectName("enter_btn")
        self.gridLayout.addWidget(self.enter_btn, 3, 2, 1, 1)
        self.one_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_btn.sizePolicy().hasHeightForWidth())
        self.one_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.one_btn.setFont(font)
        self.one_btn.setObjectName("one_btn")
        self.gridLayout.addWidget(self.one_btn, 2, 0, 1, 1)
        self.seven_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven_btn.sizePolicy().hasHeightForWidth())
        self.seven_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.seven_btn.setFont(font)
        self.seven_btn.setObjectName("seven_btn")
        self.gridLayout.addWidget(self.seven_btn, 0, 0, 1, 1)
        self.eight_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight_btn.sizePolicy().hasHeightForWidth())
        self.eight_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.eight_btn.setFont(font)
        self.eight_btn.setObjectName("eight_btn")
        self.gridLayout.addWidget(self.eight_btn, 0, 1, 1, 1)
        self.Cancel_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_btn.sizePolicy().hasHeightForWidth())
        self.Cancel_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cancel_btn.setFont(font)
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.gridLayout.addWidget(self.Cancel_btn, 4, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.login)
        self.order = QtWidgets.QWidget()
        self.order.setObjectName("order")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.order)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.order)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.order)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_6)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_5.addWidget(self.listWidget_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.appetizers_btn = QtWidgets.QPushButton(self.frame_6)
        self.appetizers_btn.setObjectName("appetizers_btn")
        self.verticalLayout_8.addWidget(self.appetizers_btn)
        self.entrees_btn = QtWidgets.QPushButton(self.frame_6)
        self.entrees_btn.setObjectName("entrees_btn")
        self.verticalLayout_8.addWidget(self.entrees_btn)
        self.drinks_btn = QtWidgets.QPushButton(self.frame_6)
        self.drinks_btn.setObjectName("drinks_btn")
        self.verticalLayout_8.addWidget(self.drinks_btn)
        self.desserts_btn = QtWidgets.QPushButton(self.frame_6)
        self.desserts_btn.setObjectName("desserts_btn")
        self.verticalLayout_8.addWidget(self.desserts_btn)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.remove_btn = QtWidgets.QPushButton(self.frame_6)
        self.remove_btn.setObjectName("remove_btn")
        self.verticalLayout_9.addWidget(self.remove_btn)
        self.CancelOrder_btn = QtWidgets.QPushButton(self.frame_6)
        self.CancelOrder_btn.setObjectName("CancelOrder_btn")
        self.verticalLayout_9.addWidget(self.CancelOrder_btn)
        self.finished_btn = QtWidgets.QPushButton(self.frame_6)
        self.finished_btn.setObjectName("finished_btn")
        self.verticalLayout_9.addWidget(self.finished_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.Appetizers = QtWidgets.QWidget()
        self.Appetizers.setObjectName("Appetizers")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Appetizers)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_15 = QtWidgets.QFrame(self.Appetizers)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.App_lbl = QtWidgets.QLabel(self.frame_15)
        self.App_lbl.setObjectName("App_lbl")
        self.horizontalLayout_9.addWidget(self.App_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.appBtn_frm = QtWidgets.QFrame(self.Appetizers)
        self.appBtn_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appBtn_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appBtn_frm.setObjectName("appBtn_frm")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.appBtn_frm)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_10.addWidget(self.appBtn_frm)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 9)
        self.stackedWidget_2.addWidget(self.Appetizers)
        
        #start Entrees
        self.Entrees = QtWidgets.QWidget()
        self.Entrees.setObjectName("Entrees")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Entrees)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_9 = QtWidgets.QFrame(self.Entrees)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Ent_lbl = QtWidgets.QLabel(self.frame_9)
        self.Ent_lbl.setObjectName("Ent_lbl")
        self.horizontalLayout_8.addWidget(self.Ent_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_13.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.Entrees)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Burrito_btn = QtWidgets.QPushButton(self.frame_10)
        self.Burrito_btn.setObjectName("Burrito_btn")
        self.gridLayout_3.addWidget(self.Burrito_btn, 0, 1, 1, 1)
        self.Tacos_btn = QtWidgets.QPushButton(self.frame_10)
        self.Tacos_btn.setObjectName("Tacos_btn")
        self.gridLayout_3.addWidget(self.Tacos_btn, 0, 0, 1, 1)
        self.Salad_btn = QtWidgets.QPushButton(self.frame_10)
        self.Salad_btn.setObjectName("Salad_btn")
        self.gridLayout_3.addWidget(self.Salad_btn, 0, 2, 1, 1)
        self.verticalLayout_13.addWidget(self.frame_10)
        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 9)
        self.stackedWidget_2.addWidget(self.Entrees)
        # end Entrees
        
        self.Drinks = QtWidgets.QWidget()
        self.Drinks.setObjectName("Drinks")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.Drinks)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_11 = QtWidgets.QFrame(self.Drinks)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Drk_lbl = QtWidgets.QLabel(self.frame_11)
        self.Drk_lbl.setObjectName("Drk_lbl")
        self.horizontalLayout_10.addWidget(self.Drk_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_16.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.Drinks)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Horchata_btn = QtWidgets.QPushButton(self.frame_12)
        self.Horchata_btn.setObjectName("Horchata_btn")
        self.gridLayout_4.addWidget(self.Horchata_btn, 0, 0, 1, 1)
        self.Cerveza_btn = QtWidgets.QPushButton(self.frame_12)
        self.Cerveza_btn.setObjectName("Cerveza_btn")
        self.gridLayout_4.addWidget(self.Cerveza_btn, 0, 1, 1, 1)
        self.Jarritos_btn = QtWidgets.QPushButton(self.frame_12)
        self.Jarritos_btn.setObjectName("Jarritos_btn")
        self.gridLayout_4.addWidget(self.Jarritos_btn, 0, 2, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_12)
        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 9)
        self.stackedWidget_2.addWidget(self.Drinks)
        self.Desserts = QtWidgets.QWidget()
        self.Desserts.setObjectName("Desserts")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.Desserts)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_14 = QtWidgets.QFrame(self.Desserts)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Des_lbl = QtWidgets.QLabel(self.frame_14)
        self.Des_lbl.setObjectName("Des_lbl")
        self.horizontalLayout_13.addWidget(self.Des_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_19.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.Desserts)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Churro_btn = QtWidgets.QPushButton(self.frame_13)
        self.Churro_btn.setObjectName("Churro_btn")
        self.gridLayout_5.addWidget(self.Churro_btn, 0, 0, 1, 1)
        self.Flan_btn = QtWidgets.QPushButton(self.frame_13)
        self.Flan_btn.setObjectName("Flan_btn")
        self.gridLayout_5.addWidget(self.Flan_btn, 0, 1, 1, 1)
        self.gridLayout_5.setColumnMinimumWidth(0, 1)
        self.gridLayout_5.setColumnMinimumWidth(1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.verticalLayout_19.addWidget(self.frame_13)
        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(1, 9)
        self.stackedWidget_2.addWidget(self.Desserts)
        self.horizontalLayout_5.addWidget(self.stackedWidget_2)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 3)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.order)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Back of House"))
        self.newTable_btn.setText(_translate("MainWindow", "New Table"))
        self.modifyTable_btn.setText(_translate("MainWindow", "Modify Table"))
        self.toGoOrder_btn.setText(_translate("MainWindow", "To Go Orders"))
        self.label_2.setText(_translate("MainWindow", "Back of House"))
        self.nine_btn.setText(_translate("MainWindow", "9"))
        self.four_btn.setText(_translate("MainWindow", "4"))
        self.five_btn.setText(_translate("MainWindow", "5"))
        self.six_btn.setText(_translate("MainWindow", "6"))
        self.two_btn.setText(_translate("MainWindow", "2"))
        self.three_btn.setText(_translate("MainWindow", "3"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.zero_btn.setText(_translate("MainWindow", "0"))
        self.enter_btn.setText(_translate("MainWindow", "Enter"))
        self.one_btn.setText(_translate("MainWindow", "1"))
        self.seven_btn.setText(_translate("MainWindow", "7"))
        self.eight_btn.setText(_translate("MainWindow", "8"))
        self.Cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.label_3.setText(_translate("MainWindow", "Back of House"))
        self.appetizers_btn.setText(_translate("MainWindow", "Appetizers"))
        self.entrees_btn.setText(_translate("MainWindow", "Entrees"))
        self.drinks_btn.setText(_translate("MainWindow", "Drinks"))
        self.desserts_btn.setText(_translate("MainWindow", "Desserts"))
        self.remove_btn.setText(_translate("MainWindow", "Remove"))
        self.CancelOrder_btn.setText(_translate("MainWindow", "Cancel"))
        self.finished_btn.setText(_translate("MainWindow", "Finished"))
        self.App_lbl.setText(_translate("MainWindow", "Appetizers"))
        self.Ent_lbl.setText(_translate("MainWindow", "Entrees"))
        self.Burrito_btn.setText(_translate("MainWindow", "Burrito"))
        self.Tacos_btn.setText(_translate("MainWindow", "Tacos"))
        self.Salad_btn.setText(_translate("MainWindow", "Salad"))
        self.Drk_lbl.setText(_translate("MainWindow", "Drinks"))
        self.Horchata_btn.setText(_translate("MainWindow", "Horchata"))
        self.Cerveza_btn.setText(_translate("MainWindow", "Cerveza"))
        self.Jarritos_btn.setText(_translate("MainWindow", "Jarritos"))
        self.Des_lbl.setText(_translate("MainWindow", "Desserts"))
        self.Churro_btn.setText(_translate("MainWindow", "Churro"))
        self.Flan_btn.setText(_translate("MainWindow", "Flan"))
        
        addButtons(self)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
