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
    

for i in data[]:
    print(i)