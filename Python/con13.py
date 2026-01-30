import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82",
    database="mydatabase102")

mycursor=mydb.cursor()

sql="drop table customers"
mycursor.execute(sql)
