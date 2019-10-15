#--- DATE : April 09, 2019 | 13:00:03
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about=''
print('About :' + about)
import os
p = "C:\\Users\\Abhishek\\Downloads\\ddownr(1)"
lstNames = []
file = open("a.txt", "r+").read().replace("\n" , "")
lngth = len(file)
i = 0
indices = []
count = 0
while i<lngth:
	each = file[i]
	if each == ",":
		indices.append(i)
	i+=1
for i in range(len(indices)):
	pos = indices[i]
	if (i-1) >= 0:
		prev = file[indices[i-1] + 1: pos ]
		lstNames.append(prev)
	else:
		prev = file[ : pos]
		lstNames.append(prev)
vids = os.listdir(p)

for i in range(len(lstNames)):
	each = lstNames[i]
	try:
		pos = vids.index(each + ".mp4")
		oldName = os.path.join(p , vids[pos])
		newName = os.path.join(p , str(i)+ ". " + vids[pos])
		os.rename(oldName,newName)
	except ValueError:
		print(each+ ".mp4" )
