import json
from PyQt5 import QtCore, QtGui, QtWidgets

class orderWidget(QtWidgets.QWidget):
    def setUp(self):
        with open('defaultSettings.json') as f:
            data = json.load(f)
        
        # create empty list of necessary objects for Items and Submenus
        
        self.appItems = {}
        self.subMenus = {}
        self.menuWidgets = {}
        self.labelFrames = {}
        self.labels = {}
        self.vLayouts = {}
        self.hLayouts = {}
        self.gLayouts = {}
        self.menuFrames = {}
        
        
        
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
        self.label.setText('Printers In Networked Kitchens')
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
        
        for subMenus in data['Menu']:
            subMenu = subMenus['subMenu']
            self.subMenus[subMenu] = QtWidgets.QPushButton(self.mainFrame)
            self.subMenus[subMenu].setObjectName(subMenu + "_btn")
            self.subMenuLayout.addWidget(self.subMenus[subMenu])
            self.subMenus[subMenu].setText(subMenu)
            
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
        i = 0
        for items in data['Menu']:
            subMenu = items['subMenu']
            self.menuWidgets[subMenu] = QtWidgets.QWidget()
            self.menuWidgets[subMenu].setObjectName(subMenu + "SubWidget")
            self.vLayouts[subMenu] = QtWidgets.QVBoxLayout(self.menuWidgets[subMenu])
            self.vLayouts[subMenu].setObjectName(subMenu + "VLayout" )
            
            self.labelFrames[subMenu] = QtWidgets.QFrame(self.menuWidgets[subMenu])
            self.labelFrames[subMenu].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.labelFrames[subMenu].setFrameShadow(QtWidgets.QFrame.Raised)
            self.labelFrames[subMenu].setObjectName(subMenu + "LabelFrame")
            
            self.hLayouts[subMenu] = QtWidgets.QHBoxLayout(self.labelFrames[subMenu])
            self.hLayouts[subMenu].setObjectName(subMenu + "LabelLayout")
            
            self.labels[subMenu] = QtWidgets.QLabel(self.labelFrames[subMenu])
            self.labels[subMenu].setObjectName(subMenu + "Label")
            self.labels[subMenu].setText(subMenu)
            
            self.hLayouts[subMenu].addWidget(self.labels[subMenu], 0, QtCore.Qt.AlignHCenter)
            self.vLayouts[subMenu].addWidget(self.labelFrames[subMenu])
            
            self.menuFrames[subMenu] = QtWidgets.QFrame(self.menuWidgets[subMenu])
            self.menuFrames[subMenu].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.menuFrames[subMenu].setFrameShadow(QtWidgets.QFrame.Raised)
            self.menuFrames[subMenu].setObjectName(subMenu + "MenuFrame")
            
            self.gLayouts[subMenu] = QtWidgets.QGridLayout(self.menuFrames[subMenu])
            self.gLayouts[subMenu].setObjectName(subMenu + "GLayout")
                
            for buttons in data['Menu'][i]['Buttons']:
                # used count as hash function to get gridlayout_6
                # row and column placement 
                row = int(count/3)
                col = count % 3  
                
                name = buttons['itemName']
                tempWidget = QtWidgets.QPushButton(self.menuFrames[subMenu])
                tempWidget.setObjectName(name + '_btn')
                tempWidget.setText(name)
                self.gLayouts[subMenu].addWidget(tempWidget,row,col,1,1)
                self.appItems[name] = tempWidget
                count += 1
    # end?
            self.vLayouts[subMenu].addWidget(self.menuFrames[subMenu])
            self.vLayouts[subMenu].setStretch(0, 1)
            self.vLayouts[subMenu].setStretch(1, 9)
            self.stackedWidget.addWidget(self.menuWidgets[subMenu])
            i += 1
            
        # end button assignments
        
        self.mainFrameLayout.addWidget(self.stackedWidget)
        self.mainFrameLayout.setStretch(0, 2)
        self.mainFrameLayout.setStretch(1, 1)
        self.mainFrameLayout.setStretch(2, 3)
        self.mainLayout.addWidget(self.mainFrame)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = orderWidget()
    ui.setUp()
    ui.show()
    sys.exit(app.exec_())               
            
            