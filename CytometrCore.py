print("cytometr core")
try:
    import serial
    import serial.tools.list_ports
except Exception as err:
    print(err)
    input()

class statuses:
    doNothing = 13
    beReady = 12
    sendingData = 11
    reading = 10

class Cytometr_core:
    def __init__(self):
        self.dataLen = 2000
        ports = serial.tools.list_ports.comports(include_links=False)
        self.portNameList = [p.device for p in ports]

        self.triggerPort = None
        self.tracer1Port = None
        self.tracer2Port = None

        self.triggerData = [0] * self.dataLen
        self.tracer1Data = [0] * self.dataLen
        self.tracer2Data = [0] * self.dataLen

        self.trig_upd = 0
        self.tr1_upd = 0
        self.tr2_upd = 0

        self.status = statuses.doNothing

    def readData(self):
        if ((self.trig_upd == 0) and (self.tr1_upd == 0)):
            print("send start")
            if (self.tracer2Port != None):
                self.tracer2Port.write(b'b2')
            if (self.tracer1Port != None):
                self.tracer1Port.write(b'b1')
            if(self.triggerPort != None):
                self.triggerPort.write(b'bt')

        print("try read")
        if(self.tr1_upd == 0): print("tr 1")
        if (self.trig_upd == 0): print("trig")
        triggerData = []
        tracer1Data = []
        tracer2Data = []


        if (self.tracer1Port != None):
            if (self.tracer1Port.inWaiting()):
                buf_trace = self.tracer1Port.read(self.dataLen * 2)
                for i in range(self.dataLen):
                    tracer1Data.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)
                self.tracer1Data = tracer1Data
                self.tr1_upd = 1
                print("New tracer1")
                self.tracer1Port.write(b'ack')

        if (self.tracer2Port != None):
            if (self.tracer2Port.inWaiting()):
                buf_trace = self.tracer2Port.read(self.dataLen * 2)
                for i in range(self.dataLen):
                    tracer2Data.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)
                self.tracer2Data = tracer2Data
                self.tr2_upd = 1
                print("New tracer2")
                self.tracer2Port.write(b'ack')

        if (self.triggerPort != None):
            if (self.triggerPort.inWaiting()):
                buf_trace = self.triggerPort.read(self.dataLen * 2)
                for i in range(self.dataLen):
                    triggerData.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)
                self.triggerData = triggerData
                self.trig_upd = 1
                print("New trigger")
                self.triggerPort.write(b'ack')

        print("trigger = ", self.triggerData)
        print("tracer1 = ", self.triggerData)
            #, tracer1Data, tracer2Data#[200 * math.exp(-((x - 100) / 10)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)], \
               #[200 * math.exp(-((x - 700) / 70)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)],\
               #[200 * math.exp(-((x - 1400) / 140)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)]