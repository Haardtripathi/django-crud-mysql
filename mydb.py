import mysql.connector

database=mysql.connector.connect(
    user='root',
    host='localhost',
    passwd="Kakarot@1231"
)

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE anyname")