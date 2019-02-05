from PyQt5 import QtCore, QtGui, QtWidgets

from mainWindow import Ui_mainWindow
import sys
app = QtWidgets.QApplication(sys.argv)
Ui = Ui_mainWindow()
Ui.setup()
Ui.show()
sys.exit(app.exec_())
