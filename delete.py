import mysql.connector as myConn

mydb = myConn.connect(
    host="localhost",
    user="root",
    password="Asphalt@12"
)
db_cursor = mydb.cursor()
db_delete = "delete from learncoding.Emp where Ename=%s"
db_value = ("sahrma",)
db_cursor.execute(db_delete,db_value)

mydb.commit()

print(db_cursor.rowcount,"! Record Deleted !")