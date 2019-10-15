
try:
    import pymysql
    import mysql.connector as sql
    import ntpath
    import pandas as pd
    import os
except ImportError:
    print("-----   Trying to Install required module:   -----")
    ModList=['pymysql','mysql-connector','ntpath','pandas']
    for module in ModList:
        os.system('python -m pip install '+ module)
    import pymysql
    import pymysql.cursors
    import mysql.connector as sql
    import pandas as pd


host="localhost"
username="id6227651__abhi_laksh_"
pwd="_abhi_laksh_"
db="id6227651_abhidatab"

# -----   ----   Taking path of the file   -----   ----
path=input("Enter the path of the csv or excel : ").replace("\\","/")
# -----   ----   Extracting name of the file   -----   ----
fileName=ntpath.basename(path)

# -----   ----   Checking Extenson of the file   -----   ----
if path[-3:]=="csv":
    data=pd.read_csv(path)
else:
    data=pd.read_excel(path)


    
keys=[]
values=[]
diction={}

def dataToDict(xlFile):
    #================    extrating values     ==================
    for colInExcel in xlFile:
        valArr=[]
        for ind in range(len(xlFile[colInExcel])):
            val=xlFile[colInExcel][ind]
            valArr.append(val)
        values.append(valArr)
    #================    extrating keys     ==================
    for key in xlFile:
        keys.append(key)
dataToDict(data)

# Turning data to dictionary 
for k,v in zip(keys,values):
    diction[k]=v



try:
    # TRY to connect database
    myDb= sql.connect(host=host , user=username , passwd=pwd,database=db)
    crsr= myDb.cursor()
except sql.errors.DatabaseError:
    # If doesnt exist then create it
    myDb= sql.connect(host=host , user=username , passwd=pwd )
    crsr= myDb.cursor()
    sqlCmnd="CREATE DATABASE IF NOT EXISTS "+ db
    crsr.execute(sqlCmnd)

colmList=[]

# Check type of values and then assigning COLUMN PROPERTIES according to it
for colmnName in keys:
    checkInt="".join(str(val) for val in diction[colmnName])
    print(checkInt)
    print(diction[colmnName])
    if checkInt.isdigit() == True:
        if 'id' in colmnName:
            colType= " INT AUTO_INCREMENT PRIMARY KEY "
            colmnName=colmnName.replace(" ","_")
            tbl=colmnName+colType
            colmList.append(tbl)
        else:
            colType=" INT (100) "
            colmnName=colmnName.replace(" ","_")
            tbl=colmnName + colType
            colmList.append(tbl)
    else:
        colType=" VARCHAR (100) "
        colmnName=colmnName.replace(" ","_")
        tbl= str(colmnName) + colType
        colmList.append(tbl)

# --- === --- === --- === --- === --- === --- === --- === --- === --- === --- === --- === --- === 


sqlCmd="CREATE TABLE IF NOT EXISTS " + fileName.split(".")[0] # CREATE TABLE <name of the file>
sqlCmd+= " ( " + ",".join(tblName for tblName in colmList) + " ) "
print(sqlCmd)
crsr.execute(sqlCmd)



# crsr.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")