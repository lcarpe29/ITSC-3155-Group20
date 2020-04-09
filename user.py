import mysql.connector


class User:

    def __init__(self, firstname, lastname, password, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.balance = balance

    # getter methods

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_password(self):
        return self.password

    def get_balance(self):
        return self.balance


    # setter methods

    def set_firstname(self, x):
        self.firstname = x

    def set_lastname(self, x):
        self.lastname = x

    def set_password(self, x):
        self.password = x

    def set_balance(self, x):
        self.balance = x