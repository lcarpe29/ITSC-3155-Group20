import tkinter as tk
import mysql.connector


class Simulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.geometry('500x500')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hithere = tk.Button(self)
        self.hithere["text"] = "Hello World\n(Click me)"
        self.hithere["command"] = self.say_hi
        self.hithere.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone")


root = tk.Tk()
sim = Simulator(master=root)
sim.mainloop()
