

#--- DATE : March 30, 2019 | 17:58:26
#---  ---  By Abhishek Soni 
#--- About : This file creates new python file

import os
from datetime import datetime as dt
import sys

def createFile(pyVer ,fname , header ,uniq=""):
	
	
	if uniq=="":
		pyName = fname + ".py"
		if pyVer[0] == "2":
			import io
			with io.open(pyName , "w+" , encoding="utf8" ) as newFile:
				newFile.write(header)
		else:
			with open(pyName , "w+" , encoding="utf8") as newFile:
				newFile.write(header)
	else:
		setName = fname + uniq + ".py"
		if pyVer[0] == "2":
			import io
			with io.open(setName , "w+" , encoding="utf8" ) as newFile:
				newFile.write(header)
		else:
			with open(setName , "w+" , encoding="utf8") as newFile:
				newFile.write(header)

def main():
	
	fileName = "new"
	currentFolder = os.getcwd()
	exist = os.path.isfile(os.path.join(currentFolder , fileName + ".py" ))
	todays = dt.today().strftime("%B %d, %Y | %H:%M:%S")
	token = dt.today().strftime("%d%m%Y%H%M%S")
	pyVer = sys.version[0:5]
	# header = u"#--- DATE : " + todays + "\n#---  ---  By Abhishek Soni \n#--- About :"
	header = u"#--- DATE : " + todays + "\n#---  ---  By Abhishek Soni \n#--- About (also write in below variable): \nabout=''\nprint('About :' + about)"
	if not exist:
		## pyFile = open(pyName,  "w" ,encoding="utf-8"  )
		createFile(pyVer , fileName , header)
	else:
		createFile(pyVer , fileName,header , token)

if __name__=="__main__":
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
