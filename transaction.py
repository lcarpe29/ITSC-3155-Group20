import mysql.connector
from user import User


class Transaction:

    def __init__(self, date, transactionType, amount, accountid):
        self.date = date
        self.type = transactionType
        self.amount = amount
        self.accountid = accountid
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7NJn-N\\ar_<3PS~T",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()

    def get_id(self):
        return self.accountid

    def get_date(self):
        return self.date

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount

    def record_transaction(self):
        insertCommand = "INSERT INTO Transactions (userID, transactDate, transactType, transactAmount) " \
                        "VALUES( " + str(self.accountid) + ", '" + self.date + "', '" + self.type + "', " \
                        + str(self.amount) + ")"
        self.cursor.execute(insertCommand)
        self.db.commit()

    def to_string(self):
        display = "Date: " + self.date + "\tType: " + self.type + "\tAmount: " + str(self.amount)
        return display
