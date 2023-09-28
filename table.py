import mysql.connector as myConn

mydb = myConn.connect(
    host="localhost",
    user="root",
    password="Asphalt@12",
    database= "LearnCoding"
)

db_cursor = mydb.cursor()
db_cursor.execute("create table Emp2(Roll int,Ename varchar(20))")
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)