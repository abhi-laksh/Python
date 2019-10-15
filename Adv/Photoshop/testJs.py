#  ----  Created : 20 January 2019 15:42 ( GMT+5:30 )
	# by --- Abhishek Soni ( Special thanks to Samprit Sarkar )
# !! This code writes JS sript for PS while extracting data from excel. !!

import os
try:
	import pandas as pd
except ImportError:
	modules=['pandas' ,'xlrd']
	for mod in modules:
		os.system("python -m pip install " + mod)
	import pandas as pd


file = input("Path of excel file : ").replace("\\","/") 
path = input("Path to save code file : ").replace("\\","/")
name = input("Enter name of the code file (without EXT) : ").replace(" ","_")
data = pd.read_excel(file)

#~~~~~~ These layer names must be present in PSD File
# (Others are student_name , course_name) will be fetched automatically for excel
layerNames =['start_day','start_super','start_month','end_day','end_super','end_month','student_name','course_name','college_name' , 'reg_id']
layerContents=[]


# jsonArr={}

# ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   

	# -----   Find Month from a number

def fixMonth(number):
	month = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' ,'Jun' , 'Jul' , 'Aug' , 'Sep', 'Oct', 'Nov' , 'Dec']
	if '0' in number[0]:
		# mm = 'January'
		ind = int(number[1]) - 1
		mm = month[ind]
	else:
		ind = int(number) -1
		mm = month[ind]
	return mm

	# -----   YY to YYYY

def fixYear(year):
	if len(year) ==2:
		yr = '20'+ year
	else:
		yr = year
	return yr

	# -----   d to dd
def fixDate(num):
	if len(num)==1:
		date = '0' + num
	else:
		date = num
	return date
# ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===  ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===  ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   === 
def setSuperScript(day):
	if day[1] == '1':
		if day== '11':
			supScrpt = 'th'
			return supScrpt
		else:
			supScrpt = 'st'
			return supScrpt
	elif day[1] == '2':
		if day== '12':
			supScrpt = 'th'
			return supScrpt
		else:
			supScrpt = 'nd'
			return supScrpt
	elif day[1] == '3':
		if day== '13':
			supScrpt = 'th'
			return supScrpt
		else:
			supScrpt = 'rd'
			return supScrpt
	else:
		supScrpt = 'th'
		return supScrpt

# || || ||    ===    Handles Excel Data   ===    || || ||    

def handleExcel(excelFile):
	
	
	for key in excelFile:
		valArr=[]
		day = []
		yr = []
		sup = []
		for ind in range(len(excelFile[key])):
			vals = excelFile[key][ind]
			if len(vals) != 0:
				raw=vals.lower().replace(" ","")
				if raw.isalpha() == True and raw.istitle() == False:
					vals.title()
					# print(vals)
					valArr.append(vals)
				else:
					checker = vals.split(".")
					if len(checker) == 3:
						dd , mm , yy = vals.split(".")
						month = fixMonth(mm)
						year = fixYear(yy)
						date = fixDate(dd)
						superScript = setSuperScript(date)
						wrdDate = month + ", " + year
						yr.append(wrdDate)
						day.append(date)
						sup.append(superScript)
					else:
						raise ValueError("Invalid Date format detected : ", vals)
			else:
				print("Blank value found after :" , excelFile[key][ind-1])

		# jsonArr[key.lower().replace(" ","_")] = valArr
		if len(valArr)!= 0 :
			layerContents.append(valArr)
		if len(sup)!= 0 and len(yr)!=0 and len(day)!=0:
			layerContents.append(sup)
			layerContents.append(day)
			layerContents.append(yr)
		if key.lower().replace(" ","_") != 'start_date' and key.lower().replace(" ","_") !='end_date':
			layerNames.append(key.lower().replace(" ","_"))



handleExcel(data)

# || || ||    ===    Writes JS   ===    || || || 

def generateJS(layers,contents,pathForJS='' , nameOfJS = '-_-Untitled-_-'):
	js_code = '''var textLayers = ''' + str(layers) + ''';
	var values =  ''' + str(contents) + ''';
	var pathPsd=prompt("Enter the path of psd","C:\\\\>>>").replace("\\\\","\\\\\\\\");
	var pathJpg = prompt("Enter the path to save JPG","C:\\\\\\>>>").replace("\\\\","\\\\\\\\")
	var fixedPath = pathJpg
	var psdFile = new File(pathPsd);  
	var saveName = "";
	var layerName = "";
	var val = "";
	if(psdFile.exists){

	    app.open(psdFile);
	    function textLayrr (layers,changes) {

	    	var names = changes[0]

	    	var start_spr = changes[1]
	    	var start_day = changes[2]
	    	var start_mnth = changes[3]
	    	

			var end_spr = changes[4]
	    	var end_day = changes[5]
	    	var end_mnth = changes[6]

	    	var course = changes[7]

	      for (i = 0 ; i< names.length ; i++){

	      	val = []

	      	val.push(start_day[i])
	      	val.push(start_spr[i])
	      	val.push(start_mnth[i])

	      	val.push(end_day[i])
	      	val.push(end_spr[i])
	      	val.push(end_mnth[i])

	      	val.push(names[i])
	      	val.push(course[i])

	      	for (var j = 0; j < layers.length; j++) {
		      		app.activeDocument.layer = activeDocument.artLayers.getByName(layers[j]);
	                if(app.activeDocument.layer.visible == true){
	                    app.activeDocument.layer.textItem.contents= val[j];
				}
	      	}
	      	var jpgFile = new File(pathJpg+"\\\\"+val[6]+".jpg");

			jpgSaveOptions = new JPEGSaveOptions();
			// jpgSaveOptions.formatOptions = FormatOptions.OPTIMIZEDBASELINE;
			// jpgSaveOptions.embedColorProfile = true;
			// jpgSaveOptions.matte = MatteType.NONE;
			jpgSaveOptions.quality = 12;

			if (jpgFile.exists){
				var dupFile = new File(pathJpg+"\\\\" + val[6] + i.toString() +".jpg");
				activeDocument.saveAs(dupFile, jpgSaveOptions, true, Extension.LOWERCASE);
				pathJpg = fixedPath
	      	}
	      	else{
	      		activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);
				pathJpg = fixedPath
	      	}
			

			
		}
		

		}

	textLayrr(textLayers,values)
	    
	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);  // SAVECHANGES to save file
	}
	else{
	    alert("Give full path");
	}'''

	fullPath = pathForJS + "/" + nameOfJS + ".js"

	jsFile= open(fullPath, "w")


	jsFile.write(js_code)

	jsFile.close()


# ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===  ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===  ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   === 
# generateJS(layerNames,layerContents,pathForJS=path,nameOfJS=name)
