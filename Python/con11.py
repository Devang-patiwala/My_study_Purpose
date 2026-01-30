import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82",
    database="mydatabase102")

mycursor=mydb.cursor()
sql="DELETE from customers WHERE address='bopal'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
