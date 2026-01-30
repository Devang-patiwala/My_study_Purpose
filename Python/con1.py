import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82"
    )
print(mydb)
