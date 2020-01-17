from tkinter import *
import sys

from app.models import session
from app.models.users import Users


class View_Profile(Frame):

    def __init__(self, root, *args, **kwargs):
        # create a new frame
        Frame.__init__(self, root)


        self.title_label = Label(self, text="Your Profile", font=('Helvetica', 15))
        self.title_label.grid(row=1, column=1, columnspan=2, pady=10)
        self.user = session.query(Users).filter_by(id=kwargs['user_id']).first()

        self.remove_button = Button(self, text="Remove Profile", command=self.removeConfirm)
        self.remove_button.grid(row=2, column=1, pady=5)

        self.first_name_title = Label(self, text="First Name:").grid(row=3, column=1, padx=20, pady=10)
        self.first_name_value = Label(self, text=self.user.first_name)
        self.first_name_value.grid(row=3, column=2, padx=20, pady=10, sticky="W")

        self.last_name_title = Label(self, text="Last Name:") \
            .grid(row=4, column=1, padx=20, pady=10)
        self.last_name_value = Label(self, text=self.user.last_name)
        self.last_name_value.grid(row=4, column=2, padx=20, pady=10, sticky="W")

        self.email_title = Label(self, text="Email:") \
            .grid(row=5, column=1, padx=20, pady=10)
        self.email_value = Label(self, text=self.user.email)
        self.email_value.grid(row=5, column=2, padx=20, pady=10, sticky="W")

        self.password_title = Label(self, text="Password:") \
            .grid(row=6, column=1, padx=20, pady=10)
        self.password_value = Label(self, text=self.user.password)
        self.password_value.grid(row=6, column=2, padx=20, pady=10, sticky="W")

        self.address_title = Label(self, text="Address:") \
            .grid(row=7, column=1, padx=20, pady=10)
        self.address_value = Label(self, text=self.user.address)
        self.address_value.grid(row=7, column=2, padx=20, pady=10, sticky="W")

        self.post_code_title = Label(self, text="Post Code:") \
            .grid(row=8, column=1, padx=20, pady=10)
        self.post_code_value = Label(self, text=self.user.post_code)
        self.post_code_value.grid(row=8, column=2, padx=20, pady=10, sticky="W")

        self.city_title = Label(self, text="City:") \
            .grid(row=9, column=1, padx=20, pady=10)
        self.city_value = Label(self, text=self.user.city)
        self.city_value.grid(row=9, column=2, padx=20, pady=10, sticky="W")

        self.phone_no_title = Label(self, text="Contact Number:") \
            .grid(row=10, column=1, padx=20, pady=10)
        self.phone_no_value = Label(self, text=self.user.phone_no)
        self.phone_no_value.grid(row=10, column=2, padx=20, pady=10, sticky="W")

    def removeConfirm(self):
        confirm_window = Tk()
        confirm_label = Label(confirm_window, text="Are you sure you want\nto delete this profile?\n"
                                                   "(This will close the program)")
        no_button = Button(confirm_window, text="No", command=lambda: confirm_window.destroy())
        yes_button = Button(confirm_window, text="Yes", command=lambda: self.removeProfile(confirm_window))

        confirm_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        no_button.grid(row=2, column=1, padx=10, pady=10)
        yes_button.grid(row=2, column=2, padx=10, pady=10)

    def removeProfile(self,confirm_window):
        session.delete(session.query(Users).filter_by(id=self.user.id).first())
        session.commit()
        confirm_window.destroy()
        sys.exit()