import mysql.connector as myConn

mydb = myConn.connect(
    host="localhost",
    user="root",
    password="Asphalt@12"
)

db_cursor = mydb.cursor()

# Corrected SQL query to create the database
db_cursor.execute("CREATE DATABASE LearnCoding")

print("Database created")
