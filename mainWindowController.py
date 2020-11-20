from mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore

from CytometrCore import *

CytoCore = Cytometr_core()

class mainWindowController(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainWindowController, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.drawPlot)

        #settings for trigger combo box
        for i in range(len(CytoCore.portNameList)):
            self.triggerPort_comboBox.addItem(CytoCore.portNameList[i], i + 1)
        self.triggerPort_comboBox.addItem("...", 0)
        self.triggerPort_comboBox.setCurrentText("...")
        self.triggerPort_comboBox_value = "..."

        # settings for tracer1 combo box
        for i in range(len(CytoCore.portNameList)):
            self.tracer1Port_comboBox.addItem(CytoCore.portNameList[i], i + 1)
        self.tracer1Port_comboBox.addItem("...", 0)
        self.tracer1Port_comboBox.setCurrentText("...")
        self.tracer1Port_comboBox_value = "..."

        # settings for tracer2 combo box
        for i in range(len(CytoCore.portNameList)):
            self.tracer2Port_comboBox.addItem(CytoCore.portNameList[i], i + 1)
        self.tracer2Port_comboBox.addItem("...", 0)
        self.tracer2Port_comboBox.setCurrentText("...")
        self.tracer2Port_comboBox_value = "..."

        #self.connectTracer1_pushButton.clicked.connect(self.connectTracer1_clicked)
        self.startStop_button.clicked.connect(self.startStop_button_clicked)

        self.connectTrigger_pushButton.clicked.connect(self.connectTrigger_clicked)
        self.connectTracer1_pushButton.clicked.connect(self.connectTracer1_clicked)
        self.connectTracer2_pushButton.clicked.connect(self.connectTracer2_clicked)

        self.triggerPort_comboBox.activated.connect(self.triggerPortNameComboboxHandler)
        self.tracer1Port_comboBox.activated.connect(self.tracer1PortNameComboboxHandler)
        self.tracer2Port_comboBox.activated.connect(self.tracer2PortNameComboboxHandler)

    def triggerPortNameComboboxHandler(self, idx):
        self.triggerPort_comboBox_value = self.triggerPort_comboBox.itemText(idx)

    def tracer1PortNameComboboxHandler(self, idx):
        self.tracer1Port_comboBox_value = self.tracer1Port_comboBox.itemText(idx)

    def tracer2PortNameComboboxHandler(self, idx):
        self.tracer2Port_comboBox_value = self.tracer2Port_comboBox.itemText(idx)

    def drawPlot(self):
        self.graphic.clear()
        x = [i for i in range(2000)]
        trig, tr1, tr2 = CytoCore.readData()
        self.graphic.plot(x, trig, pen ='r')
        self.graphic.plot(x, tr1, pen ='g')
        self.graphic.plot(x, tr2, pen ='b')

    @QtCore.pyqtSlot()
    def connectTrigger_clicked(self):
        print("connecting to", self.triggerPort_comboBox_value)
        # portName = self.triggerPort_comboBox.
        return 0

    @QtCore.pyqtSlot()
    def connectTracer1_clicked(self):
        print("connecting to", self.tracer1Port_comboBox_value)
        # portName = self.triggerPort_comboBox.
        return 0

    @QtCore.pyqtSlot()
    def connectTracer2_clicked(self):
        print("connecting to", self.tracer2Port_comboBox_value)
        # portName = self.triggerPort_comboBox.
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

