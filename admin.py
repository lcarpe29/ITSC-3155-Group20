class Admin:

    def __init__(self, firstname, lastname, password, accountid):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.accountid = accountid

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_password(self):
        return self.password

    def get_accountid(self):
        return self.accountid

    def user_withdraw(self, user, amount):
        user.set_balance(float(user.get_balance()) - amount)

    def user_deposit(self, user, amount):
        user.set_balance(float(user.get_balance()) + amount)
