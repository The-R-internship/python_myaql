import mysql.connector as myConn

print("Driver is installed")

mydb = myConn.connect(host = "localhost",
                      user = "root",
                      password = "Asphalt@12"
                      )

print(mydb, "connection established")