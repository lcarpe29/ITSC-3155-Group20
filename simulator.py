import tkinter as tk
import mysql.connector


class Simulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('Banking Simulation')
        master.geometry('500x500')
        self.pack()
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7NJn-N\\ar_<3PS~T",
            database="bankingsimulator"
        )
        self.cursor = self.db.cursor()
        self.signinWindow()

    def signinWindow(self):
        self.signinFrame = tk.Frame(self)
        self.signinFrame.pack()

        tk.Label(self.signinFrame, text="Enter Email: ").pack()
        self.entrySigninEmail = tk.Entry(self.signinFrame)
        self.entrySigninEmail.pack()
        tk.Label(self.signinFrame, text="Enter Password: ").pack()
        self.entrySigninPassword = tk.Entry(self.signinFrame, show='*')
        self.entrySigninPassword.pack()

        tk.Button(self.signinFrame, text="Sign In", command=self.signinProcess).pack(side="left")
        tk.Button(self.signinFrame, text="Sign Up", command=self.signupWindow).pack(side="right")
        tk.Button(self.signinFrame, text="Quit", fg="red", command=self.master.destroy).pack(side="bottom")

    def homeWindow(self):
        self.signinFrame.destroy()
        self.homeFrame = tk.Frame(self)
        self.homeFrame.pack()

        tk.Label(self.homeFrame, text="This will be money").pack()

    def signupWindow(self):
        self.signinFrame.destroy()

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

        tk.Button(self.signupFrame, text="Create Account", command=self.createAccount).pack(side="bottom")
        tk.Button(self.signupFrame, text="Back", command=self.fromSignupToSignin).pack(side="left")
        tk.Button(self.signupFrame, text="Quit", fg="red", command=self.master.destroy).pack(side="right")

    def fromSignupToSignin(self):
        self.signupFrame.destroy()
        self.signinWindow()

    def fromHomeToSignin(self):
        self.homeFrame.destroy()
        self.signinWindow()

    def createAccount(self):
        if ((len(self.entrySignupFirstName.get()) != 0) and (len(self.entrySignupLastName.get()) != 0) and
                (len(self.entrySignupEmail.get()) != 0) and (len(self.entrySignupPassword.get()) != 0)):
            firstName = self.entrySignupFirstName.get()
            lastName = self.entrySignupLastName.get()
            email = self.entrySignupEmail.get()
            password = self.entrySignupPassword.get()

            insertCommand = "INSERT INTO Users (userFirstName, userLastName, userEmail, userPassword) " \
                            "VALUES( '" + firstName + "', '" + lastName + "', '" + email + "', '" + password + "');"
            self.cursor.execute(insertCommand)
            self.db.commit()

            self.fromSignupToSignin()
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
        if ((len(self.entrySigninEmail.get()) != 0) and (len(self.entrySigninPassword.get()) != 0)):
            email = self.entrySigninEmail.get()
            self.cursor.execute("SELECT userPassword "
                                "FROM Users "
                                "WHERE userEmail = '" + email + "';"
                                )
            userPassword = self.cursor.fetchone()

            while userPassword is not None:
                userPassword = self.cursor.fetchone()
            print(userPassword)
            print(self.entrySigninPassword)
            if (userPassword == self.entrySigninPassword.get()):
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
