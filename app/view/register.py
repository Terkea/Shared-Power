import tkinter as tk
from tkinter import Frame, Label, Entry, Button

from app.models import session
from app.models.users import Users

from werkzeug.security import generate_password_hash


class Register(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        # window size
        root.geometry('600x400')

        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 20

        tk.Label(self, text="Register page", font=(self.FONT, self.TITLE_SIZE)).grid(row=0, column=0)

        # Labels
        self.first_name_label = Label(self, text="First name")
        self.last_name_label = Label(self, text="Last name")
        self.email_label = Label(self, text="Email")
        self.address_label = Label(self, text="Address")
        self.post_code_label = Label(self, text="Post code")
        self.city_label = Label(self, text="City")
        self.phone_no_label = Label(self, text="Phone no.")
        self.user_type_label = Label(self, text="User type")
        self.password_label = Label(self, text="Password")
        self.check_password_label = Label(self, text="Check password")

        self.first_name_label.grid(row=1, column=0)
        self.last_name_label.grid(row=2, column=0)
        self.email_label.grid(row=3, column=0)
        self.address_label.grid(row=4, column=0)
        self.post_code_label.grid(row=5, column=0)
        self.city_label.grid(row=6, column=0)
        self.phone_no_label.grid(row=7, column=0)
        self.user_type_label.grid(row=8, column=0)
        self.password_label.grid(row=9, column=0)
        self.check_password_label.grid(row=10, column=0)

        # Inputs
        self.user_type = tk.IntVar()
        self.first_name_input = Entry(self)
        self.last_name_input = Entry(self)
        self.email_input = Entry(self)
        self.address_input = Entry(self)
        self.post_code_input = Entry(self)
        self.city_input = Entry(self)
        self.phone_no_input = Entry(self)
        self.user_type_input = tk.Radiobutton(self, text="Supplier", value=1, variable=self.user_type)
        self.user_type_input2 = tk.Radiobutton(self, text="Regular user", value=2, variable=self.user_type)
        self.password_input = Entry(self, show="*")
        self.check_password_input = Entry(self, show="*")

        self.first_name_input.grid(row=1, column=1)
        self.last_name_input.grid(row=2, column=1)
        self.email_input.grid(row=3, column=1)
        self.address_input.grid(row=4, column=1)
        self.post_code_input.grid(row=5, column=1)
        self.city_input.grid(row=6, column=1)
        self.phone_no_input.grid(row=7, column=1)
        self.user_type_input.grid(row=8, column=1)
        self.user_type_input2.grid(row=8, column=2)
        self.password_input.grid(row=9, column=1)
        self.check_password_input.grid(row=10, column=1)

        self.register_button = tk.Button(self, text="Register account", command=self.validate_inputs)
        self.register_button.grid(row=11, column=0)

        self.error_label = Label(self, text="", fg="red")
        self.error_label.grid(row=11, column=1)

    def validate_inputs(self):
        validators = {"empty": True, "password_match": True, "unique_email": True}

        # check if all fields have values
        all_inputs = [self.first_name_input.get(),
                      self.last_name_input.get(),
                      self.email_input.get(),
                      self.address_input.get(),
                      self.post_code_input.get(),
                      self.city_input.get(),
                      self.phone_no_input.get(),
                      self.user_type.get(),
                      self.password_input.get(),
                      self.check_password_input.get()]

        for field in all_inputs:
            if field == "":
                self.error_label.config(text="Please fill all fields")
                validators['empty'] = False

        # check if the passwords match
        if self.password_input.get() is not self.check_password_input.get():
            self.error_label.config(text="Passwords doesnt match")
            validators["password_match"] = False

        # check if the email is available
        _user = session.query(Users).filter_by(email=self.email_input.get()).first()

        if _user == None:
            pass
        else:
            self.error_label.config(text="Email address already taken")
            validators['unique_email'] = False

        # there is a better way to get this done but atm I'm just too tired, but as long as it works we'll be fine
        if validators["empty"] == True and validators["password_match"] == True and validators["unique_email"] == True:
            # add the user to the db
            new_user = Users()
            new_user.first_name = self.first_name_input.get()
            new_user.last_name = self.last_name_input.get()
            new_user.email = self.email_input.get()
            new_user.address = self.address_input.get()
            new_user.post_code = self.post_code_input.get()
            new_user.city = self.city_input.get()
            new_user.phone_no = self.phone_no_input.get()
            new_user.password = generate_password_hash(self.password_input.get(), method='sha256')
            if self.user_type.get() == 1:
                new_user.is_supplier = True
            else:
                new_user.is_supplier = False

            session.add(new_user)
            session.commit()

            # idk why but for some reason if you import this at the top of the file it will crash
            # I spent like 2 hours trying to fix this, so better don't touch it!!!
            from app.view.login import Login
            self.root.switch_frame(Login)
