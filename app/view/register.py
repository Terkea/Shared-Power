import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class Register(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # window size
        root.geometry('600x400')

        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 20

        tk.Label(self, text="Register page", font=(self.FONT, self.TITLE_SIZE)).pack(side="top", fill="x", pady=5)
        # idk why but for some reason if you import this at the top of the file it will crash
        # I spent like 2 hours trying to fix this, so better don't touch it!!!
        from app.view.login import Login
        

        # Labels
        self.first_name_label = Label(self, text="First name")
        self.last_name_label = Label(self, text="Last name")
        self.email_label = Label(self, text="Email")
        self.address_label = Label(self, text="Address")
        self.post_code_label = Label(self, text="Post code")
        self.city_label = Label(self, text="City")
        self.phone_no_label = Label(self, text="Phone no.")
        self.user_type = Label(self, text="User type")
        self.password_label = Label(self, text="Password")
        self.check_password_label = Label(self, text="Check password")


        self.first_name_label.pack()
        self.last_name_label.pack()
        self.email_label.pack()
        self.address_label.pack()
        self.post_code_label.pack()
        self.city_label.pack()
        self.phone_no_label.pack()
        self.user_type.pack()
        self.password_label.pack()
        self.check_password_label.pack()


        tk.Button(self, text="Register account",
                  command=lambda: root.switch_frame(Login)).pack()
