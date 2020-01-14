import tkinter as tk
from tkinter import Frame, Label, Entry, Button

from app.models.users import Users
from app.view.app import App
from app.view.register import Register
from app.models import session

class Login(tk.Frame):
    # constructor method
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        # window size
        root.geometry('300x100')

        self.email_label = Label(self, text="Email").grid(row=0, column=0)
        self.password_label = Label(self, text="Password").grid(row=1, column=0)

        self.email = Entry(self)
        self.email.grid(row=0, column=1)

        self.password = Entry(self, show="*")
        self.password.grid(row=1, column=1)

        # check if the inputs are valid then redirect to the main app
        self.login_button = Button(self, text="Login", command=self.check_credentials).grid(row=2, column=0)
        self.register_button = Button(self, text="Create account", command=lambda: root.switch_frame(Register)) \
            .grid(row=2, column=1)

        self.error_label = Label(self, text="", fg="red")
        self.error_label.grid(row=3, column=1)

    def check_credentials(self):
        # check if the inputs exist
        if self.email.get() != "" and self.password.get() != "":
            # check if there's any user in the db with that email
            try:
                _user = session.query(Users).filter_by(email=self.email.get()).first()
                if _user:
                    # check if the input password matches with the one from the db
                    if _user.email == self.email.get() and _user.password == self.password.get():
                        self.root.switch_frame(App, user=_user)
                    else:
                        self.error_label.config(text="Invalid username/password")
                else:
                    self.error_label.config(text="Invalid username/password")
            except:
                pass
        else:
            self.error_label.config(text="Invalid username/password")
