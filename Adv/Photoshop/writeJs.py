#  ----  Created : 20 January 2019 15:42 ( GMT+5:30 )
	# by --- Abhishek Soni ( Special thanks to Samprit Sarkar )
# !! This code writes JS sript for PS while extracting data from excel. !!



import os
try:
	import pandas as pd
except ImportError:
	modules=['pandas' ,'xlrd']
	for mod in modules:
		os.system("sudo python -m pip install " + mod)
	import pandas as pd



files = input("Path of excel files : ").replace("\\","/") 
path = input("Path to save code files : ").replace("\\","/")
name = input("Enter name of the code files (without EXT) : ").replace(" ","_")
data = pd.read_excel(files)

#~~~~~~ These layer names must be present in PSD FILE
layerNames =['student_name' , 'course_name' , 'college_name','start_day','start_super','start_month','end_day','end_super','end_month','reg_id']
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
		checkKey = key.lower().replace(" ","")
		arrItems = [] 
		if  checkKey == "startdate" or checkKey == "start" or checkKey == "date" :
			yr = []
			day = []
			sup =  []
			for startDate in excelFile[key]:
				if '.' in startDate:
					checker = startDate.split(".")
					if len(checker) == 3:
						dd , mm , yy = startDate.split(".")
						month = fixMonth(mm)
						year = fixYear(yy)
						date = fixDate(dd)
						superScript = setSuperScript(date)
						wrdDate = month + ", " + year
						yr.append(wrdDate)
						day.append(date)
						sup.append(superScript)
						
					else:
						raise ValueError("Invalid Date format detected !!! Expected '.' got something else instead : ", startDate, " in " , key)
			
				else:
					raise SyntaxError("Invalid Date format detected !!! Expected '.' got something else instead : " , startDate , " in " , key)
			layerContents.append(day)
			layerContents.append(sup)
			layerContents.append(yr)
		if checkKey == "enddate" or checkKey == "end" or checkKey == "date" :
			yer = []
			dayy = []
			supp =  []
			for endDate in excelFile[key]:
				if '.' in endDate:
					checker = endDate.split(".")
					if len(checker) == 3:
						ddd , mmm , yyy = endDate.split(".")
						monthh = fixMonth(mmm)
						yearr = fixYear(yyy)
						dates = fixDate(ddd)
						superScriptt = setSuperScript(dates)
						wrddates = monthh + ", " + yearr
						yer.append(wrddates)
						dayy.append(dates)
						supp.append(superScriptt)
						
					else:
						raise SyntaxError("Invalid Date format detected !!! Expected '.' got something else instead : ", startDate, " in " , key)
			
				else:
					raise SyntaxError("Invalid Date format detected !!! Expected '.' got something else instead : " , startDate , " in " , key)
			layerContents.append(dayy)
			layerContents.append(supp)
			layerContents.append(yer)
		if checkKey == "studentname" or checkKey == "student" or checkKey == "name" :
			stdName = []
			for student in excelFile[key]:
				stdName.append(student)
						
			layerContents.append(stdName)

		if checkKey == "coursename" or checkKey == "course" or checkKey == "courses" :
			courseArray = []
			for course in excelFile[key]:
				courseArray.append(course)
			layerContents.append(courseArray) 
		if checkKey == "collegename" or checkKey == "college" or checkKey == "colleges" :
			collegeArray = []
			for colege in excelFile[key]:
				collegeArray.append(colege)
			layerContents.append(collegeArray)

	listReg = []
	for i , j in zip(excelFile['Reg No'],excelFile['Reg ID']):
		listReg.append( i + '-0' + str(j) )

	layerContents.append(listReg)


	for i in range(len(layerContents)):
		print(layerContents[i][-1])


#  ----   INTIAL


handleExcel(data)


# || || ||    ===    Writes JS   ===    || || || 

def generateJS(layers,contents,pathForJS='' , nameOfJS = '-_-Untitled-_-'):
	js_code = '''var textLayers = ''' + str(layers) + ''';
var values =''' + str(contents) + ''';
var pathPsd=prompt("Enter the path of psd","C:\\\\>>>").replace("\\\\","/");
var pathJpg = prompt("Enter the path to save JPG","C:\\\\\\>>>").replace("\\\\","/");
var fixedPath = pathJpg;
var psdFile = new File(pathPsd);
var saveName = "";
var layerName = "";
var val = "";
if (psdFile.exists) {
    app.open(psdFile);
    function textLayrr(layers, changes) {
        var names = changes[0]
            var course = changes[1]
            var college = changes[2]

            var start_day = changes[3]
            var start_spr = changes[4]
            
            var start_mnth = changes[5]
            

            
            var end_day = changes[6]
            var end_spr = changes[7]
            var end_mnth = changes[8]

            var regID = changes[9]
        
        for (i = 0; i < names.length; i++) {
            val = [];
            val.push(names[i])
            val.push(course[i])
            val.push(college[i])

            val.push(start_day[i])
            val.push(start_spr[i])
            val.push(start_mnth[i])

            val.push(end_day[i])
            val.push(end_spr[i])
            val.push(end_mnth[i])

            val.push(regID[i])

            
            for (var j = 0; j < layers.length; j++) {
                app.activeDocument.layer = activeDocument.artLayers.getByName(
                    layers[j]
                );
                if (app.activeDocument.layer.visible == true) {
                    app.activeDocument.layer.textItem.contents = val[j];
                }
            }
            var jpgFile = new File(pathJpg + "/" + val[0] + ".jpg");

            jpgSaveOptions = new JPEGSaveOptions();
            // jpgSaveOptions.formatOptions = FormatOptions.OPTIMIZEDBASELINE;
            // jpgSaveOptions.embedColorProfile = true;
            // jpgSaveOptions.matte = MatteType.NONE;
            jpgSaveOptions.quality = 12;

            if (jpgFile.exists) {
                var dupFile = new File(
                    pathJpg + "/" + val[0] + i.toString() + ".jpg"
                );
                activeDocument.saveAs(
                    dupFile,
                    jpgSaveOptions,
                    true,
                    Extension.LOWERCASE
                );
                pathJpg = fixedPath;
            } else {
                activeDocument.saveAs(
                    jpgFile,
                    jpgSaveOptions,
                    true,
                    Extension.LOWERCASE
                );
                pathJpg = fixedPath;
            }
        }
    }

    textLayrr(textLayers, values);

    app.activeDocument.close(SaveOptions.DONOTSAVECHANGES); // SAVECHANGES to save file
} else {
    alert("Give full path");
}'''

	fullPath = pathForJS + "/" + nameOfJS + ".js"

	jsFile= open(fullPath, "w")


	jsFile.write(js_code)

	jsFile.close()
	

# ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===  ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===  ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   ===   ++++++++   === 
generateJS(layerNames,layerContents,pathForJS=path,nameOfJS=name)