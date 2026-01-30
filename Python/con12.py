import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82",
    database="mydatabase102")

mycursor=mydb.cursor()
sql="UPDATE customers SET address='shivranjani'WHERE address='satellite'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")
