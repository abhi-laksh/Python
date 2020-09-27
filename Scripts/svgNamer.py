#--- DATE : July 02, 2019 | 20:00:38
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): It renames SVG files exported form AI
about='It renames SVG files exported form AI'
print('About :' + about)
import os
import random
from datetime import datetime as dt
global curDir

curDir = os.getcwd()
token = dt.today().strftime("%d%m%Y%H%M%S")
allSvgs = [each for each in os.listdir(curDir) if os.path.isfile(each) if ".svg" in each and each!=os.path.basename(__file__)]

def getValue(allSvgs):
	idValue = []
	for svgFile in allSvgs:
		pos = []
		svg = open(svgFile,"r").read()
		toStart = svg.find('id=')
		pos.append(int(toStart) + len('id='))
		while True:
			toStart = toStart + len('id=')
			toStart = svg.find('id=',toStart)
			if toStart == -1:
				break
			print(svg[pos[0]])
			pos.append(toStart  + len('id='))
		for i in pos:
			names = []
			name = svg[i+1]
			while name!= '"':
				names.append(name)
				i=i+1
				name=svg[i+1]
			if "layer" not in "".join(names).lower():
				idValue.append("".join(names))
		# print(random.choice(idValue))
		if os.path.isfile(os.path.join(curDir ,  "".join(names) + ".svg")):
			os.rename(svgFile , ("".join(names) + token + ".svg"))
		else:
			os.rename(svgFile , "".join(names) + ".svg")
		idValue.clear()			
getValue(allSvgs)		
for i in range(len(allSvgs)):
	pass