import sqlite3 as mySql
import pandas as pd
import tkinter as tk
from sqlite3 import Error as err


class database:

	def createDb(self,file):
		try:

			self.datab= mySql.connect(file)
			print(mySql.version)
		except err as self.e:
			print(self.e)
		finally:
			self.datab.close()
	def createTable(self,file):

