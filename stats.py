from PyQt6 import QtCore, QtGui, QtWidgets

class Stats(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.setWindowTitle("Статистика")
        self.setMinimumSize(600, 600)
        
        self.statsTree = QtWidgets.QTreeWidget(self)
        self.setStats = QtWidgets.QTreeWidgetItem(["Статистика по сетам"])
        self.rarityStats = QtWidgets.QTreeWidgetItem(["Статистика по редкости"])
        self.stypeStats = QtWidgets.QTreeWidgetItem(["Статистика по супертипам"])
        self.typeStats = QtWidgets.QTreeWidgetItem(["Статистика по типам"])
        self.utypeStats = QtWidgets.QTreeWidgetItem(["Статистика по подтипам"])
        self.colorStats = QtWidgets.QTreeWidgetItem(["Статистика по цветам"])
        self.artistStats = QtWidgets.QTreeWidgetItem(["Статистика по художникам"])
        self.designStats = QtWidgets.QTreeWidgetItem(["Статистика по оформлению"])
        self.foilStats = QtWidgets.QTreeWidgetItem(["Статистика по фойлу"])
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.statsTree)
        self.setLayout(vbox)
        
        self.statsTree.setColumnCount(3)
        self.statsTree.setHeaderLabels(["Название", "Уникальных карт", "Всего карт"])

        items = [self.setStats, self.rarityStats, self.stypeStats, self.typeStats, self.utypeStats, self.colorStats, self.artistStats, self.designStats, self.foilStats]

        self.statsTree.insertTopLevelItems(0, items)
        
        self.statsTree.resizeColumnToContents(0)
        self.statsTree.resizeColumnToContents(1)
        self.statsTree.resizeColumnToContents(2)
        self.statsTree.setSortingEnabled(True)
        
    def setSetStats(self, data):
        self.setStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.setStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setRarityStats(self, data):
        self.rarityStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.rarityStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setSupertypeStats(self, data):
        self.stypeStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.stypeStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setTypeStats(self, data):
        self.typeStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.typeStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setUndertypeStats(self, data):
        self.utypeStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.utypeStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setColorStats(self, data):
        self.colorStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.colorStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setArtistStats(self, data):
        self.artistStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.artistStats.addChild(item)
        
        self.statsTree.resizeColumnToContents(0)
            
    def setDesignStats(self, data):
        self.designStats.takeChildren()
        
        for i in range(len(data)):
            item = QtWidgets.QTreeWidgetItem([data[i][0], str(data[i][1]), str(data[i][2])])
            self.designStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)
            
    def setFoilStats(self, data):
        self.foilStats.takeChildren()
        
        for i in range(len(data)):
            foil = "Фойл" if data[i][0] == 1 else "Не фойл"
            item = QtWidgets.QTreeWidgetItem([foil, str(data[i][1]), str(data[i][2])])
            self.foilStats.addChild(item)
            
        self.statsTree.resizeColumnToContents(0)