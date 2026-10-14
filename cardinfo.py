from PyQt6 import QtCore, QtGui, QtWidgets
from cardimage import CardImage

class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()

class CardInfo(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFixedWidth(320)
        
        self.lb_image = ClickableLabel(self)
        self.lb_name = QtWidgets.QLabel(self)
        self.lb_type = QtWidgets.QLabel(self)
        self.lb_manacost = QtWidgets.QLabel(self)
        self.lb_attrs = QtWidgets.QLabel(self)
        self.lb_description = QtWidgets.QLabel(self)
        self.pb_change = QtWidgets.QPushButton("Сменить", self)
        self.dialog_image = CardImage(self)
        
        self.data = []
        self.currentInfo = 0
        
        vbox = QtWidgets.QVBoxLayout()
        hbox1 = QtWidgets.QHBoxLayout()
        hbox2 = QtWidgets.QHBoxLayout()
        hbox1.addWidget(self.lb_name, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        hbox1.addWidget(self.lb_manacost, alignment = QtCore.Qt.AlignmentFlag.AlignRight)
        hbox2.addWidget(self.lb_type, alignment = QtCore.Qt.AlignmentFlag.AlignLeft)
        hbox2.addWidget(self.lb_attrs, alignment = QtCore.Qt.AlignmentFlag.AlignRight)
        vbox.addWidget(self.lb_image)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.lb_description)
        vbox.addWidget(self.pb_change)
        self.setLayout(vbox)
        
        self.lb_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_image.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lb_description.setWordWrap(True)
        self.pb_change.setEnabled(False)
        
        self.lb_image.clicked.connect(self.onLabelClicked)
        self.pb_change.clicked.connect(self.onChangeClicked)
        
    def fillInfo(self):
        self.lb_name.setText(self.data[self.currentInfo][0])
        #self.lb_image = QtWidgets.QLabel(self)
        typeStr = ""
        if(self.data[self.currentInfo][1] != None):
            typeStr += self.data[self.currentInfo][1]
        if(self.data[self.currentInfo][2] != None):
            if typeStr != "":
                typeStr += " - "
            typeStr += self.data[self.currentInfo][2]
        if(self.data[self.currentInfo][3] != None):
            if typeStr != "":
                typeStr += " - "
            typeStr += self.data[self.currentInfo][3]
        self.lb_type.setText(typeStr)
        if self.data[self.currentInfo][4] != None:
            self.lb_manacost.setText(str(self.data[self.currentInfo][4]))
        else:
            self.lb_manacost.setText("")
        attrStr = ""
        if self.data[self.currentInfo][5] != None and self.data[self.currentInfo][6] != None:
            attrStr += str(self.data[self.currentInfo][5]) + "/" + str(self.data[self.currentInfo][6])
        elif self.data[self.currentInfo][7] != None:
            attrStr += str(self.data[self.currentInfo][7])
        self.lb_attrs.setText(attrStr)
        self.lb_description.setText(self.data[self.currentInfo][8])
        
        number = self.data[self.currentInfo][10]
        if self.currentInfo == 1:
            number += 1000
        imgPath = ""
        if self.data[self.currentInfo][1] != None and "Фишка" in self.data[self.currentInfo][1]:
            imgPath = f"Pictures/T{self.data[self.currentInfo][9]}/{number:03}.jpg"
        else:
            imgPath = f"Pictures/{self.data[self.currentInfo][9]}/{number:03}.jpg"
        image = QtGui.QPixmap(imgPath)
        if image.isNull():
            print(imgPath)
        else:
            scaled = image.scaled(150, 240, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
            self.lb_image.setPixmap(scaled)
            self.lb_image.resize(scaled.width(), scaled.height())
            self.dialog_image.lb_image.setPixmap(image)
            self.dialog_image.setWindowTitle(self.data[self.currentInfo][0])
        
    def onLabelClicked(self):
        self.dialog_image.show()
        
    def onChangeClicked(self):
        self.currentInfo = 0 if self.currentInfo == 1 else 1
        self.fillInfo()