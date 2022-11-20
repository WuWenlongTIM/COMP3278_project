import tkinter as tk
import login as lg
import timetable as tm
import backendConnector as bk
from tkinter.messagebox import showerror
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # s = ttk.Style()
        # s.configure("TFrame", background="white")

        self.login = False
        self.title("ICMS")
        self.geometry("480x180")
        self.resizable(False, False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.loginFrame = lg.LoginFrame(self)
        self.loginFrame.config(borderwidth=1, relief=tk.GROOVE)
        self.loginFrame.grid(sticky=tk.NSEW, column=0, row=0)

        self.timeTableFrame = tm.TimeTableFrame(self)
        self.timeTableFrame.config(borderwidth=1, relief=tk.GROOVE)
        self.timeTableFrame.grid(sticky=tk.NSEW, column=0, row=0)

        self.loginFrame.tkraise()
        self.after(1000, self.refresh())

    def passwordLogin(self, u, p):
        if bk.passwordLogin(u, p):
            showerror("Error", "Username And Password Do Not Match!")
        else:
            self.geometry("1200x720")
            self.login = True
            self.refresh()

    def faceLogin(self):
        if bk.faceLogin():
            showerror("Error", "User Not Exist")
        else:
            self.geometry("1200x730")
            self.login = True
            self.refresh()

    def logout(self):
        self.geometry("480x180")
        self.login = False
        self.refresh()

    def refresh(self):

        self.loginFrame.destroy()
        self.loginFrame = lg.LoginFrame(self)
        self.loginFrame.config(borderwidth=1, relief=tk.GROOVE)
        self.loginFrame.grid(sticky=tk.NSEW, column=0, row=0)

        self.timeTableFrame.destroy()
        self.timeTableFrame = tm.TimeTableFrame(self)
        self.timeTableFrame.config(borderwidth=1, relief=tk.GROOVE)
        self.timeTableFrame.grid(sticky=tk.NSEW, column=0, row=0)

        if self.login:
            self.timeTableFrame.tkraise()
        else:
            self.loginFrame.tkraise()


app = App()
app.mainloop()
