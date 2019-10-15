import sqlite3 as sql

from sqlite3 import Error as err

class dbOperation:
    cur= self.conn.cursor()

    def creatDb(self,file):
    
        try:
            self.conn = sql.connect(file)
        except err as e:
            print(e)()
    def createTable(self,file,name="", cols=[]):
        cur= self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + name.replace(" ","") + " (" + ",".join(tup for tup in cols) + " );" )
    def insert(self,name="" , data={} ):
        cur.execute("INSERT INTO " + name + " (" )

file="sample.db"

tbl="clients"

colms=[("id INT PRIMARY KEY"),("name text NOT NULL"),("phone INT NOT NULL"),("address text NOT NULL")]

db=dbOperation()
db.creatDb(file)
db.createTable(file,name=tbl , cols=colms)