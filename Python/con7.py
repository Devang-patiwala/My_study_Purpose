import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devang@82",
    database="mydatabase102")

mycursor=mydb.cursor()

sql="INSERT INTO customers (name,address)VALUES(%s,%s)"
val=[
    ('anil', 'satellite'),
    ('seema', 'amabawadi'),
    ('heena', 'gota'),
    ('akash', 'bopal')
    ]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted")
    
