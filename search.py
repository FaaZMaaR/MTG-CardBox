from PyQt6 import QtCore, QtGui, QtWidgets

class Search(QtWidgets.QWidget):
    searchClicked = QtCore.pyqtSignal(str)
    
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.le_search = QtWidgets.QLineEdit(self)
        self.pb_search = QtWidgets.QPushButton("Поиск", self)
        self.pb_reset = QtWidgets.QPushButton("Сброс", self)
        
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.le_search)
        hbox.addWidget(self.pb_search)
        hbox.addWidget(self.pb_reset)
        self.setLayout(hbox)
        
        self.pb_search.clicked.connect(self.onSearchClicked)
        self.pb_reset.clicked.connect(self.onResetClicked)
        
    def onSearchClicked(self):
        self.searchClicked.emit(self.le_search.text())
        
    def onResetClicked(self):
        self.le_search.setText("")
        self.onSearchClicked()