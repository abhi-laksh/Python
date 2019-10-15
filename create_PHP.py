#-----------------------------------------------------------------------------------------# 
#    																					  #
#    This script creates a Web Design Architecture. See below to know more :		      #
#      																				      #
#    1. Dictionary's Key is name of directory , whose value is a list of name of          #
#       files in that directory.													      #
#             																		      #
#    2. If want to create subFolders, then use dictionary in that list, following the     #
#       instruction (1).																  #
#																						  #
#-----------------------------------------------------------------------------------------#

#---------------------------------# 
#    							  #
#    Author : Abhishek Soni		  #
#    Format : UTF- 8			  #
#    About : CREATE WEB DESIGN    #
#    		  FOLDER STRUCTURE 	  #
#             					  #
#---------------------------------#
about='Create Web Design Folder Structure'
print('About : ' + about)
print("Creating...")
import os
from datetime import datetime as dt
import shutil
import sys

# --- Creates File
def createFile(pyVer,fname):
	if pyVer[0] == "2":
		import io
		io.open(fname , "w+" , encoding="utf8")
	else:
		open(fname , "w+" , encoding="utf8")
# --- Writes into File
def writeFile(pyVer , fname , content):
	if pyVer[0] == "2":
		import io
		with io.open(fname , "a") as newFile:
			newFile.write(content)
	else:
		with open(fname , "a") as newFile:
			newFile.write(content)
# --- Different Content to diff file
def writeContent(webFolder):
	strs = os.walk(webFolder)
	allDirs = os.listdir(webFolder)
	pyVer = sys.version[0:5]
	jsFiles = []
	cssFiles = []
	for root , dirs , f in strs:
		for each in f:
			if ".scss" in each:
				if "_" not in each:
					mainFile = each
					mainPath = root
				else:
					absPath = os.path.join(root , each)
					fName = each.split(".")
					relPaths = os.path.join(os.path.relpath(root ,mainPath) , fName[0][1:]).replace("\\" , "/")
					cnt = '@import "'+ relPaths + '";\n'
					writeFile(pyVer , os.path.join(mainPath,mainFile) , cnt)
			else:
				if ".css"  in each:
					absPath = os.path.join(root , each)
					relPaths = os.path.join(os.path.relpath(root ,webFolder) , each).replace("\\" , "/")
					cssFiles.append(relPaths)
				elif ".js"  in each:
					absPath = os.path.join(root , each)
					relPaths = os.path.join(os.path.relpath(root ,webFolder) , each).replace("\\" , "/")
					jsFiles.append(relPaths)
	for e in allDirs:
		if e == "index.php":
			cnt = '''<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<meta content="width=device-width ,  initial-scale=1.0" name="viewport">\n\t\t<!-- CSS Libraries -->\n\t\t'''
			for each in cssFiles:
				cnt += '<link href="'+ each + '" rel="stylesheet">\n\t\t'
			cnt += '''\n\t\t<title>\n\t\t\tMy Document\n\t\t</title>\n\t</head>\n\t<body>\n\t<!-- All Javascript/Jqueries -->\n\t\t'''
			for each in jsFiles:
				cnt +='<script src="'+ each + '"></script>\n\t\t'
			cnt += '''\n\t</body>\n</html>'''
			writeFile(pyVer , os.path.join(webFolder , e) , cnt)
# --- Create Project Structure
def create_web_proj(struct):
	global curDir , webFolder
	# infos = str(struct)
	toCopy = "sass.py"
	pyVer = sys.version[0:5]
	mainDir = list(struct.keys())
	token = dt.today().strftime("%d_%m_%Y_%H_%M_%S")
	for k in mainDir:
		if "WEB_PHP" in k:
			withDate = k + "_" + token
			subDir = os.path.join(curDir,withDate)
			curDir = subDir
			os.mkdir(curDir)
			webFolder = curDir
			shutil.copy(toCopy,webFolder)
		else:
			subDir = os.path.join(curDir,k)
			curDir = subDir
			os.mkdir(curDir)
			
		val = struct[k]
		if type(val) != str:
			for each in val:
				if type(each) == str:
					if "." in each:
						dist = os.path.join(curDir , each)
						createFile(pyVer,dist)
					else:
						subF = os.path.join(curDir , each)
						os.mkdir(subF)
				elif type(each) == list:
					print("Found List ---- " , each)
				elif type(each) == dict:
					create_web_proj(each)
			if "WEB_PHP" not in k:
				curDir= os.path.join(curDir , "..")
		else:
			print("Other --- " ,val)
def main():
	global curDir , webFolder
	curDir = os.getcwd()
	toCreate = {
	"WEB_PHP": [
					{
						"css" : ["a.css"]
					} ,
					{
						"layouts" : [
										{
											"commons" : [] , 
										}
									]
					},
					"images" ,
					"pages",
					{
						"js":["main.js","a.js"]
					} ,
					"index.php" ,
					"config.php" ,
					"connection.php" ,
					"main.css",
					
					{
					"sass" : ["main.scss" ,
								{
									"abstracts" : ["_functions.scss" , "_mixins.scss" , "_varibales.scss"]
								} , 
								{
									"base"	: ["_base.scss" , "_animation.scss" , "_keyframes.scss" , "_responsive.scss" , "_typography.scss"]
								} , 
								{
									"components" : ["_form.scss" , "_input.scss" , "_button.scss" , "_links.scss" , "_messages.scss" , "_others.scss", "_icons.scss"]
								} ,
								{
									"layouts" : ["_flexbox.scss" , "_header.scss" , "_footer.scss"]
								} , 
								{
									"pages" : ["_home.scss"]
								}]
					} 
					]
	}
	create_web_proj(toCreate)
	writeContent(webFolder)

if __name__=="__main__":
	main()
