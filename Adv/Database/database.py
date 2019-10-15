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




conn= mySql.connect("client.db")

crsr= conn.cursor()

def createTable():
	crsr.execute("""CREATE TABLE IF NOT EXISTS clients(
	id integer PRIMARY KEY, 
	name text NOT NULL, 
	address text NOT NULL, 
	project_id integer NOT NULL);""")

	crsr.execute(""" INSERT INTO clients
		(name , address , project_id) VALUES
		('Abhishek' , 'Lake Town' , 1 );
		 """)

	conn.commit()

	conn.close()

# createTable()
def display(datab):
	crsr.execute(""" SELECT * FROM clients """)
	row = crsr.fetchall()

	for r in row:
		print(r)

display(conn)