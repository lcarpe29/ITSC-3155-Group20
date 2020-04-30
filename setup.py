import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="7NJn-N\\ar_<3PS~T"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS bankingsimulator")
mycursor.execute("CREATE DATABASE IF NOT EXISTS bankingsimulator")
mycursor.execute("USE bankingsimulator")
mycursor.execute("DROP TABLE IF EXISTS Users")
mycursor.execute(
    "CREATE TABLE Users ("
    "userID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "userFirstName VARCHAR(20) NOT NULL,"
    "userLastName VARCHAR(20) NOT NULL,"
    "userEmail VARCHAR(40) NOT NULL,"
    "userPassword VARCHAR(20) NOT NULL,"
    "userBalance INT DEFAULT 0,"
    "admin INT DEFAULT NULL"
    ")"
)
mycursor.execute("DROP TABLE IF EXISTS Transactions")
mycursor.execute(
    "CREATE TABLE Transactions ("
    "userID INT NOT NULL,"
    "transactDate VARCHAR(10),"
    "transactType VARCHAR(10),"
    "transactAmount FLOAT"
    ")"
)
insertCommand = "INSERT INTO Users (userFirstName, userLastName, userEmail, userPassword, admin) " \
                "VALUES( 'root', 'root', 'root@uncc.edu', 'root123', 1);"
mycursor.execute(insertCommand)
mydb.commit()