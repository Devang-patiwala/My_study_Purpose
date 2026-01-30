import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82",
    database="mydatabase102")

mycursor=mydb.cursor()
sql="SELECT*from customers WHERE address='gota'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
