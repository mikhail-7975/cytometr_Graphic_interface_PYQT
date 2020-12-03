import os
from multiprocessing import Process

def f(name):
	print('hello com3', name)
	os.system("testReadModule.py")

def f2(name):
	print('hello com7', name)
	os.system("testReadModuleCOM7.py")

if __name__ == '__main__':
	p1 = Process(target=f, args=('bob',))
	p2 = Process(target=f2, args=('bob',))
	p1.start()
	p2.start()
	p1.join()
	p2.join()