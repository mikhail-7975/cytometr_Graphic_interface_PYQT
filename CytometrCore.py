import random
import math

import serial
import serial.tools.list_ports

class Cytometr_core:
    def __init__(self):
        self.dataLen = 2000
        ports = serial.tools.list_ports.comports(include_links=False)
        self.portNameList = [p.device for p in ports]

        self.triggerPort = None
        self.tracer1Port = None
        self.tracer2Port = None

        self.triggerData = []
        self.tracer1Data = []
        self.tracer2Data = []

        self.status = 0

    def readData(self):

        #self.tracer1Port.write(b'ack')
        #self.tracer2Port.write(b'ack')
        triggerData = []
        tracer1Data = []
        tracer2Data = []
        if(self.triggerPort != None):
            self.triggerPort.write(b'ack')
            while (not self.triggerPort.inWaiting()):
                print('.0')
            print("begin reading trigger")
            buf_trace = self.triggerPort.read(self.dataLen * 2)
            print(buf_trace)


            for i in range(self.dataLen):
                triggerData.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)

            print(triggerData)
        else:
            triggerData = [0] * 2000

        if (self.tracer1Port != None):
            self.tracer1Port.write(b'ack')
            while (not self.tracer1Port.inWaiting()):
                print('.0')
            print("begin reading trigger")
            buf_trace = self.tracer1Port.read(self.dataLen * 2)
            print(buf_trace)


            for i in range(self.dataLen):
                tracer1Data.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)

            print(tracer1Data)
        else:
            tracer1Data = [0] * 2000

        if (self.tracer2Port != None):
            self.tracer2Port.write(b'ack')
            while (not self.tracer2Port.inWaiting()):
                print('.0')
            print("begin reading trigger")
            buf_trace = self.tracer2Port.read(self.dataLen * 2)
            print(buf_trace)


            for i in range(self.dataLen):
                tracer2Data.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)

            print(tracer2Data)
        else:
            tracer2Data = [0] * 2000
        #plt.plot(trace5)
        '''
        while (not self.tracer1Port.inWaiting()):
            print('.1')

        print("begin reading tracer1")
        buf_trace = self.tracer1Port.read(self.dataLen * 2)
        print(buf_trace)

        tracer1Data = []
        for i in range(self.dataLen):
            tracer1Data.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)

        print(tracer1Data)

        while (not self.tracer2Port.inWaiting()):
            print('.2')

        print("begin reading tracer2")
        buf_trace = self.tracerwPort.read(self.dataLen * 2)
        print(buf_trace)

        tracer2Data = []
        for i in range(self.dataLen):
            tracer2Data.append(buf_trace[2 * i] + buf_trace[2 * i + 1] * 256)

        print(tracer2Data)
        '''
        return triggerData, tracer1Data, tracer2Data#, tracer1Data, tracer2Data#[200 * math.exp(-((x - 100) / 10)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)], \
               #[200 * math.exp(-((x - 700) / 70)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)],\
               #[200 * math.exp(-((x - 1400) / 140)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)]