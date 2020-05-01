import tkinter as tk
import tkinter.font as font
import mysql.connector

from datetime import date
from user import User
from admin import Admin
from transaction import Transaction


class Simulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('Banking Simulation')
        master.geometry('500x500')
        master.configure(bg="black")
        self.pack()
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7NJn-N\\ar_<3PS~T",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()
        self.today = date.today().strftime("%m/%d/%y")
        self.transactionLog = []
        self.initializeTransactionLog()
        self.signinWindow()

    # Initializing
    def initializeTransactionLog(self):
        self.cursor.execute("SELECT *"
                            "FROM Transactions "
                            )

        userInfo = self.cursor.fetchall()

        for row in userInfo:
            accountID = int(row[0])
            date = row[1]
            type = row[2]
            amount = float(row[3])
            tempTransaction = Transaction(date, type, amount, accountID)
            self.transactionLog.append(tempTransaction)

    # All User Windows
    def signinWindow(self):
        self.signinFrame = tk.Frame(self, bg='black')
        self.signinFrame.pack()

        myfont = font.Font(size=30)
        tk.Label(self.signinFrame, text="49er Credit Union", fg="green", bg="black", font=myfont).pack()

        tk.Label(self.signinFrame, text="Enter Email: ", bg="black", fg='#ffcc00').pack()
        self.entrySigninEmail = tk.Entry(self.signinFrame)
        self.entrySigninEmail.pack()
        tk.Label(self.signinFrame, text="Enter Password: ", bg="black", fg='#ffcc00').pack()
        self.entrySigninPassword = tk.Entry(self.signinFrame, show='*')
        self.entrySigninPassword.pack()

        btnSignin = tk.Button(self.signinFrame, text="Sign In", highlightbackground='#ffcc00', fg='green',
                              command=self.signinProcess)
        btnSignin.pack(side="left")
        btnQuit = tk.Button(self.signinFrame, text="Quit", highlightbackground='#ffcc00', fg="red",
                            command=self.master.destroy)
        btnQuit.pack(side="right")

    # Account holder Windows
    def homeWindow(self):
        self.homeFrame = tk.Frame(self)
        self.homeFrame.pack()

        myfont = font.Font(size=30)
        tk.Label(self.homeFrame, text="49er Credit Union", fg="green", bg="black", font=myfont).pack()

        myfont = font.Font(size=20)
        tk.Label(self.homeFrame, text="Welcome, " + self.userInstance.get_firstname() + " " +
                                      self.userInstance.get_lastname(), fg="green", bg="black", font=myfont).pack()
        tk.Label(self.homeFrame, text="Balance: " + str(self.userInstance.get_balance()), bg="black",
                 fg='#ffcc00').pack()
        tk.Label(self.homeFrame, text="Account ID: " + str(self.userInstance.get_accountid()), bg="black",
                 fg='#ffcc00').pack()

        tk.Button(self.homeFrame, text="Transaction History", highlightbackground='#ffcc00', fg='green',
                  command=self.transactionHistoryWindow).pack(side="left")
        tk.Button(self.homeFrame, text="Transfer Funds", highlightbackground='#ffcc00', fg='green',
                  command=self.transferFundsWindow).pack(side="right")
        tk.Button(self.homeFrame, text="Logout", highlightbackground='#ffcc00', fg='green',
                  command=self.confirmLogoutWindow).pack(side="bottom")

    def transactionHistoryWindow(self):
        self.homeFrame.destroy()
        self.transactionHistoryFrame = tk.Frame(self)
        self.transactionHistoryFrame.pack()

        if len(self.userInstance.get_userlog()) == 0:
            message = "No Transaction History"
        else:
            message = "Transaction History: \n"
            for transaction in self.userInstance.get_userlog():
                message = message + transaction.to_string() + "\n"
        tk.Message(self.transactionHistoryFrame, text=message, bg="black", fg='#ffcc00', width=450).pack()

        tk.Button(self.transactionHistoryFrame, text="Back", highlightbackground='#ffcc00', fg='green',
                  command=self.fromHistoryToHome).pack(side="left")

    def transferFundsWindow(self):
        self.homeFrame.destroy()
        self.transferFundsFrame = tk.Frame(self)
        self.transferFundsFrame.pack()

        tk.Label(self.transferFundsFrame, text="Enter Account ID: ", bg="black", fg='#ffcc00').pack()
        self.entryTransferFundsAccountID = tk.Entry(self.transferFundsFrame)
        self.entryTransferFundsAccountID.pack()
        tk.Label(self.transferFundsFrame, text="Transaction Amount: ", bg="black", fg='#ffcc00').pack()
        self.entryTransferFundsAmount = tk.Entry(self.transferFundsFrame)
        self.entryTransferFundsAmount.pack()

        tk.Button(self.transferFundsFrame, text="Back", highlightbackground='#ffcc00',
                  fg='green', command=self.fromTransferToHome).pack(side="left")
        tk.Button(self.transferFundsFrame, text="Okay", highlightbackground='#ffcc00',
                  fg='green', command=self.transfer).pack(side="right")

    def fromHomeToSignin(self):
        self.homeFrame.destroy()
        self.userInstance = None
        self.signinWindow()

    def fromHistoryToHome(self):
        self.transactionHistoryFrame.destroy()
        self.homeWindow()

    def fromTransferToHome(self):
        self.transferFundsFrame.destroy()
        self.homeWindow()

    def fromSigninToHome(self):
        self.signinFrame.destroy()
        self.homeWindow()

    # Admin Windows
    def adminHomeWindow(self):
        self.signinFrame.destroy()
        self.adminHomeFrame = tk.Frame(self)
        self.adminHomeFrame.pack()

        myfont = font.Font(size=30)
        tk.Label(self.adminHomeFrame, text="49er Credit Union", fg="green", bg="black", font=myfont).pack()

        myfont = font.Font(size=20)
        tk.Label(self.adminHomeFrame,
                 text="Welcome, " + self.adminInstance.get_firstname() + " " + self.adminInstance.get_lastname(),
                 fg="green", bg="black", font=myfont).pack()

        tk.Button(self.adminHomeFrame, text="New Account", highlightbackground='#ffcc00', fg='green',
                  command=self.signupWindow).pack()
        tk.Button(self.adminHomeFrame, text="User Transaction", highlightbackground='#ffcc00', fg='green',
                  command=self.transactionWindow).pack()
        tk.Button(self.adminHomeFrame, text="Logout", highlightbackground='#ffcc00', fg='green',
                  command=self.confirmLogoutWindow).pack()

    def signupWindow(self):
        self.adminHomeFrame.destroy()

        self.signupFrame = tk.Frame(self)
        self.signupFrame.pack()

        tk.Label(self.signupFrame, text="Enter First Name: ", bg="black", fg='#ffcc00').pack()
        self.entrySignupFirstName = tk.Entry(self.signupFrame)
        self.entrySignupFirstName.pack()
        tk.Label(self.signupFrame, text="Enter Last Name: ", bg="black", fg='#ffcc00').pack()
        self.entrySignupLastName = tk.Entry(self.signupFrame)
        self.entrySignupLastName.pack()
        tk.Label(self.signupFrame, text="Enter Email: ", bg="black", fg='#ffcc00').pack()
        self.entrySignupEmail = tk.Entry(self.signupFrame)
        self.entrySignupEmail.pack()
        tk.Label(self.signupFrame, text="Enter Password: ", bg="black", fg='#ffcc00').pack()
        self.entrySignupPassword = tk.Entry(self.signupFrame, show='*')
        self.entrySignupPassword.pack()
        tk.Label(self.signupFrame, text="Confirm Password: ", bg="black", fg='#ffcc00').pack()
        self.entrySignupConfirmPassword = tk.Entry(self.signupFrame, show='*')
        self.entrySignupConfirmPassword.pack()
        self.adminCheck = tk.IntVar()
        self.cbSignupAdminAccount = tk.Checkbutton(self.signupFrame, text="Admin Account",
                                                   variable=self.adminCheck, onvalue=1)
        self.cbSignupAdminAccount.pack()

        tk.Button(self.signupFrame, text="Create Account", highlightbackground='#ffcc00', fg='green',
                  command=self.createAccount).pack(side="right")
        tk.Button(self.signupFrame, text="Back", highlightbackground='#ffcc00', fg='green',
                  command=self.fromSignupToAdmin).pack(side="left")

    def transactionWindow(self):
        self.adminHomeFrame.destroy()

        self.transactionFrame = tk.Frame(self)
        self.transactionFrame.pack()

        self.wdVar = tk.IntVar()
        self.rbWithdraw = tk.Radiobutton(self.transactionFrame, text="Withdraw",
                                         variable=self.wdVar, value=1)
        self.rbWithdraw.pack()
        self.rbDeposit = tk.Radiobutton(self.transactionFrame, text="Deposit",
                                        variable=self.wdVar, value=2)
        self.rbDeposit.pack()
        tk.Label(self.transactionFrame, text="Enter Account ID", bg="black", fg='#ffcc00').pack()
        self.entryTransactionAccountID = tk.Entry(self.transactionFrame)
        self.entryTransactionAccountID.pack()
        tk.Label(self.transactionFrame, text="Transaction Amount: ", bg="black", fg='#ffcc00').pack()
        self.entryTransactionAmount = tk.Entry(self.transactionFrame)
        self.entryTransactionAmount.pack()

        tk.Button(self.transactionFrame, text="Back", highlightbackground='#ffcc00',
                  fg='green', command=self.fromTransactionToAdmin).pack(side="left")
        tk.Button(self.transactionFrame, text="Okay", highlightbackground='#ffcc00',
                  fg='green', command=self.withdrawDeposit).pack(side="right")

    def fromSignupToAdmin(self):
        self.signupFrame.destroy()
        self.adminHomeWindow()

    def fromAdminToSignin(self):
        self.adminHomeFrame.destroy()
        self.adminInstance = None
        self.signinWindow()

    def fromTransactionToAdmin(self):
        self.transactionFrame.destroy()
        self.adminHomeWindow()

    # Processes
    def withdrawDeposit(self):
        if (len(self.entryTransactionAmount.get()) != 0) and (
                len(self.entryTransactionAccountID.get()) != 0) and self.wdVar.get() != 0:
            accountID = int(self.entryTransactionAccountID.get())
            amount = float(self.entryTransactionAmount.get())
            self.cursor.execute("SELECT *"
                                "FROM Users "
                                "WHERE userID = " + str(accountID) + ";"
                                )

            userInfo = self.cursor.fetchall()

            if (len(userInfo) == 0):
                # todo add popup
                self.showErrorWindow("AccountID doesn't exist")
                print("AccountID doesn't exist")
            else:
                for row in userInfo:
                    firstName = row[1]
                    lastName = row[2]
                    password = row[4]
                    balance = float(row[5])

                userForTransaction = User(firstName, lastName, password, balance, accountID, self.transactionLog)

                if self.wdVar.get() == 2:
                    self.adminInstance.user_deposit(userForTransaction, amount)
                    self.db.reconnect()
                    deposit = Transaction(self.today, "Deposit", amount, userForTransaction.get_accountid())
                    self.transactionLog.append(deposit)
                    self.transactionLog[len(self.transactionLog) - 1].record_transaction()
                else:
                    self.adminInstance.user_withdraw(userForTransaction, amount)
                    self.db.reconnect()
                    withdraw = Transaction(self.today, "Withdraw", amount, userForTransaction.get_accountid())
                    self.transactionLog.append(withdraw)
                    self.transactionLog[len(self.transactionLog) - 1].record_transaction()

                self.fromTransactionToAdmin()

        elif self.wdVar.get() == 0:
            # todo add pop up
            self.showErrorWindow("Select either withdraw or deposit")
            print("Select either withdraw or deposit")
        elif len(self.entryTransactionAccountID.get()) == 0:
            # todo add pop up
            self.showErrorWindow("Enter Account ID")
            print("Enter Account ID")
        elif len(self.entryTransactionAmount.get()) == 0:
            # todo add pop up
            self.showErrorWindow("Enter transaction amount")
            print("Enter transaction amount")
        else:
            # todo add pop up
            self.showErrorWindow("Internal Error")
            print("Internal Error")

    def transfer(self):
        if (len(self.entryTransferFundsAmount.get()) != 0) and (len(self.entryTransferFundsAccountID.get()) != 0):
            accountID = int(self.entryTransferFundsAccountID.get())
            amount = float(self.entryTransferFundsAmount.get())
            self.cursor.execute("SELECT *"
                                "FROM Users "
                                "WHERE userID = " + str(accountID) + ";"
                                )

            userInfo = self.cursor.fetchall()

            if (len(userInfo) == 0):
                # todo add popup
                self.showErrorWindow("AccountID doesn't exist")
                print("AccountID doesn't exist")
            else:
                for row in userInfo:
                    firstName = row[1]
                    lastName = row[2]
                    password = row[4]
                    balance = float(row[5])

                tempAdmin = Admin("temp", "temp", "temp", "temp")
                userForTransaction = User(firstName, lastName, password, balance, accountID, self.transactionLog)

                tempAdmin.user_withdraw(self.userInstance, amount)
                self.db.reconnect()
                tempAdmin.user_deposit(userForTransaction, amount)
                self.db.reconnect()

                message = "Transferred Funds to " + str(userForTransaction.get_accountid())
                transfer = Transaction(self.today, message, amount, self.userInstance.get_accountid())
                self.transactionLog.append(transfer)
                self.transactionLog[len(self.transactionLog) - 1].record_transaction()

                message = "Received from " + str(self.userInstance.get_accountid())
                transfer = Transaction(self.today, message, amount, userForTransaction.get_accountid())
                self.transactionLog.append(transfer)
                self.transactionLog[len(self.transactionLog) - 1].record_transaction()

                self.fromTransferToHome()

        elif len(self.entryTransferFundsAccountID.get()) == 0:
            # todo add pop up
            self.showErrorWindow("Enter Account ID")
            print("Enter Account ID")
        elif len(self.entryTransferFundsAmount.get()) == 0:
            # todo add pop up
            self.showErrorWindow("Enter transaction amount")
            print("Enter transaction amount")
        else:
            # todo add pop up
            self.showErrorWindow("Internal Error")
            print("Internal Error")

    def createAccount(self):
        if ((len(self.entrySignupFirstName.get()) != 0) and (len(self.entrySignupLastName.get()) != 0) and
                (len(self.entrySignupEmail.get()) != 0) and (len(self.entrySignupPassword.get()) != 0) and
                (len(self.entrySignupConfirmPassword.get()) != 0)):
            if (self.entrySignupPassword.get() == self.entrySignupConfirmPassword.get()):
                firstName = self.entrySignupFirstName.get()
                lastName = self.entrySignupLastName.get()
                email = self.entrySignupEmail.get()
                password = self.entrySignupPassword.get()
                adminPrivilege = self.adminCheck.get()

                insertCommand = "INSERT INTO Users (userFirstName, userLastName, userEmail, userPassword, admin) " \
                                "VALUES( '" + firstName + "', '" + lastName + "', '" + email + "', '" + password + \
                                "', '" + str(adminPrivilege) + "');"
                self.cursor.execute(insertCommand)
                self.db.commit()

                self.fromSignupToAdmin()
            else:
                self.showErrorWindow("Passwords Do Not Match")
        else:
            if len(self.entrySignupFirstName.get()) == 0:
                # todo add popup
                self.showErrorWindow("No First Name Entered")
                print("No First Name")
            elif len(self.entrySignupLastName.get()) == 0:
                # todo add popup
                self.showErrorWindow("No Last Name Entered")
                print("No Last Name")
            elif len(self.entrySignupEmail.get()) == 0:
                # todo add popup
                self.showErrorWindow("No Email Entered")
                print("No Email")
            elif len(self.entrySignupPassword.get()) == 0:
                # todo add popup
                self.showErrorWindow("No Password Entered")
                print("No Password")
            else:
                # todo add popup
                self.showErrorWindow("Internal Error")
                print("Error")

    def signinProcess(self):
        if (len(self.entrySigninEmail.get()) != 0) and (len(self.entrySigninPassword.get()) != 0):
            email = self.entrySigninEmail.get()
            self.cursor.execute("SELECT userFirstName, userLastName, userPassword, userBalance, admin, userID "
                                "FROM Users "
                                "WHERE userEmail = '" + email + "';"
                                )

            passwordCheck = self.cursor.fetchall()

            for row in passwordCheck:
                firstName = row[0]
                lastName = row[1]
                password = row[2]
                balance = row[3]
                adminPrivilege = row[4]
                accountID = row[5]

            if password == self.entrySigninPassword.get():
                if adminPrivilege == 1:
                    # Create admin instance and open to admin home screen
                    self.adminInstance = Admin(firstName, lastName, password, accountID)
                    self.adminHomeWindow()
                else:
                    # Create user instance and open home screen
                    self.userInstance = User(firstName, lastName, password, balance, accountID, self.transactionLog)
                    self.fromSigninToHome()
            else:
                # todo add popup
                self.showErrorWindow("Password is incorrect")
                print("Password is wrong")
        else:
            if len(self.entrySigninEmail.get()) == 0:
                # todo add popup
                self.showErrorWindow("No Email Entered")
                print("No Email")
            elif len(self.entrySigninPassword.get()) == 0:
                # todo add popup
                self.showErrorWindow("No Password Entered")
                print("No Password")
            else:
                # todo add popup
                self.showErrorWindow("Internal Error")
                print("Internal Error")

    # Extra Windows
    def showErrorWindow(self, message):
        errorMessage = tk.Tk()
        errorMessage.title("Error")

        tk.Label(errorMessage, text=message, bg="black", fg='#ffcc00').pack()
        tk.Button(errorMessage, text="Okay", highlightbackground='#ffcc00', fg='green',
                  command=errorMessage.destroy).pack()

    def confirmLogoutWindow(self):
        self.confirmLogout = tk.Tk()
        self.confirmLogout.title("Logout?")
        tk.Label(self.confirmLogout, text="You will be logged out of your account. Do you wish to continue?").pack()
        tk.Button(self.confirmLogout, text="Yes", highlightbackground='#ffcc00', fg='green',
                  command=self.toSignin).pack(side="left")
        tk.Button(self.confirmLogout, text="No", highlightbackground='#ffcc00', fg='green',
                  command=self.confirmLogout.destroy).pack(side="right")

    def toSignin(self):
        self.confirmLogout.destroy()

        if self.adminHomeFrame.winfo_exists():
            self.adminHomeFrame.destroy()
        else:
            self.homeFrame.destroy()

        self.signinWindow()


root = tk.Tk()
sim = Simulator(master=root)
sim.mainloop()
