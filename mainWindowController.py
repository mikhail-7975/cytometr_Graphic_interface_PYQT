print("main window controller")
try:
    from mainWindow import Ui_MainWindow
    from PyQt5 import QtWidgets, QtCore

    from CytometrCore import *
except Exception as err:
    print(err)
    input()

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
        self.setTriggerSettings_pushButton.clicked.connect(self.setTrigger_clicked)
        self.setTracer1Settings_pushButton.clicked.connect(self.setTracer1_clicked)
        self.setTracer2Settings_pushButton.clicked.connect(self.setTracer2_clicked)

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

        x = [i for i in range(CytoCore.dataLen * 2)]
        CytoCore.readData()
        if((CytoCore.trig_upd == 1) and (CytoCore.tr1_upd == 1)):# and (CytoCore.tr2_upd == 1)):
            tr = CytoCore.triggerData + [-1 for i in range(CytoCore.dataLen)]
            tr1 = [-1 for i in range(CytoCore.dataLen)] + CytoCore.tracer1Data
            tr2 = [-1 for i in range(CytoCore.dataLen)] + CytoCore.tracer2Data
            self.graphic.clear()
            self.graphic.plot(x, tr, pen ='r')
            self.graphic.plot(x, tr1, pen ='g')
            self.graphic.plot(x, tr2, pen ='b')
            CytoCore.tr2_upd = 0
            CytoCore.tr1_upd = 0
            CytoCore.trig_upd = 0
            #CytoCore.tracer1Updated = 0

    @QtCore.pyqtSlot()
    def connectTrigger_clicked(self):
        if CytoCore.triggerPort == None:
            print("connecting to", self.triggerPort_comboBox_value)
            CytoCore.triggerPort = serial.Serial(self.triggerPort_comboBox_value)
            self.connectTrigger_pushButton.setText("connected " + self.triggerPort_comboBox_value)
            #CytoCore.triggerPort.write(b'ack')
        else:
            CytoCore.triggerPort.__del__()
            CytoCore.triggerPort = None
            self.connectTrigger_pushButton.setText("connect")
        # portName = self.triggerPort_comboBox.
        return 0

    @QtCore.pyqtSlot()
    def connectTracer1_clicked(self):
        if CytoCore.tracer1Port == None:
            print("connecting to", self.tracer1Port_comboBox_value)
            CytoCore.tracer1Port = serial.Serial(self.tracer1Port_comboBox_value)
            self.connectTracer1_pushButton.setText("connected " + self.tracer1Port_comboBox_value)
            #CytoCore.tracer1Port.write(b'ack')
        else:
            CytoCore.tracer1Port.__del__()
            CytoCore.tracer1Port = None
            self.connectTracer1_pushButton.setText("connect")
        # portName = self.triggerPort_comboBox.
        return 0

    @QtCore.pyqtSlot()
    def connectTracer2_clicked(self):
        if CytoCore.tracer2Port == None:
            print("connecting to", self.tracer2Port_comboBox_value)
            CytoCore.tracer2Port = serial.Serial(self.tracer2Port_comboBox_value)
            self.connectTracer2_pushButton.setText("connected " + self.tracer2Port_comboBox_value)
            #CytoCore.tracer2Port.write(b'ack')
        else:
            CytoCore.tracer2Port.__del__()
            CytoCore.tracer2Port = None
            self.connectTracer2_pushButton.setText("connect")
        # portName = self.triggerPort_comboBox.
        return 0

    @QtCore.pyqtSlot()
    def startStop_button_clicked(self):
        if CytoCore.status == statuses.doNothing:
            self.startStop_button.setText("stop")
            self.timer.start(10)

            CytoCore.status = statuses.beReady
        else:
            self.timer.stop()
            CytoCore.status = statuses.doNothing
            if (CytoCore.triggerPort != None):
                CytoCore.triggerPort.write(b'end')
            if (CytoCore.tracer1Port != None):
                CytoCore.tracer1Port.write(b'end')
            if (CytoCore.tracer2Port != None):
                CytoCore.tracer2Port.write(b'end')
            self.startStop_button.setText("start")
        return 0

    @QtCore.pyqtSlot()
    def setTrigger_clicked(self):
        if CytoCore.triggerPort != None:
            msg = "st" + self.triggerLevel_lineEdit.text() + 'g' + self.gain_lineEdit.text() + '.'
            CytoCore.triggerPort.write(msg.encode('utf-8'))
        return 0

    @QtCore.pyqtSlot()
    def setTracer1_clicked(self):
        if CytoCore.triggerPort != None:
            msg = "st" + "0000" + 'g' + self.tracer1gain_lineEdit.text() + '.'
            CytoCore.tracer1Port.write(msg.encode('utf-8'))
        return 0

    @QtCore.pyqtSlot()
    def setTracer2_clicked(self):
        if CytoCore.tracer2rPort != None:
            msg = "st" + "0000" + 'g' + self.tracer2gain_lineEdit.text() + '.'
            CytoCore.tracer2Port.write(msg.encode('utf-8'))
        return 0