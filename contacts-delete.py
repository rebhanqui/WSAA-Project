import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contacts"
)

cursor = connection.cursor()
sql = "DELETE FROM contactslist WHERE cid = %s"
values = (11,)  # Leading zeros not allowed

cursor.execute(sql, values)

connection.commit()
print("Contact Deleted")

cursor.close()
connection.close()