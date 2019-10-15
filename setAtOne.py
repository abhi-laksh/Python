#--- DATE : May 18, 2019 | 18:32:13
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Pull particular file type (jpg,txt) from different dirs* and put to single dir*.
about='Pull particular file type (jpg, txt) from different dirs* and put to single dir*'
print('About :' + about)

import os
import shutil
fileType = '.ttf'
curDir = os.getcwd()
allDir = [(root , f) for root , dirs , file in os.walk(curDir) for f in file if fileType in f]

# runas /noprofile /user:Administrator cmd
# copy 'AdventPro-Bold.ttf' '%WINDIR%\Fonts'
# reg add 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts' /v 'FontName (TrueType)' /t REG_SZ /d FontName.ttf /f

try:
	ch = 'allItems' 
	os.mkdir(ch)
except FileExistsError:
	ch = input("Folder 'allItems' already exists ! Enter another name : ")
	os.mkdir(ch)

for path , name in allDir:
	# print( os.path.join(curDir, ch))
	shutil.move(os.path.join(path,name) , os.path.join(curDir, ch))