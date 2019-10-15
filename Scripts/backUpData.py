#--- DATE : September 28, 2019 | 14:03:23
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about='Checks File , if detects changes it backups it.'
print('About : ' + about)
import os

currDir = os.getcwd()

a = []
for name in os.listdir():
	inf = os.stat(name)
	print(os.path.basename(name) + " "+ str(os.path.getmtime(name)))
	# print(os.path.basename(name) + " "+ str(inf.st_size) + " " + str(inf.st_ctime))
	a.append(os.path.getmtime(name))
	print()
print("AMx : " , max(a)) 