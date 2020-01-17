import tkinter as tk
import datetime
from tkinter import *
from tkinter.ttk import *
import uuid

from tkcalendar import DateEntry

from app.models import session
from app.models.booking import Booking
from app.models.checkout import Checkout
from app.models.tools import Tools


class CustomerTools(tk.Frame):

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

        self.validation_label = Label(self, text="")
        self.validation_label.pack(anchor="w")

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

        self.booking_window = Tk()
        self.booking_window.geometry("250x300")

        # recreate the window
        self.title_label = Label(self.booking_window, text="Order tool", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.grid(row=1, column=1, columnspan=2, pady=10, padx=10)

        self.tool_name_label = Label(self.booking_window, text=_tool.name, font=(self.FONT, 15))
        self.tool_name_label.grid(row=2, column=1, columnspan=2, pady=5, padx=10)

        self.notice_label = Label(self.booking_window, text="Starting from:")
        self.notice_label.grid(row=3, column=1, pady=5, padx=10)

        today = datetime.date.today()
        maxdate = today + datetime.timedelta(days=42)
        self.calendar = DateEntry(self.booking_window, width=12, maxdate=maxdate, mindate=today, background='darkblue',
                                  foreground='white', disabledforeground='red', borderwidth=2, year=2020)
        self.calendar.grid(row=3, column=2, pady=5, padx=10)

        self.calendar_label = Label(self.booking_window, text="Booking Period:")
        self.calendar_label.grid(row=4, column=1, pady=5, padx=10)

        self.period_of_time = Combobox(self.booking_window, values=[1, 1.5, 2, 2.5, 3], width=10)
        self.period_of_time.current(0)
        self.period_of_time.grid(row=4, column=2, pady=5, padx=10)

        self.delivery_label = Label(self.booking_window, text="Delivery?")
        self.delivery_label.grid(row=5, column=1, columnspan=2, pady=5, padx=10)

        self.delivery = IntVar()
        self.delivery_input = tk.Radiobutton(self.booking_window, text="Yes", value=1, variable=self.delivery)
        self.delivery_input.grid(row=6, column=1, pady=5, padx=10, sticky="e")
        self.delivery_input2 = tk.Radiobutton(self.booking_window, text="No", value=2, variable=self.delivery)
        self.delivery_input2.grid(row=6, column=2, pady=5, padx=10, sticky="w",)

        self.book_button = Button(self.booking_window, command=self.book_tool, text="Add to Basket")
        self.book_button.grid(row=7, column=1, columnspan=2, pady=5, padx=10)

    def expandTool(self):

        tool_id = self.treeview.item(self.treeview.selection(), "text")
        tool = session.query(Tools).filter_by(id=tool_id).first()

        expand_window = Tk()
        back_button = Button(expand_window, text="Back", command=lambda: expand_window.destroy())
        back_button.grid(row=1, column=1, padx=10, pady=10, sticky="E")
        order_button = Button(expand_window, text="Edit", command=self.addToBasket)
        order_button.grid(row=2, column=1, padx=10, pady=10, sticky="E")

        name_title = Label(expand_window, text="Tool Name:").grid(row=3, column=1, padx=5, pady=5)
        name_value = Label(expand_window, text=tool.name).grid(row=3, column=2, padx=5, pady=5, sticky="W")

        description_title = Label(expand_window, text="Tool Description:").grid(row=4, column=1, padx=5, pady=5)
        description_value = Message(expand_window, text=tool.description).grid(row=4, column=2, padx=5, pady=5, sticky="W")

        daily_price_title = Label(expand_window, text="Day Hire Price:").grid(row=5, column=1, padx=5, pady=5)
        daily_price_value = Label(expand_window, text=tool.daily_price).grid(row=5, column=2, padx=5, pady=5, sticky="W")

        half_price_title = Label(expand_window, text="Half Day Hire Price:").grid(row=6, column=1, padx=5, pady=5)
        half_price_value = Label(expand_window, text=tool.half_day_price).grid(row=6, column=2, padx=5, pady=5, sticky="W")

        delivery_cost_title = Label(expand_window, text="Delivery Charge:").grid(row=7, column=1, padx=5, pady=5)
        delivery_cost_value = Label(expand_window, text=tool.delivery_cost).grid(row=7, column=2, padx=5, pady=5, sticky="W")

        expand_window.mainloop()

    def book_tool(self):
        validators = {
            "days": False,
            "availability": True
        }

        # validation
        print(self.period_of_time.get())
        if self.period_of_time.get() == 0:
            self.validation_label.config(text="Period of time\nmust be selected")
            validators['days'] = False
        else:
            validators["days"] = True

        # check the availability of the tool
        # grab all the bookings for the selected tool
        _bookings = session.query(Booking).filter(Booking.tool_id == self.tool_id).all()

        already_booked = False
        for booking in _bookings:
            their_booking_day = booking.booked_date
            their_period_of_time = booking.duration_of_booking
            their_deltatime = datetime.datetime.strptime(their_booking_day, '%Y-%m-%d') +\
                              datetime.timedelta(days=float(their_period_of_time))

            my_booking_day = self.calendar.get_date()

            if their_deltatime > my_booking_day:
                # the tool is booked in that daterange
                self.validation_label.config(text=f"Somebody booked that tool in that daterange "
                                                  f"{their_booking_day} - {their_deltatime}")
                break
            else:
                validators["days"] = True

        if validators['days'] == True and validators["availability"] == True:
            order = Checkout()
            order.id = uuid.uuid4().hex
            order.user_id = self.CURRENT_USER
            order.tool_id = self.tool_id
            order.duration_of_booking = self.period_of_time.get()
            order.booked_date = self.calendar.get_date()

            if self.delivery.get() == 1:
                order.delivery = True
            else:
                order.delivery = False

            session.add(order)
            session.commit()

            self.validation_label.config(text="Item added to basket!")
            self.booking_window.destroy()


        # print(self.calendar.get())
        # print(self.how_many_days.get())
        # print(self.CURRENT_USER, self.tool_id)

    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('tool_name', 'description', 'daily_price', 'half_day_price', 'delivery_cost')

        tv.heading("#0", text='ID', anchor='w')
        tv.column("#0", anchor="w", width=10)

        tv.heading('tool_name', text='Tool name')
        tv.column('tool_name', anchor='center', width=100)

        tv.heading('description', text='Description')
        tv.column('description', anchor='center', width=150)

        tv.heading('daily_price', text='Daily price')
        tv.column('daily_price', anchor='center', width=50)

        tv.heading('half_day_price', text='Half day price')
        tv.column('half_day_price', anchor='center', width=50)

        tv.heading('delivery_cost', text='Delivery Charge')
        tv.column('delivery_cost', anchor='center', width=50)

        tv.pack(fill=BOTH, expand=1)
        self.treeview = tv


    def loadTable(self):
        # get the tools and store them into this list
        # could use list comprehension to keep the syntax prettier but IDK how to do that with sql
        # alchemy and I got no time to spend researching that
        _tools = []
        for tool in session.query(Tools):
            if tool.availability:
                _tools.append(tool)
            else:
                pass

        for tool in _tools:
            self.treeview.insert('', 'end', text=tool.id,
                                 values=(tool.name, tool.description, tool.daily_price + " GBP",
                                         tool.half_day_price + " GBP", tool.delivery_cost + " GBP"))
