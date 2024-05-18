#pip install mysql-connector
#pip install flask
import flask
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE contacts;")

cursor.close()
connection.close()