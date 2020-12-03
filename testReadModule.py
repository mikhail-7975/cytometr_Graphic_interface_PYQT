print("import serial: ...")
try:
	import serial
except Exception as Err:
	print(Err)
	input()
print("import serial: ok")

#port = input()
try:
	s = serial.Serial('COM3')
except Exception:
	print("error")
	input()

print("port opened")


inp = ""
while(inp != "x"):
	str = b''
	while(s.inWaiting()):
		str += s.read()
	if(str != b''):
		print("COM3", str)
		print()
		print()
	#inp = input()	  