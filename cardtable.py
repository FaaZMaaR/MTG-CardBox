from PyQt6 import QtCore, QtGui, QtWidgets

class CardTable(QtWidgets.QTableWidget):
    cardSelected = QtCore.pyqtSignal(int)
    
    def __init__(self, parent = None):
        QtWidgets.QTableWidget.__init__(self, 0, 7, parent)
        
        headers = ["id", "Название", "Сет", "Номер", "Редкость", "Количество", "Фойл"]
        self.setHorizontalHeaderLabels(headers)
        
        self.hideColumn(0)
        self.setSelectionBehavior(self.SelectionBehavior.SelectRows)
        
        self.cellClicked.connect(self.onRowSelected)
        
    def fillTable(self, data):
        self.setSortingEnabled(False)
        self.setRowCount(0)
        for row in range(len(data)):
            if data[row][0] == None:
                continue
            self.insertRow(row)
            for col in range(len(data[row])):
                self.setItem(row, col, QtWidgets.QTableWidgetItem(str(data[row][col])))
        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
        
    def onRowSelected(self, row, col):
        self.cardSelected.emit(int(self.item(row, 0).text()))