import mysql.connector
from transaction import Transaction

class User:
    def __init__(self, firstname, lastname, password, balance, accountid, generalTransactionLog):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.balance = float(balance)
        self.accountid = int(accountid)
        self.userlog = self.create_log(generalTransactionLog)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7NJn-N\\ar_<3PS~T",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()

    # getter methods
    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_password(self):
        return self.password

    def get_balance(self):
        return self.balance

    def get_accountid(self):
        return self.accountid

    def get_userlog(self):
        return self.userlog

    def set_balance(self, x):
        self.balance = float(x)
        command = "UPDATE Users " \
                  "SET userBalance = " + str(x) + " " \
                                                  "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()
        self.db.reconnect()

    def create_log(self, generalLog):
        userLog = []
        for x in generalLog:
            if x.get_id() == self.accountid:
                userLog.append(x)
        return userLog

