import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from tkcalendar import DateEntry

from app.models import session
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

        _tool = session.query(Tools).filter_by(id = self.tool_id).first()

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

        self.calendar = DateEntry(self, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2020)
        self.calendar.pack()

        self.calendar_label = Label(self, text="For how many days would you like to rent the tool?")
        self.calendar_label.pack()

        days = IntVar()
        self.period_of_time = Combobox(self, textvariable=days)
        self.period_of_time.pack()
        self.period_of_time["values"] = [1, 1.5, 2, 2.5, 3]
        
        self.validation_label = Label(self, text="")
        self.validation_label.pack()
        
        self.book_button = Button(self, command=self.book_tool, text="Add item to the basket")
        self.book_button.pack()

        



    def book_tool(self):
        self.tool_id = self.treeview.item(self.treeview.selection(), "text")

        order = Checkout()
        order.user_id = self.CURRENT_USER
        order.tool_id = self.tool_id

        self.error_label.config(text="Item added to your basket")

        print(self.CURRENT_USER, self.tool_id)



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