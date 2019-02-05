import json
from PyQt5 import QtCore, QtGui, QtWidgets

class orderWidget(QtWidgets.QWidget):
    def setUp(self,mainWindow):
        with open('defaultSettings.json') as f:
            data = json.load(f)
        
        # create empty list of necessary objects for Items and Submenus
        
        self.appItems = []
        self.subMenus = []
        self.menuWidgets = []
        self.labelFrames = []
        self.labels = []
        self.vLayouts = []
        self.hLayouts = []
        self.gLayouts = []
        self.menuFrames = []
        
        
        
        # set up widget
        self.setObjectName("order")
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setObjectName("mainLayout")
        # set up label
        self.labelFrame = QtWidgets.QFrame(self)
        self.labelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelFrame.setObjectName("labelFrame")
        self.labelLayout = QtWidgets.QHBoxLayout(self.labelFrame)
        self.labelLayout.setObjectName("labelLayout")
        self.label = QtWidgets.QLabel(self.labelFrame)
        self.label.setObjectName("label")
        self.labelLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label.setText('Printers IN Kitchen')
        self.mainLayout.addWidget(self.labelFrame)
        
        # set up mainFrame and mainFrameLayout
        self.mainFrame = QtWidgets.QFrame(self)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.mainFrameLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.mainFrameLayout.setObjectName("mainFrameLayout")
        self.listWidget = QtWidgets.QListWidget(self.mainFrame)
        self.listWidget.setObjectName("listWidget")
        self.mainFrameLayout.addWidget(self.listWidget)
        
        # add the defualSettings submenus
        self.subMenuLayout = QtWidgets.QVBoxLayout()
        self.subMenuLayout.setObjectName("subMenuLayout")
        self.menuNavLayout = QtWidgets.QVBoxLayout()
        self.menuNavLayout.setObjectName("menuNavLayout")
        count = 0
        for subMenus in data['Menu']:
            subMenu = subMenus['subMenu']
            self.subMenus.append(QtWidgets.QPushButton(self.mainFrame))
            self.subMenus[count].setObjectName(subMenu + "_btn")
            self.subMenuLayout.addWidget(self.subMenus[count])
            self.subMenus[count].setText(subMenu)
            count += 1
        self.menuNavLayout.addLayout(self.subMenuLayout)
        
        # add core nav buttons
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menuNavLayout.addItem(spacerItem2)
        self.remove_btn = QtWidgets.QPushButton(self.mainFrame)
        self.remove_btn.setObjectName("remove_btn")
        self.menuNavLayout.addWidget(self.remove_btn)
        self.CancelOrder_btn = QtWidgets.QPushButton(self.mainFrame)
        self.CancelOrder_btn.setObjectName("CancelOrder_btn")
        self.menuNavLayout.addWidget(self.CancelOrder_btn)
        self.finished_btn = QtWidgets.QPushButton(self.mainFrame)
        self.finished_btn.setObjectName("finished_btn")
        self.menuNavLayout.addWidget(self.finished_btn)
        self.mainFrameLayout.addLayout(self.menuNavLayout)
        self.remove_btn.setText("Remove")
        self.CancelOrder_btn.setText("Cancel")
        self.finished_btn.setText("Finished")
        
        # menuItems and the stackedWidget that holds it
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        
        count = 0
        for i in range(0,len(data['Menu'])):
            subMenu = data['Menu'][i]['subMenu']
            self.menuWidgets.append(QtWidgets.QWidget())
            self.menuWidgets[i].setObjectName(subMenu)
            
            self.vLayouts.append(QtWidgets.QVBoxLayout(self.menuWidgets[i]))
            self.vLayouts[i].setObjectName("labelLayout_" + str(i + 1))
            
            self.labelFrames.append(QtWidgets.QFrame(self.menuWidgets[i]))
            self.labelFrames[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.labelFrames[i].setFrameShadow(QtWidgets.QFrame.Raised)
            self.labelFrames[i].setObjectName("labelFrame_" + str(i + 1))
            
            self.hLayouts.append(QtWidgets.QHBoxLayout(self.labelFrames[i]))
            self.hLayouts[i].setObjectName("labelLayout_" + str(i + 1))
            
            self.labels.append(QtWidgets.QLabel(self.labelFrames[i]))
            self.labels[i].setObjectName(subMenu + "_" + str(i + 1))
            self.labels[i].setText(subMenu)
            
            self.hLayouts[i].addWidget(self.labels[i], 0, QtCore.Qt.AlignHCenter)
            self.vLayouts[i].addWidget(self.labelFrames[i])
            
            self.menuFrames.append(QtWidgets.QFrame(self.menuWidgets[i]))
            self.menuFrames[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.menuFrames[i].setFrameShadow(QtWidgets.QFrame.Raised)
            self.menuFrames[i].setObjectName("menuFrame_" + str(i + 1))
            
            self.gLayouts.append(QtWidgets.QGridLayout(self.menuFrames[i]))
            self.gLayouts[i].setObjectName("gLayout_" + str(i + 1))
                
            for buttons in data['Menu'][i]['Buttons']:
                # used count as hash function to get gridlayout_6
                # row and column placement 
                row = int(count/3)
                col = count % 3  
                
                name = buttons['itemName']
                tempWidget = QtWidgets.QPushButton(self.menuFrames[i])
                tempWidget.setObjectName(name + '_btn')
                tempWidget.setText(name)
                self.gLayouts[i].addWidget(tempWidget,row,col,1,1)
                self.appItems.append(tempWidget)
                count += 1
    # end?
            self.vLayouts[i].addWidget(self.menuFrames[i])
            self.vLayouts[i].setStretch(0, 1)
            self.vLayouts[i].setStretch(1, 9)
            self.stackedWidget.addWidget(self.menuWidgets[i])
        self.mainFrameLayout.addWidget(self.stackedWidget)
        self.mainFrameLayout.setStretch(0, 2)
        self.mainFrameLayout.setStretch(1, 1)
        self.mainFrameLayout.setStretch(2, 3)
        self.mainLayout.addWidget(self.mainFrame)
            
            
            
            