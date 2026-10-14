from PyQt6 import QtCore, QtGui, QtWidgets

class CardImage(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.lb_image = QtWidgets.QLabel(self)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.lb_image)
        self.setLayout(vbox)