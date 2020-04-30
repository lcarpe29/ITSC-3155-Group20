import mysql.connector
from user import User
from transaction import Transaction

class Account:

    def __init__(self, accountid, accountName, accountNum, balance, transactArr):
        self.accountid = accountid
        self.accountName = accountName
        self.balance = balance
        self.accountNum - accountNum
        self.transactArr = transactArr
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="enterpassword",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()

        def withdraw_funds(date, type, amount, accountid, ):
            self.balance = self.balance - amount
            transaction = Transaction(date, type, amount, accountid)
            self.transactArr.append(transaction)

        def deposit_funds(date, type, amount, accountid, ):
            self.balance = self.balance + amount
            transaction = Transaction(date, type, amount, accountid)
            self.transactArr.append(transaction)

        # getter methods
        def get_accountid(self):
            return self.accountid

        def get_accountName(self):
            return self.accountName

        def get_balance(self):
            return self.balance

        def set_accountName(self, x):
            self.accountName = x
            #TODO figure out these commands
            #command = "UPDATE Users " \
                      #"SET userPassword = '" + str(x) + "' " \
                                                        #"WHERE userID = " + str(self.accountid) + ";"
            #self.cursor.execute(command)
            self.db.commit()

        def set_balance(self, x):
            self.balance = x
