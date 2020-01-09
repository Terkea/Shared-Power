import tkinter as tk
from tkinter import Frame, Label, Entry, Button

from app.view.content_frames.basket import Basket
from app.view.content_frames.bookings import Bookings
from app.view.content_frames.invoices import Invoices
from app.view.content_frames.tools import Tools
from app.view.content_frames.view_profile import View_Profile
from app.view.content_frames.welcome import Welcome


class App(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        # create a new frame
        tk.Frame.__init__(self, root)

        # user
        self.USER = kwargs['user']

        # frame size
        root.geometry('1000x500')

        # both width and height are not resizable
        root.resizable(False, False)

        # column, row sizes
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        # set the content frame size to 800
        self.grid_columnconfigure(1, minsize=800)
        self.rowconfigure(0, minsize=500)

        # create the frames
        self.users_menu_frame = Frame(self, background='red')
        self.welcome_frame = Frame(self, background='blue')
        self.view_profile = Frame(self, background='green')

        # this is the frame that the user will see when they log in
        self.content_frame = Welcome(self)

        # column/row configurations for menu frame
        self.users_menu_frame.grid_columnconfigure(0, minsize=150)
        self.users_menu_frame.grid_rowconfigure(0, minsize=50)
        self.users_menu_frame.grid_rowconfigure(1, minsize=40)
        self.users_menu_frame.grid_rowconfigure(2, minsize=40)
        self.users_menu_frame.grid_rowconfigure(3, minsize=40)
        self.users_menu_frame.grid_rowconfigure(4, minsize=40)
        self.users_menu_frame.grid_rowconfigure(5, minsize=40)

        # items for menu frame
        hello_label = tk.Label(self.users_menu_frame, text='Hello, User').grid(column=0, row=0, sticky='nswe')

        view_profile_button = tk.Button(self.users_menu_frame, text="View Profile", command=lambda: self.switch_frame(
            View_Profile(self, user_id=self.USER.id)))\
            .grid(column=0, row=1, sticky='nswe')

        invoices_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Invoices(self, user_id=self.USER.id)),text="Invoices")\
            .grid(column=0, row=2, sticky='nswe')

        bookings_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Bookings(self, user_id=self.USER.id)), text="View bookings")\
            .grid(column=0, row=3, sticky='nswe')

        tools_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Tools(self, user_id=self.USER.id)), text="Search tools")\
            .grid(column=0, row=4, sticky='nswe')

        basket_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Basket(self, user_id=self.USER.id)), text="Basket")\
            .grid(column=0, row=5, sticky='nswe')

        # the position of the frames in the main one
        self.users_menu_frame.grid(column=0, row=0, sticky='nswe')
        self.content_frame.grid(column=1, row=0, sticky='nswe')

    def switch_frame(self, frame):
        """
        swaps the content frame in view with the one passed as param
        :param frame: Frame
        """
        if self.content_frame is not frame:
            self.content_frame.grid_forget()
            self.content_frame = frame
            self.content_frame.grid(column=1, row=0, sticky='nswe')
