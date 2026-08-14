import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    database="student_management_db"
)

cursor = conn.cursor()