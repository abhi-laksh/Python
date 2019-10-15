import sqlite3 as sql

from sqlite3 import Error as err

class dbOperation:

    def creatDb(self,file):
    
        try:
            self.conn = sql.connect(file)
        except err as e:
            print(e)

    def createTable(self,name="", cols=[]):
        cur= self.conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS " + name.replace(" ","") + " (" + ",".join(tup for tup in cols) + " );" 
        cur.execute(query)
    
    def insert(self,name="" , data={} ):
        cur= self.conn.cursor()
        # query = "INSERT INTO " + name.replace(" ","") + " ( " + ",".join(key.lower() for key in data.keys()) + " ) " + "VALUES" + " ( " + " 'Abhishek' , 'Lake Town' , 1 " + " );"
        query = "INSERT INTO " + name.replace(" ","") + " ( " + ",".join(key.lower() for key in data.keys()) + " ) " + "VALUES" + " ( " + ",".join(str(val) for val in data.values()) + " );"
        cur.execute(query)


files="sample.db"

tbl="clients"

colms=[("id integer PRIMARY KEY"),("name text NOT NULL"),("phone integer NOT NULL"),("address text NOT NULL")]

data={'name' : "'Abhishek'" , 'phone' : 9845754745 , 'address' : "'LakeTown'" }

db=dbOperation()
db.creatDb(files)

db.createTable(name=tbl , cols=colms)   
db.insert(name=tbl , data=data)