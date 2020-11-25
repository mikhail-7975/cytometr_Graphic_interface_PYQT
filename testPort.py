import serial

s = serial.Serial('COM12')

while(1):
    str = input()
    s.write(str.encode('utf-8'))

