import mysql.connector




class User:

    def __init__(self, firstname, lastname, password, balance, accountid, accountArr):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.balance = balance
        self.accountid = accountid
        self.accountArr = accountArr
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="enterpassword",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()


    def perform_transaction(self, date, type, amount, account1, account2):

        if (type == "withdraw"):
            account1.withdraw_funds(date, type, amount, self.accountid, )
        if(type == "deposit"):
            account1.deposit_funds(date, type, amount, self.accountid, )
        if(type == "transfer"):
            account1.withdraw_funds(date, type, amount, self.accountid, )
            account2.deposit_funds(date, type, amount, self.accountid, )


    #getter methods
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

    # setter methods

    def set_firstname(self, x):
        self.firstname = x
        command = "UPDATE Users " \
                  "SET userFirstName = '" + str(x) + "' " \
                                                     "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()

    def set_lastname(self, x):
        self.lastname = x
        command = "UPDATE Users " \
                  "SET userLastName = '" + str(x) + "' " \
                                                    "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()

    def set_password(self, x):
        self.password = x
        command = "UPDATE Users " \
                  "SET userPassword = '" + str(x) + "' " \
                                                    "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()

    def set_balance(self, x):
        self.balance = x
        command = "UPDATE Users " \
                  "SET userBalance = " + str(x) + " " \
                                                  "WHERE userID = " + str(self.accountid) + ";"
        self.cursor.execute(command)
        self.db.commit()
