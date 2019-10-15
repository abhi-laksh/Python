import os
import pandas as pd

try:
    import pymysql
    import mysql.connector as sql
    import ntpath
except ImportError:
    print("-----   Trying to Install required module:   -----")
    ModList=['pymysql','mysql-connector','ntpath']
    for module in ModList:
        os.system('python -m pip install '+ module)
    import pymysql
    import pymysql.cursors
    import mysql.connector as sql


path=input("Enter the path of the csv or excel : ").replace("\\","/")
print(path)

fileName=ntpath.basename(path)
print(fileName)

if path[-3:]=="csv":
    data=pd.read_csv(path)
    
else:
    data=pd.read_excel(path)
    


try:
    # TRY to connect database
    myDb= sql.connect(host="localhost" , user="root" , passwd="",database="maindb")
    crsr = myDb.cursor()


except sql.errors.DatabaseError:
    # If doesnt exist then create it
    myDb= sql.connect(host="localhost" , user="root" , passwd="")
    crsr= myDb.cursor()
    crsr.execute("CREATE DATABASE IF NOT EXISTS maindb")
    myDb= sql.connect(host="localhost" , user="root" , passwd="", database="maindb")
    crsr = myDb.cursor()



colmList=[]


#Check values are int or string
keys=[]
values=[]

#================    extrating values     ==================
for colInExcel in data:
    valArr=[]
    for ind in range(len(data[colInExcel])):
        val=data[colInExcel][ind]
        valArr.append(val)
    values.append(valArr)
#================    extrating keys     ==================
for key in data:
    keys.append(key)

diction={}

for k,v in zip(keys,values):
    diction[k]=v

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
            colType=" INT (100) NOT NULL"
            colmnName=colmnName.replace(" ","_")
            tbl=colmnName + colType
            colmList.append(tbl)
    else:
        colType=" VARCHAR (100) NOT NULL"
        colmnName=colmnName.replace(" ","_")
        tbl= str(colmnName) + colType
        colmList.append(tbl)




sqlTbl="CREATE TABLE IF NOT EXISTS " + fileName.split(".")[0] # CREATE TABLE <name of the file>
sqlTbl+= " ( " + ",".join(tblName for tblName in colmList) +" ) "
# crsr.execute(sqlTbl)

print(sqlTbl)
# ---- ---- Transpose a matrix
sqlInsert= " INSERT INTO " + fileName.split(".")[0]
sqlInsert += " ( " + ",".join(str(tbls) for tbls in keys if 'id' not in tbls ) + " ) "
# sqlInsert += " VALUES ( " + ",".join(str(tuple(vals)) for vals in values) + " );"
dubList=list(map(tuple, zip(*values[1:])))
sqlInsert += " VALUES " +  ",".join(str(vals)  for vals in dubList) + ";"
print(sqlInsert) 
# crsr.execute(sqlInsert)
# myDb.commit()
# myDb.close()
# crsr.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")