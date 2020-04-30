import mysql.connector
from user import User


class Transaction:

    def __init__(self, date, type, amount, accountid):
        self.date = date
        self.type = type
        self.amount = amount
        self.accountid = accountid
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="enterpassword",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()

    def get_date(self):
        return self.date

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount

    def set_date(self, x):
        self.date = x
        command = "UPDATE Transactions " \
                  "SET transactDate = '" + str(x) + "' " \
                                                     "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()

    def set_type(self, x):
        self.date = x
        command = "UPDATE Transactions " \
                  "SET transactType = '" + str(x) + "' " \
                                                    "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()

    def set_amount(self, x):
        self.date = x
        command = "UPDATE Transactions " \
                  "SET transactAmount = '" + str(x) + "' " \
                                                    "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()