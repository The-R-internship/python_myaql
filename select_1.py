import mysql.connector as myConn

mydb = myConn.connect(
    host="localhost",
    user="root",
    password="Asphalt@12"
)

db_cursor = mydb.cursor()

db_cursor.execute("select * from LearnCoding.Emp")
db_select = db_cursor.fetchall()

print(db_select)

