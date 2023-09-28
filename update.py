import mysql.connector as myConn

mydb = myConn.connect(
    host="localhost",
    user="root",
    password="Asphalt@12"
)
db_cursor = mydb.cursor()

db_updatedata = "update Learncoding.Emp set roll=%s where Ename=%s"
db_value = (11,"Akash")
db_cursor.execute(db_updatedata,db_value)

mydb.commit()

print ("value updated")