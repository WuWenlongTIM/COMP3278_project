import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.welcomeFrame = WelcomeFrame(self)
        self.welcomeFrame.config(borderwidth=1, relief=tk.GROOVE)
        self.welcomeFrame.grid(column=0, row=0, sticky=tk.NSEW)
        self.controlFrame = ControlFrame(self)
        self.controlFrame.config(borderwidth=1, relief=tk.GROOVE)
        self.controlFrame.grid(column=1, row=0, sticky=tk.NSEW)


class WelcomeFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        icon = tk.PhotoImage(file="book.png")
        self.book_icon = icon.subsample(2)

        self.label = ttk.Label(self)
        self.label.config(image=self.book_icon)
        self.label.grid(column=0, row=0)


class ControlFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=1)
        self.rowconfigure(index=3, weight=1)
        self.rowconfigure(index=4, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.label = ttk.Label(
            self, text="Log in:", font='Monaco 18 bold' 
        )
        self.label.grid(column=0, row=0, sticky=tk.SW, padx=10)

        self.strvu = tk.StringVar(self, value="Username")
        self.strvp = tk.StringVar(self, value="Password")
        self.firstu = True
        self.firstp = True
        # self.strvu = tk.StringVar(self, value="Tim")
        # self.strvp = tk.StringVar(self, value="123456")
        # self.firstu = False
        # self.firstp = False
        self.entryu = ttk.Entry(self, textvariable=self.strvu)
        self.entryu.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky=tk.EW,
            padx=10,
            pady=10,
            ipadx=0,
            ipady=3,
        )
        self.entryp = ttk.Entry(self, textvariable=self.strvp)
        self.entryp.grid(
            column=0,
            row=2,
            columnspan=2,
            sticky=tk.EW,
            padx=10,
            pady=10,
            ipadx=0,
            ipady=3,
        )
        self.entryu.bind("<FocusIn>", self.clearu)
        self.entryp.bind("<FocusIn>", self.clearp)

        self.buttonp = ttk.Button(self, text="password login", width=20)
        self.buttonp.grid(column=0, row=3, sticky=tk.S, pady=5, ipadx=0, ipady=0)
        self.buttonp.bind("<Button>", self.passwordlogin)

        self.buttonf = ttk.Button(self, text="face login", width=20)
        self.buttonf.grid(column=1, row=3, sticky=tk.N, pady=5, ipadx=0, ipady=0)
        self.buttonf.bind("<Button>", self.facelogin)

    def clearu(self, event):
        if self.firstu:
            self.firstu = False
            self.strvu.set("")

    def clearp(self, event):
        if self.firstp:
            self.firstp = False
            self.strvp.set("")
            self.entryp.config(show="*")

    def passwordlogin(self, event):
        if self.firstu or self.firstp:
            showerror("Error", "No Input")
        else:
            u = self.strvu.get().strip()
            p = self.strvp.get().strip()
            if u == "" or p == "":
                showerror("Error", "No Input")
            else:
                self.container.container.passwordLogin(u, p)

    def facelogin(self, event):
        self.container.container.faceLogin()

    def reset(self):
        self.strvu = tk.StringVar(self, value="Username")
        self.strvp = tk.StringVar(self, value="Password")
        self.firstu = True
        self.firstp = True
