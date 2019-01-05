import json
from PyQt5 import QtCore, QtGui, QtWidgets

class addButtons():
    def __init__(self,mainWindow):
        with open('defaultSettings.json') as f:
            data = json.load(f)
        
        # create empty list of necessary objects for Items and Submenus
        
        mainWindow.appItems = []
        mainWindow.subMenus = []
        mainWindow.menuWidgets = []
        mainWindow.labelFrames = []
        mainWindow.labels = []
        mainWindow.vLayouts = []
        mainWindow.hLayouts = []
        mainWindow.gLayouts = []
        mainWindow.menuFrames = []
        
        mainWindow.subMenuLayout = QtWidgets.QVBoxLayout()
        mainWindow.subMenuLayout.setObjectName("subMenuLayout")
        mainWindow.menuNavLayout = QtWidgets.QVBoxLayout()
        mainWindow.menuNavLayout.setObjectName("menuNavLayout")
        
        # add the defualSettings submenus
        count = 0
        for subMenus in data['Menu']:
            subMenu = subMenus['subMenu']
            mainWindow.subMenus.append(QtWidgets.QPushButton(mainWindow.frame_6))
            mainWindow.subMenus[count].setObjectName(subMenu + "_btn")
            mainWindow.subMenuLayout.addWidget(mainWindow.subMenus[count])
            mainWindow.subMenus[count].setText(subMenu)
            count += 1
        mainWindow.menuNavLayout.addLayout(mainWindow.subMenuLayout)
        
        # add core nav buttons
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        mainWindow.menuNavLayout.addItem(spacerItem2)
        mainWindow.remove_btn = QtWidgets.QPushButton(mainWindow.frame_6)
        mainWindow.remove_btn.setObjectName("remove_btn")
        mainWindow.menuNavLayout.addWidget(mainWindow.remove_btn)
        mainWindow.CancelOrder_btn = QtWidgets.QPushButton(mainWindow.frame_6)
        mainWindow.CancelOrder_btn.setObjectName("CancelOrder_btn")
        mainWindow.menuNavLayout.addWidget(mainWindow.CancelOrder_btn)
        mainWindow.finished_btn = QtWidgets.QPushButton(mainWindow.frame_6)
        mainWindow.finished_btn.setObjectName("finished_btn")
        mainWindow.menuNavLayout.addWidget(mainWindow.finished_btn)
        mainWindow.horizontalLayout_5.addLayout(mainWindow.menuNavLayout)
        mainWindow.remove_btn.setText("Remove")
        mainWindow.CancelOrder_btn.setText("Cancel")
        mainWindow.finished_btn.setText("Finished")
        
        # menuItems and the stackedWidget that holds it
        mainWindow.stackedWidget_2 = QtWidgets.QStackedWidget(mainWindow.frame_6)
        mainWindow.stackedWidget_2.setObjectName("stackedWidget_2")
        
        count = 0
        for i in range(0,len(data['Menu'])):
            subMenu = data['Menu'][i]['subMenu']
            mainWindow.menuWidgets.append(QtWidgets.QWidget())
            mainWindow.menuWidgets[i].setObjectName(subMenu)
            
            mainWindow.vLayouts.append(QtWidgets.QVBoxLayout(mainWindow.menuWidgets[i]))
            mainWindow.vLayouts[i].setObjectName("labelLayout_" + str(i + 1))
            
            mainWindow.labelFrames.append(QtWidgets.QFrame(mainWindow.menuWidgets[i]))
            mainWindow.labelFrames[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            mainWindow.labelFrames[i].setFrameShadow(QtWidgets.QFrame.Raised)
            mainWindow.labelFrames[i].setObjectName("labelFrame_" + str(i + 1))
            
            mainWindow.hLayouts.append(QtWidgets.QHBoxLayout(mainWindow.labelFrames[i]))
            mainWindow.hLayouts[i].setObjectName("labelLayout_" + str(i + 1))
            
            mainWindow.labels.append(QtWidgets.QLabel(mainWindow.labelFrames[i]))
            mainWindow.labels[i].setObjectName(subMenu + "_" + str(i + 1))
            mainWindow.labels[i].setText(subMenu)
            
            mainWindow.hLayouts[i].addWidget(mainWindow.labels[i], 0, QtCore.Qt.AlignHCenter)
            mainWindow.vLayouts[i].addWidget(mainWindow.labelFrames[i])
            
            mainWindow.menuFrames.append(QtWidgets.QFrame(mainWindow.menuWidgets[i]))
            mainWindow.menuFrames[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            mainWindow.menuFrames[i].setFrameShadow(QtWidgets.QFrame.Raised)
            mainWindow.menuFrames[i].setObjectName("menuFrame_" + str(i + 1))
            
            mainWindow.gLayouts.append(QtWidgets.QGridLayout(mainWindow.menuFrames[i]))
            mainWindow.gLayouts[i].setObjectName("gLayout_" + str(i + 1))
                
            for buttons in data['Menu'][0]['Buttons']:
                # used count as hash function to get gridlayout_6
                # row and column placement 
                row = int(count/3)
                col = count % 3  
                
                name = buttons['itemName']
                tempWidget = QtWidgets.QPushButton(mainWindow.menuFrames[i])
                tempWidget.setObjectName(name + '_btn')
                tempWidget.setText(name)
                mainWindow.gLayouts[i].addWidget(tempWidget,row,col,1,1)
                mainWindow.appItems.append(tempWidget)
                count += 1
    # end?
            mainWindow.vLayouts[i].addWidget(mainWindow.menuFrames[i])
            mainWindow.vLayouts[i].setStretch(0, 1)
            mainWindow.vLayouts[i].setStretch(1, 9)
            mainWindow.stackedWidget_2.addWidget(mainWindow.menuWidgets[i])
            
            
            
            
            
               
            