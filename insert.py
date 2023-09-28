import mysql.connector as myConn

mydb = myConn.connect(
    host="localhost",
    user="root",
    password="Asphalt@12",
    database= "LearnCoding"
)

db_cursor = mydb.cursor()
db_insert = "insert into Emp(Roll,Ename) values(%s,%s)"
db_list = [(21,"Akash"),(31, "Sahrma"),(41,"yash") ]
db_cursor.executemany(db_insert,db_list)

mydb.commit()

print(db_cursor.rowcount, "Record inserted") 