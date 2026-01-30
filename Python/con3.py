import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82"
    )
mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASE")
for x in mycursor:
    print(x)
