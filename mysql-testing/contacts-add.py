import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contacts"
)

cursor = connection.cursor()
sql = "INSERT INTO contactslist (cid, firstName, lastName, department, telNum) VALUES (%s, %s, %s, %s, %s)"
values = (11, "Rebecca", "Quinn", "Customer Service", 1852345678) #leading zeros not allowed - check out

cursor.execute(sql, values)

connection.commit()
print("Contact Added")

cursor.close()
connection.close()