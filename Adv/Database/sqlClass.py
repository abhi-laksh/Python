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


    