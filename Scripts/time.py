#--- DATE : May 09, 2019 | 08:28:13
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about='Sets Time'
print('About :' + about)
import os
import time
try:
    import ntplib
    import admin
except ModuleNotFoundError:
	mods = ['admin' , 'ntlib']
	for e in mods:
		os.system("python -m pip install " + e)

try:
	import ntplib
	client = ntplib.NTPClient()
	response = client.request('pool.ntp.org')
	print(time.strftime('%H:%M:%S',time.localtime(response.tx_time)))
	os.system('date ' + time.strftime('%d-%m-%Y',time.localtime(response.tx_time)))
	os.system('time ' + time.strftime('%H:%M:%S',time.localtime(response.tx_time)))
except:
	print('Could not sync with time server. ( Check internet connection )')
	ch = input("Press Enter to exit : ")
