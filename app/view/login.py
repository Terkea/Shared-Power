import tkinter as tk
from tkinter import Frame, Label, Entry, Button

from app.view.app import App
from app.view.register import Register


class Login(tk.Frame):
    # constructor method
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # window size
        root.geometry('200x100')

        self.email_label = Label(self, text="Email").grid(row=0, column=0)
        self.password_label = Label(self, text="Password").grid(row=1, column=0)

        self.email = Entry(self).grid(row=0, column=1)
        self.password = Entry(self).grid(row=1, column=1)

        self.login_button = Button(self, text="Login", command=lambda: root.switch_frame(App)).grid(row=2, column=0)
        self.register_button = Button(self, text="Create account", command=lambda: root.switch_frame(Register)) \
            .grid(row=2, column=1)

    def redirect_app(self):
        print("app")

    def redirect_register(self):
        print("register")
