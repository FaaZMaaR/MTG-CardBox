from PyQt6 import QtGui,QtWidgets
import sys
from mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(r"MTG.ico"))
window = MainWindow()
window.show()
sys.exit(app.exec())