import tkinter as tk
from tkinter import Frame, Label, Entry, Button

from app.models import session
from app.models.users import Users


class Invoices(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        self.CURRENT_USER = session.query(Users).filter_by(id=kwargs['user_id']).first()


        # create a new frame
        tk.Frame.__init__(self, root)



        self.title_label = Label(self, text="Invoices", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.pack(side='top')