from PyQt6 import QtCore, QtGui, QtWidgets

class NameFilter(QtWidgets.QWidget):
    def __init__(self, title, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
            
        self.lb_title = QtWidgets.QLabel(title, self)
        self.lb_inclusive = QtWidgets.QLabel("включить", self)
        self.lb_exclusive = QtWidgets.QLabel("исключить", self)
        self.comb_name = QtWidgets.QComboBox(self)
        self.list_inclusive = QtWidgets.QListWidget(self)
        self.list_exclusive = QtWidgets.QListWidget(self)
        self.pb_include = QtWidgets.QPushButton("Включительно", self)
        self.pb_add = QtWidgets.QPushButton("Добавить", self)
        self.pb_remove = QtWidgets.QPushButton("Убрать", self)
        self.pb_clear = QtWidgets.QPushButton("Очистить", self)
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lb_title, 0, 0, 1, 4)
        grid.addWidget(self.lb_inclusive, 1, 2)
        grid.addWidget(self.lb_exclusive, 1, 3)
        grid.addWidget(self.comb_name, 2, 0, 1, 2)
        grid.addWidget(self.list_inclusive, 2, 2, 3, 1)
        grid.addWidget(self.list_exclusive, 2, 3, 3, 1)
        grid.addWidget(self.pb_include, 4, 0)
        grid.addWidget(self.pb_add, 3, 0)
        grid.addWidget(self.pb_remove, 3, 1)
        grid.addWidget(self.pb_clear, 4, 1)
        self.setLayout(grid)
        
        self.lb_inclusive.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_exclusive.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.pb_include.clicked.connect(self.onIncludeClicked)
        self.pb_add.clicked.connect(self.onAddClicked)
        self.pb_remove.clicked.connect(self.onRemoveClicked)
        self.pb_clear.clicked.connect(self.onClearClicked)
        
    def fillComboBox(self, data):
        for name in data:
            self.comb_name.addItem(name[0])
            
    def onIncludeClicked(self):
        if self.pb_include.text() == "Включительно":
            self.pb_include.setText("Исключительно")
            self.list_inclusive.clear()
        else:
            self.pb_include.setText("Включительно")
            self.list_exclusive.clear()
            
    def onAddClicked(self):
        if self.pb_include.text() == "Включительно":
            self.list_inclusive.addItem(QtWidgets.QListWidgetItem(self.comb_name.currentText()))
        else:
            self.list_exclusive.addItem(QtWidgets.QListWidgetItem(self.comb_name.currentText()))
            
    def onRemoveClicked(self):
        if self.pb_include.text() == "Включительно":
            self.list_inclusive.takeItem(self.list_inclusive.currentIndex().row())
        else:
            self.list_exclusive.takeItem(self.list_exclusive.currentIndex().row())
            
    def onClearClicked(self):
        self.list_inclusive.clear()
        self.list_exclusive.clear()

class IntFilter(QtWidgets.QWidget):
    def __init__(self, title, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
            
        self.lb_title = QtWidgets.QLabel(title, self)
        self.comb_name = QtWidgets.QComboBox(self)
        self.table_filter = QtWidgets.QTableWidget(0, 3, self)
        self.sb_value = QtWidgets.QSpinBox(self)
        self.pb_compare = QtWidgets.QPushButton("=", self)
        self.pb_add = QtWidgets.QPushButton("Добавить", self)
        self.pb_remove = QtWidgets.QPushButton("Убрать", self)
        self.pb_clear = QtWidgets.QPushButton("Очистить", self)
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lb_title, 0, 0, 1, 3)
        grid.addWidget(self.comb_name, 1, 0, 1, 2)
        grid.addWidget(self.table_filter, 1, 2, 5, 1)
        grid.addWidget(self.sb_value, 2, 1)
        grid.addWidget(self.pb_compare, 2, 0)
        grid.addWidget(self.pb_add, 3, 0, 1, 2)
        grid.addWidget(self.pb_remove, 4, 0, 1, 2)
        grid.addWidget(self.pb_clear, 5, 0, 1, 2)
        self.setLayout(grid)
        
        self.comb_name.addItem("Мана-стоимость")
        self.comb_name.addItem("Сила")
        self.comb_name.addItem("Выносливость")
        self.comb_name.addItem("Верность")
        
        self.sb_value.setMinimum(0)
        self.sb_value.setMaximum(100)
        
        headers = ["Характеристика", "Сравнение", "Значение"]
        self.table_filter.setHorizontalHeaderLabels(headers)
        self.table_filter.setSelectionBehavior(self.table_filter.SelectionBehavior.SelectRows)
        
        self.pb_compare.clicked.connect(self.onCompareClicked)
        self.pb_add.clicked.connect(self.onAddClicked)
        self.pb_remove.clicked.connect(self.onRemoveClicked)
        self.pb_clear.clicked.connect(self.onClearClicked)
        
    def onCompareClicked(self):
        if self.pb_compare.text() == "=":
            self.pb_compare.setText(">")
        elif self.pb_compare.text() == ">":
            self.pb_compare.setText("<")
        else:
            self.pb_compare.setText("=")
            
    def onAddClicked(self):
        row = self.table_filter.rowCount()
        self.table_filter.insertRow(row)
        self.table_filter.setItem(row, 0, QtWidgets.QTableWidgetItem(self.comb_name.currentText()))
        self.table_filter.setItem(row, 1, QtWidgets.QTableWidgetItem(self.pb_compare.text()))
        self.table_filter.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.sb_value.value())))
    
    def onRemoveClicked(self):
        self.table_filter.removeRow(self.table_filter.currentRow())
    
    def onClearClicked(self):
        self.table_filter.setRowCount(0)

class SubstringFilter(QtWidgets.QWidget):
    def __init__(self, title, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
            
        self.lb_title = QtWidgets.QLabel(title, self)
        self.le_substring = QtWidgets.QLineEdit(self)
        self.list_inclusive = QtWidgets.QListWidget(self)
        self.pb_add = QtWidgets.QPushButton("Добавить", self)
        self.pb_remove = QtWidgets.QPushButton("Убрать", self)
        self.pb_clear = QtWidgets.QPushButton("Очистить", self)
        
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lb_title, 0, 0, 1, 2)
        grid.addWidget(self.le_substring, 1, 0)
        grid.addWidget(self.pb_add, 2, 0)
        grid.addWidget(self.pb_remove, 3, 0)
        grid.addWidget(self.pb_clear, 4, 0)
        grid.addWidget(self.list_inclusive, 1, 1, 4, 1)
        self.setLayout(grid)
        
        self.pb_add.clicked.connect(self.onAddClicked)
        self.pb_remove.clicked.connect(self.onRemoveClicked)
        self.pb_clear.clicked.connect(self.onClearClicked)
        
    def onAddClicked(self):
        self.list_inclusive.addItem(QtWidgets.QListWidgetItem(self.le_substring.text()))
            
    def onRemoveClicked(self):
        self.list_inclusive.takeItem(self.list_inclusive.currentIndex().row())
            
    def onClearClicked(self):
        self.list_inclusive.clear()

class ColorFilter(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
            
        self.lb_title = QtWidgets.QLabel("Цвет", self)
        self.pb_white = QtWidgets.QPushButton(self)
        self.pb_blue = QtWidgets.QPushButton(self)
        self.pb_black = QtWidgets.QPushButton(self)
        self.pb_red = QtWidgets.QPushButton(self)
        self.pb_green = QtWidgets.QPushButton(self)
        self.pb_noncolor = QtWidgets.QPushButton(self)
            
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.pb_white)
        hbox.addWidget(self.pb_blue)
        hbox.addWidget(self.pb_black)
        hbox.addWidget(self.pb_red)
        hbox.addWidget(self.pb_green)
        hbox.addWidget(self.pb_noncolor)
        vbox.addWidget(self.lb_title)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.pb_white.setCheckable(True)
        self.pb_blue.setCheckable(True)
        self.pb_black.setCheckable(True)
        self.pb_red.setCheckable(True)
        self.pb_green.setCheckable(True)
        self.pb_noncolor.setCheckable(True)
            
        self.pb_white.setIcon(QtGui.QIcon("Pictures/Icons/WhiteT.png"))
        self.pb_white.setIconSize(QtCore.QSize(50, 50))
        self.pb_blue.setIcon(QtGui.QIcon("Pictures/Icons/BlueT.png"))
        self.pb_blue.setIconSize(QtCore.QSize(50, 50))
        self.pb_black.setIcon(QtGui.QIcon("Pictures/Icons/BlackT.png"))
        self.pb_black.setIconSize(QtCore.QSize(50, 50))
        self.pb_red.setIcon(QtGui.QIcon("Pictures/Icons/RedT.png"))
        self.pb_red.setIconSize(QtCore.QSize(50, 50))
        self.pb_green.setIcon(QtGui.QIcon("Pictures/Icons/GreenT.png"))
        self.pb_green.setIconSize(QtCore.QSize(50, 50))
        self.pb_noncolor.setIcon(QtGui.QIcon("Pictures/Icons/NoncolorT.png"))
        self.pb_noncolor.setIconSize(QtCore.QSize(50, 50))
        
        self.pb_white.toggled.connect(self.onWhiteToggled)
        self.pb_blue.toggled.connect(self.onBlueToggled)
        self.pb_black.toggled.connect(self.onBlackToggled)
        self.pb_red.toggled.connect(self.onRedToggled)
        self.pb_green.toggled.connect(self.onGreenToggled)
        self.pb_noncolor.toggled.connect(self.onNoncolorToggled)
        
    def turnOffColors(self):
        self.pb_white.setChecked(False)
        self.pb_blue.setChecked(False)
        self.pb_black.setChecked(False)
        self.pb_red.setChecked(False)
        self.pb_green.setChecked(False)
        
    def turnOffNoncolor(self):
        self.pb_noncolor.setChecked(False)
        
    def onWhiteToggled(self, state):
        if state:
            self.pb_white.setIcon(QtGui.QIcon("Pictures/Icons/White.png"))
            self.turnOffNoncolor()
        else:
            self.pb_white.setIcon(QtGui.QIcon("Pictures/Icons/WhiteT.png"))
            
    def onBlueToggled(self, state):
            if state:
                self.pb_blue.setIcon(QtGui.QIcon("Pictures/Icons/Blue.png"))
                self.turnOffNoncolor()
            else:
                self.pb_blue.setIcon(QtGui.QIcon("Pictures/Icons/BlueT.png"))
                
    def onBlackToggled(self, state):
            if state:
                self.pb_black.setIcon(QtGui.QIcon("Pictures/Icons/Black.png"))
                self.turnOffNoncolor()
            else:
                self.pb_black.setIcon(QtGui.QIcon("Pictures/Icons/BlackT.png"))
                
    def onRedToggled(self, state):
            if state:
                self.pb_red.setIcon(QtGui.QIcon("Pictures/Icons/Red.png"))
                self.turnOffNoncolor()
            else:
                self.pb_red.setIcon(QtGui.QIcon("Pictures/Icons/RedT.png"))
                
    def onGreenToggled(self, state):
            if state:
                self.pb_green.setIcon(QtGui.QIcon("Pictures/Icons/Green.png"))
                self.turnOffNoncolor()
            else:
                self.pb_green.setIcon(QtGui.QIcon("Pictures/Icons/GreenT.png"))
                
    def onNoncolorToggled(self, state):
            if state:
                self.pb_noncolor.setIcon(QtGui.QIcon("Pictures/Icons/Noncolor.png"))
                self.turnOffColors()
            else:
                self.pb_noncolor.setIcon(QtGui.QIcon("Pictures/Icons/NonColorT.png"))
            
class FilterStruct:
    def __init__(self):
        self.setInList = []
        self.setExList = []
        self.rarityInList = []
        self.rarityExList = []
        self.stypeInList = []
        self.stypeExList = []
        self.typeInList = []
        self.typeExList = []
        self.utypeInList = []
        self.utypeExList = []
        self.manacostEqList = []
        self.manacostGrList = []
        self.manacostLessList = []
        self.strengthEqList = []
        self.strengthGrList = []
        self.strengthLessList = []
        self.enduranceEqList = []
        self.enduranceGrList = []
        self.enduranceLessList = []
        self.loyaltyEqList = []
        self.loyaltyGrList = []
        self.loyaltyLessList = []
        self.descriptionList = []
        self.white = False
        self.blue = False
        self.black = False
        self.red = False
        self.green = False
        self.noncolor = False
        self.artistInList = []
        self.artistExList = []
        self.designInList = []
        self.designExList = []

class Filter(QtWidgets.QDialog):
    filterApplied = QtCore.pyqtSignal(FilterStruct)
    filterReset = QtCore.pyqtSignal()
    
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.setWindowTitle("Фильтры")
        self.setMinimumSize(800, 600)
        
        self.setFilter = NameFilter("Сет", self)
        self.rarityFilter = NameFilter("Редкость", self)
        self.stypeFilter = NameFilter("Супертип", self)
        self.typeFilter = NameFilter("Тип", self)
        self.utypeFilter = NameFilter("Подтип", self)
        self.attrFilter = IntFilter("Характеристики", self)
        self.descriptionFilter = SubstringFilter("Описание", self)
        self.colorFilter = ColorFilter(self)
        self.artistFilter = NameFilter("Художник", self)
        self.designFilter = NameFilter("Оформление", self)
        self.pb_apply = QtWidgets.QPushButton("Применить", self)
        self.pb_reset = QtWidgets.QPushButton("Сбросить", self)
        
        scroll = QtWidgets.QScrollArea(self)
        wgt = QtWidgets.QWidget(self)        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.setFilter)
        vbox.addWidget(self.rarityFilter)
        vbox.addWidget(self.stypeFilter)
        vbox.addWidget(self.typeFilter)
        vbox.addWidget(self.utypeFilter)
        vbox.addWidget(self.attrFilter)
        vbox.addWidget(self.descriptionFilter)
        vbox.addWidget(self.colorFilter)
        vbox.addWidget(self.artistFilter)
        vbox.addWidget(self.designFilter)
        wgt.setLayout(vbox)
        scroll.setWidget(wgt)
        
        mvbox = QtWidgets.QVBoxLayout()
        mvbox.addWidget(scroll)
        mvbox.addWidget(self.pb_apply)
        mvbox.addWidget(self.pb_reset)
        self.setLayout(mvbox)
        
        self.pb_apply.clicked.connect(self.onApplyClicked)
        self.pb_reset.clicked.connect(self.onResetClicked)
        
    def onApplyClicked(self):
        filterData = FilterStruct()
        
        for i in range(self.setFilter.list_inclusive.count()):
            filterData.setInList.append(self.setFilter.list_inclusive.item(i).text())
        for i in range(self.setFilter.list_exclusive.count()):
            filterData.setExList.append(self.setFilter.list_exclusive.item(i).text())
            
        for i in range(self.rarityFilter.list_inclusive.count()):
            filterData.rarityInList.append(self.rarityFilter.list_inclusive.item(i).text())
        for i in range(self.rarityFilter.list_exclusive.count()):
            filterData.rarityExList.append(self.rarityFilter.list_exclusive.item(i).text())
            
        for i in range(self.stypeFilter.list_inclusive.count()):
            filterData.stypeInList.append(self.stypeFilter.list_inclusive.item(i).text())
        for i in range(self.stypeFilter.list_exclusive.count()):
            filterData.stypeExList.append(self.stypeFilter.list_exclusive.item(i).text())
            
        for i in range(self.typeFilter.list_inclusive.count()):
            filterData.typeInList.append(self.typeFilter.list_inclusive.item(i).text())
        for i in range(self.typeFilter.list_exclusive.count()):
            filterData.typeExList.append(self.typeFilter.list_exclusive.item(i).text())
            
        for i in range(self.utypeFilter.list_inclusive.count()):
            filterData.utypeInList.append(self.utypeFilter.list_inclusive.item(i).text())
        for i in range(self.utypeFilter.list_exclusive.count()):
            filterData.utypeExList.append(self.utypeFilter.list_exclusive.item(i).text())
            
        for i in range(self.attrFilter.table_filter.rowCount()):
            if self.attrFilter.table_filter.item(i, 0).text() == "Мана-стоимость":
                if self.attrFilter.table_filter.item(i, 1).text() == "=":
                    filterData.manacostEqList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == ">":
                    filterData.manacostGrList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == "<":
                    filterData.manacostLessList.append(self.attrFilter.table_filter.item(i, 2).text())
            elif self.attrFilter.table_filter.item(i, 0).text() == "Сила":
                if self.attrFilter.table_filter.item(i, 1).text() == "=":
                    filterData.strengthEqList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == ">":
                    filterData.strengthGrList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == "<":
                    filterData.strengthLessList.append(self.attrFilter.table_filter.item(i, 2).text())
            elif self.attrFilter.table_filter.item(i, 0).text() == "Выносливость":
                if self.attrFilter.table_filter.item(i, 1).text() == "=":
                    filterData.enduranceEqList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == ">":
                    filterData.enduranceGrList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == "<":
                    filterData.enduranceLessList.append(self.attrFilter.table_filter.item(i, 2).text())
            elif self.attrFilter.table_filter.item(i, 0).text() == "Верность":
                if self.attrFilter.table_filter.item(i, 1).text() == "=":
                    filterData.loyaltyEqList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == ">":
                    filterData.loyaltyGrList.append(self.attrFilter.table_filter.item(i, 2).text())
                elif self.attrFilter.table_filter.item(i, 1).text() == "<":
                    filterData.loyaltyLessList.append(self.attrFilter.table_filter.item(i, 2).text())
                    
        for i in range(self.descriptionFilter.list_inclusive.count()):
            filterData.descriptionList.append(self.descriptionFilter.list_inclusive.item(i).text())
            
        filterData.white = self.colorFilter.pb_white.isChecked()
        filterData.blue = self.colorFilter.pb_blue.isChecked()
        filterData.black = self.colorFilter.pb_black.isChecked()
        filterData.red = self.colorFilter.pb_red.isChecked()
        filterData.green = self.colorFilter.pb_green.isChecked()
        filterData.noncolor = self.colorFilter.pb_noncolor.isChecked()
            
        for i in range(self.artistFilter.list_inclusive.count()):
            filterData.artistInList.append(self.artistFilter.list_inclusive.item(i).text())
        for i in range(self.artistFilter.list_exclusive.count()):
            filterData.artistExList.append(self.artistFilter.list_exclusive.item(i).text())
            
        for i in range(self.designFilter.list_inclusive.count()):
            filterData.designInList.append(self.designFilter.list_inclusive.item(i).text())
        for i in range(self.designFilter.list_exclusive.count()):
            filterData.designExList.append(self.designFilter.list_exclusive.item(i).text())  
            
        self.filterApplied.emit(filterData)
    
    def onResetClicked(self):
        self.filterReset.emit()