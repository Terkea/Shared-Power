import tkinter as tk
import datetime
from tkinter import *
from tkinter.ttk import *

from tkcalendar import DateEntry

from app.models import session
from app.models.booking import Booking
from app.models.checkout import Checkout
from app.models.tools import Tools


class Tools_frame(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # create a new frame
        tk.Frame.__init__(self, root)

        # grab the user with the specified id to query for his tools
        self.CURRENT_USER = kwargs['user_id']

        self.title_label = Label(self, text="Tools", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.pack(side='top')

        self.order_button = Button(self, command=self.book_tool_frame, text="Order")
        self.order_button.pack(anchor="w")

        self.search_field = Entry(self)
        self.search_field.pack(fill=tk.BOTH)

        self.search_button = Button(self, command=self.search_tool, text="Search")
        self.search_button.pack(anchor="e")

        self.error_label = Label(self, text="")
        self.error_label.pack()

        self.createTable()
        self.loadTable()

    def search_tool(self):
        # grab the keyword from the search field
        keyword = self.search_field.get()

        # clear the table
        self.treeview.delete(*self.treeview.get_children())

        # repopulate the table with the search results
        _search_tools = []
        for tool in session.query(Tools).filter(Tools.name.like("%" + keyword + "%")):
            _search_tools.append(tool)

        print(_search_tools)

        for tool in _search_tools:
            self.treeview.insert('', 'end', text=tool.id,
                                 values=(tool.name,
                                         tool.description, tool.daily_price + " GBP", tool.half_day_price + " GBP"))

    def book_tool_frame(self):
        self.tool_id = self.treeview.item(self.treeview.selection(), "text")

        _tool = session.query(Tools).filter_by(id=self.tool_id).first()

        # clear the frame
        self.title_label.destroy()
        self.order_button.destroy()
        self.search_field.destroy()
        self.search_button.destroy()
        self.treeview.destroy()

        # recreate the window
        self.title_label = Label(self, text="Order tool", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.pack(side='top')

        self.tool_name_label = Label(self, text=_tool.name)
        self.tool_name_label.pack()

        self.notice_label = Label(self, text="Starting from")
        self.notice_label.pack()

        today = datetime.date.today()
        maxdate = today + datetime.timedelta(days=60)
        self.calendar = DateEntry(self, width=12, maxdate=maxdate, mindate=today, background='darkblue',
                                  foreground='white', disabledforeground='red', borderwidth=2, year=2020)
        self.calendar.pack()

        self.calendar_label = Label(self, text="For how many days would you like to rent the tool?")
        self.calendar_label.pack()

        self.how_many_days = DoubleVar()
        self.period_of_time = Combobox(self, textvariable=self.how_many_days)
        self.period_of_time.pack()
        self.period_of_time["values"] = [1, 1.5, 2, 2.5, 3]

        self.delivery_label = Label(self, text="Delivery?")
        self.delivery_label.pack()

        self.delivery = IntVar()
        self.delivery_input = tk.Radiobutton(self, text="Yes", value=1, variable=self.delivery)
        self.delivery_input.pack()
        self.delivery_input2 = tk.Radiobutton(self, text="No", value=2, variable=self.delivery)
        self.delivery_input2.pack()

        self.validation_label = Label(self, text="")
        self.validation_label.pack()

        self.book_button = Button(self, command=self.book_tool, text="Add item to the basket")
        self.book_button.pack()

    def book_tool(self):
        validators = {
            "days": False,
            "availability": True
        }

        # validation
        if self.how_many_days.get() == 0:
            self.validation_label.config(text="You have to select a period of time for your booking")
            validators['days'] = False
        else:
            validators["days"] = False

        # check the availability of the tool
        # grab all the bookings for the selected tool
        _bookings = session.query(Booking).filter(Booking.tool_id == self.tool_id).all()

        already_booked = False
        for booking in _bookings:
            their_booking_day = booking.booked_date
            their_period_of_time = booking.duration_of_booking
            their_deltatime = datetime.datetime.strptime(their_booking_day, '%Y-%m-%d') +\
                              datetime.timedelta(days=float(their_period_of_time))

            my_booking_day = datetime.datetime.combine(self.calendar.get_date(), datetime.time.min)
            my_period_of_time = self.period_of_time.get()
            my_deltatime = my_booking_day + datetime.timedelta(days=float(my_period_of_time))

            if their_deltatime > my_booking_day:
                # the tool is booked in that daterange
                self.validation_label.config(text=f"Somebody booked that tool in that daterange "
                                                  f"{their_booking_day} - {their_deltatime}")
                break
            else:
                validators["days"] = True

        if validators['days'] == True and validators["availability"] == True:
            order = Checkout()
            order.user_id = self.CURRENT_USER
            order.tool_id = self.tool_id
            order.duration_of_booking = self.how_many_days.get()
            order.booked_date = self.calendar.get_date()

            if self.delivery.get() == 1:
                order.delivery = True
            else:
                order.delivery = False

            session.add(order)
            session.commit()

            self.validation_label.config(text="Item added to basked")

        # print(self.calendar.get())
        # print(self.how_many_days.get())
        # print(self.CURRENT_USER, self.tool_id)

    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = tk.Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('tool_name', 'description', 'daily_price', 'half_day_price')

        tv.heading("#0", text='ID', anchor='w')
        tv.column("#0", anchor="w", width=10)

        tv.heading('tool_name', text='Tool name')
        tv.column('tool_name', anchor='center', width=100)

        tv.heading('description', text='Description')
        tv.column('description', anchor='center', width=150)

        tv.heading('daily_price', text='Daily price')
        tv.column('daily_price', anchor='center', width=50)

        tv.heading('half_day_price', text='Half day price')
        tv.column('half_day_price', anchor='center', width=100)

        tv.pack(fill=BOTH, expand=1)
        self.treeview = tv

    def loadTable(self):
        # get the tools and store them into this list
        # could use list comprehension to keep the syntax prettier but IDK how to do that with sql
        # alchemy and I got no time to spend researching that
        _tools = []
        for tool in session.query(Tools):
            _tools.append(tool)

        for tool in _tools:
            self.treeview.insert('', 'end', text=tool.id,
                                 values=(tool.name,
                                         tool.description, tool.daily_price + " GBP", tool.half_day_price + " GBP"))
