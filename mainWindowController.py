from mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore

import random

class mainWindowController(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainWindowController, self).__init__(parent)
        self.setupUi(self)

        self.connectTracer1_pushButton.clicked.connect(self.connectTracer1_pushButton_clicked)
        self.startStop_button.clicked.connect(self.startStop_button_clicked)

    def drawPlot(self):
        self.graphic.clear()
        self.graphic.plot([i for i in range(100)], [random.randint(-5, 5) for i in range(100)], pen ='g')
        self.graphic.plot([i for i in range(100)], [random.randint(-5, 5) for i in range(100)], pen ='b')

    @QtCore.pyqtSlot()
    def connectTracer1_pushButton_clicked(self):
        return 0

    @QtCore.pyqtSlot()
    def startStop_button_clicked(self):
        self.drawPlot()
        return 0