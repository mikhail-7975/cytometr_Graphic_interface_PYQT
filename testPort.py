import serial
import serial.tools.list_ports

import  matplotlib.pyplot as plt

ports = serial.tools.list_ports.comports(include_links=False)
portNameList = [p.device for p in ports]
print(portNameList)

print("input port name:")
#portName = input()


s = serial.Serial('COM3')


print("ready to read...")
s.write(b'b0')
while(1):
    inp = b''
    while(len(inp) < 14000):
        if(s.inWaiting()):
            inp += s.read_all()
            print(inp)
            y_ = [i for i in inp]
            print(len(y_), y_)
            print(len(inp))

    #print("type(inp[0])", type(inp[0]))
    #print("ord(inp[0]) =", ord(inp[0]))
    #print("decoded:", inp.decode('utf-8'))
    y = [i for i in inp]
    print(len(y), y)
    plt.plot(y, 'x-')
    plt.show()
    #input()
    s.write(b'b0')
