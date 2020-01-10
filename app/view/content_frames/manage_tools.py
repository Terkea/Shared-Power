import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from app.models import session
from app.models.tools import Tools
from app.view.content_frames.create_tool import CreateTool


class ManageTools(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # create a new frame
        tk.Frame.__init__(self, root)

        # grab the user with the specified id to query for his tools
        self.CURRENT_USER = kwargs['user_id']

        label = Label(self, text="View Tools", font=(self.FONT, self.TITLE_SIZE)).pack(side='top')

        self.createTable()
        self.loadTable()

    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
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
        # get the user tools and store them into this list
        # could use list comprehension to keep the syntax prettier but IDK how to do that with sql
        # alchemy and I got no time to spend researching that
        _user_tools = []
        for tool in session.query(Tools).filter(Tools.owner_id == self.CURRENT_USER):
            _user_tools.append(tool)

        for tool in _user_tools:
            self.treeview.insert('', 'end', text=tool.id,
                                 values=(tool.name,
                                 tool.description, tool.daily_price + " GBP", tool.half_day_price + " GBP"))
