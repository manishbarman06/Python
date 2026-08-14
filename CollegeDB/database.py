import mysql.connector

con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456789",
    database = "college"
)

cursor = con.cursor()