import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82",
    database="mydatabase102")

mycursor=mydb.cursor()
mycursor.execute("SELECT*from customers")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
