import random
import math

import serial
import serial.tools.list_ports

class Cytometr_core:
    def __init__(self):
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
        return [200 * math.exp(-((x - 100) / 10)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)], \
               [200 * math.exp(-((x - 700) / 70)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)],\
               [200 * math.exp(-((x - 1400) / 140)**2 / 2) + random.randint(-10, 10) for x in range(0, 2000)]