import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contacts"
)

cursor = connection.cursor()
sql = "UPDATE contactslist SET firstName=%s, lastName=%s, department=%s, telNum=%s WHERE cid=%s;"
values = ("Andrew", "Valukonis", "IT", 1852998278, 10)  # Leading zeros not allowed

cursor.execute(sql, values)

connection.commit()
print("Contact Updated")

cursor.close()
connection.close()