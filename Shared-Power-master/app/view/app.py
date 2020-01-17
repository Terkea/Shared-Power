import tkinter as tk
from tkinter import Frame

from app.view.content_frames.basket import Basket
from app.view.content_frames.bookings import Bookings
from app.view.content_frames.invoice import Invoice
from app.view.content_frames.owner_tools import OwnerTools
from app.view.content_frames.customer_tools import CustomerTools
from app.view.content_frames.view_profile import View_Profile


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
        self.users_menu_frame = Frame(self)
        self.supplier_menu_frame = Frame(self)

        # this is the frame that the user will see when they log in
        if self.USER.is_supplier:
            self.content_frame = OwnerTools(self, user_id=self.USER.id)
        else:
            self.content_frame = CustomerTools(self, user_id=self.USER.id)

        # column/row configurations for user menu frame
        self.users_menu_frame.grid_columnconfigure(0, minsize=150)
        self.users_menu_frame.grid_rowconfigure(0, minsize=50)
        self.users_menu_frame.grid_rowconfigure(1, minsize=40)
        self.users_menu_frame.grid_rowconfigure(2, minsize=40)
        self.users_menu_frame.grid_rowconfigure(3, minsize=40)
        self.users_menu_frame.grid_rowconfigure(4, minsize=40)
        self.users_menu_frame.grid_rowconfigure(5, minsize=40)

        # column/row configurations for supplier menu frame
        self.supplier_menu_frame.grid_columnconfigure(0, minsize=150)
        self.supplier_menu_frame.grid_rowconfigure(0, minsize=50)
        self.supplier_menu_frame.grid_rowconfigure(1, minsize=40)
        self.supplier_menu_frame.grid_rowconfigure(2, minsize=40)
        self.supplier_menu_frame.grid_rowconfigure(3, minsize=40)

        # items for menu frame
        hello_label = tk.Label(self.users_menu_frame, text=f"Hello, {self.USER.first_name}").\
            grid(column=0, row=0, sticky='nswe')
        hello_label = tk.Label(self.supplier_menu_frame, text=f"Hello, {self.USER.first_name}"). \
            grid(column=0, row=0, sticky='nswe')

        home_button = tk.Button(self.users_menu_frame, text="Home", command=lambda: self.switch_frame(
            CustomerTools(self, user_id=self.USER.id))).grid(column=0, row=1, sticky='nswe')
        home_button = tk.Button(self.supplier_menu_frame, text="Home", command=lambda: self.switch_frame(
            OwnerTools(self, user_id=self.USER.id))).grid(column=0, row=1, sticky='nswe')

        view_profile_button = tk.Button(self.users_menu_frame, text="View Profile", command=lambda: self.switch_frame(
            View_Profile(self, user_id=self.USER.id)))\
            .grid(column=0, row=2, sticky='nswe')
        view_profile_button = tk.Button(self.supplier_menu_frame, text="View Profile", command=lambda: self.switch_frame(
            View_Profile(self, user_id=self.USER.id))) \
            .grid(column=0, row=2, sticky='nswe')

        invoices_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Invoice(self, user_id=self.USER.id)),text="Invoices")\
            .grid(column=0, row=3, sticky='nswe')
        invoices_button = tk.Button(self.supplier_menu_frame, command=lambda: self.switch_frame(
            Invoice(self, user_id=self.USER.id)),text="Invoices") \
            .grid(column=0, row=3, sticky='nswe')

        bookings_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Bookings(self, user_id=self.USER.id)), text="View bookings")\
            .grid(column=0, row=4, sticky='nswe')
        bookings_button = tk.Button(self.supplier_menu_frame, command=lambda: self.switch_frame(
            Bookings(self, user_id=self.USER.id)), text="View bookings") \
            .grid(column=0, row=4, sticky='nswe')

        basket_button = tk.Button(self.users_menu_frame, command=lambda: self.switch_frame(
            Basket(self, user_id=self.USER.id)), text="Basket")\
            .grid(column=0, row=5, sticky='nswe')


        # the position of the frames in the main one
        # display the proper interface for each user
        if self.USER.is_supplier:
            self.supplier_menu_frame.grid(column=0, row=0, sticky='nswe')
        else:
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
