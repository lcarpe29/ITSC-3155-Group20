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
    "userBalance FLOAT DEFAULT 0,"
    "admin INT DEFAULT NULL"
    ")"
)
insertCommand = "INSERT INTO Users (userFirstName, userLastName, userEmail, userPassword, admin) " \
                "VALUES( 'root', 'root', 'root@uncc.edu', 'root123', 1);"

mycursor.execute(insertCommand)

query = """UPDATE Users
        SET userBalance = 200
        WHERE userID = 1;"""
mycursor.execute(query)
mydb.commit()
