from sqlite3 import Cursor
import mysql.connector
from numpy import insert

mydb = mysql.connector.connect(host='localhost',user='sangeeta',password='sangeeta@468',database='example',autocommit=True)

Cursor = mydb.cursor("insert into signup(number ,email , password ,conformpassword)")