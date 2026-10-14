from PyQt6 import QtCore, QtGui, QtWidgets
from cardtable import CardTable
from cardinfo import CardInfo
from search import Search
from filter import Filter
from data import MTGData
from stats import Stats

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent, flags = QtCore.Qt.WindowType.Window | QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("MTG CardBox")
        self.setFixedSize(1050, 800)
        
        menuBar = self.menuBar()
        
        menuApp = menuBar.addMenu("Приложение")
        action = menuApp.addAction("О приложении", self.aboutApp)
        action.setStatusTip("Получение сведений о приложении")
        menuApp.addSeparator()
        action = menuApp.addAction("Выход", QtGui.QKeySequence("Ctrl+Q"), QtWidgets.QApplication.instance().quit)
        action.setStatusTip("Завершение работы программы")
        
        menuFilter = menuBar.addAction("Фильтр", self.filterMenu)
        
        self.menuGroup = menuBar.addMenu("Группировка")
        
        menuStats = menuBar.addAction("Статистика", self.statsMenu)
        
        self.cardTable = CardTable(self)
        self.cardInfo = CardInfo(self)
        self.search = Search(self)
        self.filter = Filter(self)
        self.stats = Stats(self)
        
        self.mtgdata = MTGData("MTG.db")
        
        mainWidget = QtWidgets.QWidget(self)
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        vbox.addWidget(self.cardTable)
        vbox.addWidget(self.search)
        hbox.addLayout(vbox)
        hbox.addWidget(self.cardInfo)
        mainWidget.setLayout(hbox)
        
        self.setCentralWidget(mainWidget)
        
        self.cardTable.cardSelected.connect(self.onCardSelected)
        self.search.searchClicked.connect(self.onSearchClicked)
        self.filter.filterApplied.connect(self.onFilterApplied)
        self.filter.filterReset.connect(self.onFilterReset)
        
        self.cardTable.fillTable(self.mtgdata.fetchMainData())
        self.filter.setFilter.fillComboBox(self.mtgdata.fetchSetNames())
        self.filter.rarityFilter.fillComboBox(self.mtgdata.fetchRarityNames())
        self.filter.stypeFilter.fillComboBox(self.mtgdata.fetchStypeNames())
        self.filter.typeFilter.fillComboBox(self.mtgdata.fetchTypeNames())
        self.filter.utypeFilter.fillComboBox(self.mtgdata.fetchUtypeNames())
        self.filter.artistFilter.fillComboBox(self.mtgdata.fetchArtistNames())
        self.filter.designFilter.fillComboBox(self.mtgdata.fetchDesignNames())
        self.groupMenu()
        self.setStats()
        
    def updateTable(self):
        self.mtgdata.updateFilter()
        self.cardTable.fillTable(self.mtgdata.fetchMainData())
        self.groupMenu()
        self.setStats()
        
    def setStats(self):
        self.stats.setSetStats(self.mtgdata.fetchSetQuantity())
        self.stats.setRarityStats(self.mtgdata.fetchRarityQuantity())
        self.stats.setSupertypeStats(self.mtgdata.fetchSupertypeQuantity())
        self.stats.setTypeStats(self.mtgdata.fetchTypeQuantity())
        self.stats.setUndertypeStats(self.mtgdata.fetchUndertypeQuantity())
        self.stats.setColorStats(self.mtgdata.fetchColorQuantity())
        self.stats.setArtistStats(self.mtgdata.fetchArtistQuantity())
        self.stats.setDesignStats(self.mtgdata.fetchDesignQuantity())
        self.stats.setFoilStats(self.mtgdata.fetchFoilQuantity())
        
    def aboutApp(self):
        QtWidgets.QMessageBox.about(self, "О программе", 
                                    """<center>\"MTG CardBox\" v3.0.0
                                    <br><br>Приложение MTG CardBox позволяет просматривать коллекцию карт из ККИ Magic: The Gathering<sup>TM</sup>.
                                    <br><br>(c) Wizards of the Coast, 2026<br>(c) FaaZMaaR, 2026""")
        
    def filterMenu(self):
        self.filter.show()
    
    def statsMenu(self):
        self.stats.show()
    
    def groupMenu(self):
        self.menuGroup.clear()
        
        if self.mtgdata.groupRarity == "":
            menuRarity = self.menuGroup.addMenu("Редкость")
            for rarity in self.mtgdata.fetchFilteredRarityNames():
                menuRarity.addAction(rarity[0], lambda param = rarity[0]: self.groupRarity(param))
        
        if self.mtgdata.groupSet == "":
            menuSet = self.menuGroup.addMenu("Сет")
            for set_ in self.mtgdata.fetchFilteredSetNames():
                menuSet.addAction(set_[0], lambda param = set_[0]: self.groupSet(param))
        
        colorsAndTypes = self.mtgdata.fetchFilteredColorsAndTypes()
        bWhite = False
        bBlue = False
        bBlack = False
        bRed = False
        bGreen = False
        bMulticol = False
        bNoncol = False
        bNonBase = False
        bBase = False
        bToken = False
        bCreature = False
        bLand = False
        bPW = False
        bArt = False
        bSorc = False
        bInst = False
        bEnch = False
        for i in range(len(colorsAndTypes)):
            if colorsAndTypes[i][0] == "White":
                bWhite = True
            if colorsAndTypes[i][0] == "Blue":
                bBlue = True
            if colorsAndTypes[i][0] == "Black":
                bBlack = True
            if colorsAndTypes[i][0] == "Red":
                bRed = True
            if colorsAndTypes[i][0] == "Green":
                bGreen = True
            if colorsAndTypes[i][1] > 1:
                bMulticol = True
            if colorsAndTypes[i][0] == None:
                bNoncol = True
            if (colorsAndTypes[i][3] != None) and ("Земля" in colorsAndTypes[i][3]) and ((colorsAndTypes[i][2] == None) or ("Базовый" not in colorsAndTypes[i][2])):
                bNonBase = True
            if (colorsAndTypes[i][3] != None) and ("Земля" in colorsAndTypes[i][3]) and (colorsAndTypes[i][2] != None) and ("Базовый" in colorsAndTypes[i][2]):
                bBase = True
            if (colorsAndTypes[i][2] != None) and ("Фишка" in colorsAndTypes[i][2]):
                bToken = True
            if (colorsAndTypes[i][3] != None) and ("Существо" in colorsAndTypes[i][3]):
                bCreature = True
            if (colorsAndTypes[i][3] != None) and ("Земля" in colorsAndTypes[i][3]):
                bLand = True
            if (colorsAndTypes[i][3] != None) and ("Planeswalker" in colorsAndTypes[i][3]):
                bPW = True
            if (colorsAndTypes[i][3] != None) and ("Артефакт" in colorsAndTypes[i][3]):
                bArt = True
            if (colorsAndTypes[i][3] != None) and ("Волшебство" in colorsAndTypes[i][3]):
                bSorc = True
            if (colorsAndTypes[i][3] != None) and ("Мгновенное заклинание" in colorsAndTypes[i][3]):
                bInst = True
            if (colorsAndTypes[i][3] != None) and ("Чары" in colorsAndTypes[i][3]):
                bEnch = True
        
        if self.mtgdata.groupColor == "":
            menuColor = self.menuGroup.addMenu("Цвет")
            if bWhite: menuColor.addAction("Белый", lambda param = "Белый": self.groupColor(param))
            if bBlue: menuColor.addAction("Синий", lambda param = "Синий": self.groupColor(param))
            if bBlack: menuColor.addAction("Черный", lambda param = "Черный": self.groupColor(param))
            if bRed: menuColor.addAction("Красный", lambda param = "Красный": self.groupColor(param))
            if bGreen: menuColor.addAction("Зеленый", lambda param = "Зеленый": self.groupColor(param))
            if bMulticol: menuColor.addAction("Многоцветный", lambda param = "Многоцветный": self.groupColor(param))
            if bNoncol: menuColor.addAction("Бесцветный", lambda param = "Бесцветный": self.groupColor(param))
            if bNonBase: menuColor.addAction("Небазовая земля", lambda param = "Небазовая земля": self.groupColor(param))
            if bBase: menuColor.addAction("Базовая земля", lambda param = "Базовая земля": self.groupColor(param))
            if bToken: menuColor.addAction("Фишка", lambda param = "Фишка": self.groupColor(param))
        
        if self.mtgdata.groupType == "":
            menuType = self.menuGroup.addMenu("Тип")
            if bCreature: menuType.addAction("Существо", lambda param = "Существо": self.groupType(param))
            if bLand: menuType.addAction("Земля", lambda param = "Земля": self.groupType(param))
            if bPW: menuType.addAction("Planeswlaker", lambda param = "Planeswlaker": self.groupType(param))
            if bArt: menuType.addAction("Артефакт", lambda param = "Артефакт": self.groupType(param))
            if bSorc: menuType.addAction("Волшебство", lambda param = "Волшебство": self.groupType(param))
            if bInst: menuType.addAction("Мгновенное заклинание", lambda param = "Мгновенное заклинание": self.groupType(param))
            if bEnch: menuType.addAction("Чары", lambda param = "Чары": self.groupType(param))
        
        self.menuGroup.addAction("Сброс", self.groupReset)
    
    def groupRarity(self, rarity):
        self.mtgdata.groupRarity = rarity
        self.updateTable()
    
    def groupSet(self, set_):
        self.mtgdata.groupSet = set_
        self.updateTable()
    
    def groupColor(self, color):
        self.mtgdata.groupColor = color
        self.updateTable()
    
    def groupType(self, type):
        self.mtgdata.groupType = type
        self.updateTable()
    
    def groupReset(self):
        self.mtgdata.clearGroup()
        self.updateTable()
    
    def onCardSelected(self, id):
        self.cardInfo.data = self.mtgdata.fetchCardInfo(id)
        self.cardInfo.currentInfo = 0
        self.cardInfo.fillInfo()
        if len(self.cardInfo.data) > 1:
            self.cardInfo.pb_change.setEnabled(True)
        else:
            self.cardInfo.pb_change.setEnabled(False)
            
    def onSearchClicked(self, searchStr):
        self.mtgdata.searchName = searchStr
        self.updateTable()
        
    def onFilterApplied(self, filterData):
        self.mtgdata.filterSetIn = filterData.setInList
        self.mtgdata.filterSetEx = filterData.setExList
        self.mtgdata.filterRarityIn = filterData.rarityInList
        self.mtgdata.filterRarityEx = filterData.rarityExList
        self.mtgdata.filterStypeIn = filterData.stypeInList
        self.mtgdata.filterStypeEx = filterData.stypeExList
        self.mtgdata.filterTypeIn = filterData.typeInList
        self.mtgdata.filterTypeEx = filterData.typeExList
        self.mtgdata.filterUtypeIn = filterData.utypeInList
        self.mtgdata.filterUtypeEx = filterData.utypeExList
        self.mtgdata.filterArtistIn = filterData.artistInList
        self.mtgdata.filterArtistEx = filterData.artistExList
        self.mtgdata.filterDesignIn = filterData.designInList
        self.mtgdata.filterDesignEx = filterData.designExList
        self.mtgdata.filterManacostEq = filterData.manacostEqList
        self.mtgdata.filterManacostGr = filterData.manacostGrList
        self.mtgdata.filterManacostLess = filterData.manacostLessList
        self.mtgdata.filterStrengthEq = filterData.strengthEqList
        self.mtgdata.filterStrengthGr = filterData.strengthGrList
        self.mtgdata.filterStrengthLess = filterData.strengthLessList
        self.mtgdata.filterEnduranceEq = filterData.enduranceEqList
        self.mtgdata.filterEnduranceGr = filterData.enduranceGrList
        self.mtgdata.filterEnduranceLess = filterData.enduranceLessList
        self.mtgdata.filterLoyaltyEq = filterData.loyaltyEqList
        self.mtgdata.filterLoyaltyGr = filterData.loyaltyGrList
        self.mtgdata.filterLoyaltyLess = filterData.loyaltyLessList
        self.mtgdata.filterDescription = filterData.descriptionList
        self.mtgdata.filterWhite = filterData.white
        self.mtgdata.filterBlue = filterData.blue
        self.mtgdata.filterBlack = filterData.black
        self.mtgdata.filterRed = filterData.red
        self.mtgdata.filterGreen = filterData.green
        self.mtgdata.filterNoncolor = filterData.noncolor
        self.updateTable()
    
    def onFilterReset(self):
        self.mtgdata.clearFilter()
        self.updateTable()