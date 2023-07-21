import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eudalius6',
    port = '33061'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE prometheus")
print("All done!")