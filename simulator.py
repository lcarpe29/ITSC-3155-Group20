import tkinter as tk
import tkinter.font as font
import mysql.connector

from user import User
from admin import Admin


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
        self.signinWindow()

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
        # todo signup btn doesn't work -- request new account?
        btnSignup = tk.Button(self.signinFrame, text="Sign Up", highlightbackground='#ffcc00', fg='green',
                              command=self.signupWindow)
        btnSignup.pack(side="right")
        btnQuit = tk.Button(self.signinFrame, text="Quit", highlightbackground='#ffcc00', fg="red",
                            command=self.master.destroy)
        btnQuit.pack(side="bottom")

    # Account holder Windows
    def homeWindow(self):
        self.signinFrame.destroy()
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

        tk.Button(self.adminHomeFrame, text="New Account", command=self.signupWindow).pack()
        tk.Button(self.adminHomeFrame, text="User Transaction", command=self.transactionWindow).pack()

    def signupWindow(self):
        self.adminHomeFrame.destroy()

        self.signupFrame = tk.Frame(self)
        self.signupFrame.pack()

        tk.Label(self.signupFrame, text="Enter First Name: ").pack()
        self.entrySignupFirstName = tk.Entry(self.signupFrame)
        self.entrySignupFirstName.pack()
        tk.Label(self.signupFrame, text="Enter Last Name: ").pack()
        self.entrySignupLastName = tk.Entry(self.signupFrame)
        self.entrySignupLastName.pack()
        tk.Label(self.signupFrame, text="Enter Email: ").pack()
        self.entrySignupEmail = tk.Entry(self.signupFrame)
        self.entrySignupEmail.pack()
        tk.Label(self.signupFrame, text="Enter Password: ").pack()
        self.entrySignupPassword = tk.Entry(self.signupFrame, show='*')
        self.entrySignupPassword.pack()
        self.adminCheck = tk.IntVar()
        self.cbSignupAdminAccount = tk.Checkbutton(self.signupFrame, text="Admin Account",
                                                   variable=self.adminCheck, onvalue=1)
        self.cbSignupAdminAccount.pack()

        tk.Button(self.signupFrame, text="Create Account", command=self.createAccount).pack(side="bottom")
        tk.Button(self.signupFrame, text="Back", command=self.fromSignupToAdmin).pack(side="left")
        tk.Button(self.signupFrame, text="Quit", fg="red", command=self.master.destroy).pack(side="right")

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
        tk.Label(self.transactionFrame, text="Enter Account ID").pack()
        self.entryTransactionAccountID = tk.Entry(self.transactionFrame)
        self.entryTransactionAccountID.pack()
        tk.Label(self.transactionFrame, text="Transaction Amount: ").pack()
        self.entryTransactionAmount = tk.Entry(self.transactionFrame)
        self.entryTransactionAmount.pack()

        self.btnTransactionOkay = tk.Button(self.transactionFrame, text="Okay", command=self.withdrawDeposit).pack()

    # Transition Methods
    def fromSignupToAdmin(self):
        self.signupFrame.destroy()
        self.adminHomeWindow()

    def fromHomeToSignin(self):
        self.homeFrame.destroy()
        self.signinWindow()

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
                print("AccountID doesn't exits")
            else:
                for row in userInfo:
                    firstName = row[1]
                    lastName = row[2]
                    password = row[4]
                    balance = float(row[5])

                userForTransaction = User(firstName, lastName, password, balance, accountID)

                if self.wdVar.get() == 2:
                    self.adminInstance.user_deposit(userForTransaction, amount)
                else:
                    self.adminInstance.user_withdraw(userForTransaction, amount)

                self.transactionFrame.destroy()
                self.adminHomeWindow()

        elif self.wdVar.get() == 0:
            # todo add pop up
            print("Select either withdraw or deposit")
        elif len(self.entryTransactionAccountID.get()) == 0:
            # todo add pop up
            print("Enter Account ID")
        elif len(self.entryTransactionAmount.get()) == 0:
            # todo add pop up
            print("Enter transaction amount")
        else:
            # todo add pop up
            print("Internal Error")

    def createAccount(self):
        if ((len(self.entrySignupFirstName.get()) != 0) and (len(self.entrySignupLastName.get()) != 0) and
                (len(self.entrySignupEmail.get()) != 0) and (len(self.entrySignupPassword.get()) != 0)):
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
            if len(self.entrySignupFirstName.get()) == 0:
                # todo add popup
                print("No First Name")
            elif len(self.entrySignupLastName.get()) == 0:
                # todo add popup
                print("No Last Name")
            elif len(self.entrySignupEmail.get()) == 0:
                # todo add popup
                print("No Email")
            elif len(self.entrySignupPassword.get()) == 0:
                # todo add popup
                print("No Password")
            else:
                # todo add popup
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
                    self.userInstance = User(firstName, lastName, password, balance, accountID)
                    self.homeWindow()
            else:
                # todo add popup
                print("Password is wrong")
        else:
            if len(self.entrySigninEmail.get()) == 0:
                # todo add popup
                print("No Email")
            elif len(self.entrySigninPassword.get()) == 0:
                # todo add popup
                print("No Password")
            else:
                # todo add popup
                print("Error")


root = tk.Tk()
sim = Simulator(master=root)
sim.mainloop()
