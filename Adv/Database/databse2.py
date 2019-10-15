import sqlite3 as mySql
import pandas as pd
import tkinter as tk
from sqlite3 import Error as err


# =================      For creating database            ===================

# path=input("Enter the path of database file : ").replace("\\","/")
# name=input("Enter the name of database file : ")
# file= path + "/" + name
# def createDb(file):
# 	try:

# 		datab= mySql.connect(file)
# 		print(mySql.version)
# 	except err as e:
# 		print(e)
# 	finally:
# 		datab.close()

# if __name__=="__main__":
# 	createDb(file)



# tbl_name = input("Enter name for table : ").replace(" ","")
tbl_name = 'projects'


projName = 'projName'
desc = 'description'
client_id = 'client_id'

lst=(projName,desc,client_id)

conn= mySql.connect("projects.db")

crsr= conn.cursor()

def crateTable():
	crsr.execute("""CREATE TABLE IF NOT EXISTS projects (id integer PRIMARY KEY,  projName text NOT NULL, description text NOT NULL, client_id integer NOT NULL);""")

	crsr.execute("""INSERT INTO projects (projName, description ,client_id) VALUES ('Android app','Google' , 1);""")

	

	conn.commit()

	# conn.close()

# crateTable()

def display(datab):
	crsr.execute(""" SELECT * FROM projects """)
	row = crsr.fetchall()

	for r in row:
		print(r)

display(conn)