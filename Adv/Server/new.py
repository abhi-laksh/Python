#--- DATE : July 10, 2019 | 09:52:27
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Socket Implementation
about='Socket Implementation'
print('About :' + about)
import os
try:
	import socket
except ModuleNotFoundError:
	mods = ['socket']
	for mod in mods:
		os.system('python -m pip install ' + str(mod))
		try:
			import mod
		except Exception as e:
			print(e)
			break

