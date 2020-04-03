import mysql.connector


class User:

    def __init__(self, firstname, lastname, password):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.balance = 0
