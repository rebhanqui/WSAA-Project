import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contacts"
)

cursor = connection.cursor()
sql = "CREATE TABLE contactslist(cid INT PRIMARY KEY, firstName VARCHAR(50), lastName VARCHAR(50), department VARCHAR(50), telNum VARCHAR(50));"
cursor.execute(sql)

cursor.close()
connection.close()