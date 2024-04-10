import mysql.connector

# Access Database using credentials
databaseConnection = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'eagle2021',
)


cursorObject = databaseConnection.cursor()

#MYSQL SQL function delete database if exists
cursorObject.execute("DROP database IF EXISTS CRUDDB")

#MYSQL SQL function create database
cursorObject.execute("CREATE DATABASE CRUDDB")

print("ALL DONE!")

databaseConnection.close()