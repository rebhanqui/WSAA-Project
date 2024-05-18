import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contacts"
)

cursor = connection.cursor()
sql = "SELECT * FROM contactslist WHERE cid = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)
    
cursor.close()
connection.close()