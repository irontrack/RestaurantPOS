import json
from PyQt5 import QtCore, QtGui, QtWidgets

class addButtons():
    def __init__(self,MainWindow):
        with open('defaultSettings.json') as f:
            data = json.load(f)
            # create empty list of push button widgets
        MainWindow.appItems = []
        count = 0
        for buttons in data['Menu'][0]['Buttons']:
            # used count as hash function to get gridlayout_6
            # row and column placement
            row = int(count/3)
            col = count % 3  
            name = buttons['itemName']
            tempWidget = QtWidgets.QPushButton(MainWindow.appBtn_frm)
            tempWidget.setObjectName(name + '_btn')
            tempWidget.setText(name)
            MainWindow.gridLayout_6.addWidget(tempWidget,row,col,1,1)
            MainWindow.appItems.append(tempWidget)
            count += 1
            print(buttons['itemName'],row,col)