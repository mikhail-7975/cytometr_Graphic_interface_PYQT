from mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore

import random
import math

class CytometrCore:
    def __init__(self):
        self.triggerPort = None
        self.tracer1Port = None
        self.tracer2Port = None

        self.triggerData = []
        self.tracer1Data = []
        self.tracer2Data = []

        self.status = 0

    def readData(self):
        return [200 * math.exp(-((x - 100) / 10)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)], \
               [200 * math.exp(-((x - 700) / 70)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)],\
               [200 * math.exp(-((x - 1400) / 140)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)]

CytoCore = CytometrCore()

class mainWindowController(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainWindowController, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.drawPlot)

        self.connectTracer1_pushButton.clicked.connect(self.connectTracer1_pushButton_clicked)
        self.startStop_button.clicked.connect(self.startStop_button_clicked)

    def drawPlot(self):
        self.graphic.clear()
        trig, tr1, tr2 = CytoCore.readData()
        self.graphic.plot([i for i in range(2000)], trig, pen ='r')
        self.graphic.plot([i for i in range(2000)], tr1, pen ='g')
        self.graphic.plot([i for i in range(2000)], tr2, pen ='b')

    @QtCore.pyqtSlot()
    def connectTracer1_pushButton_clicked(self):
        return 0

    @QtCore.pyqtSlot()
    def startStop_button_clicked(self):
        if CytoCore.status == 0:
            self.timer.start(100)
            CytoCore.status = 1
        else:
            self.timer.stop()
            CytoCore.status = 0
        return 0