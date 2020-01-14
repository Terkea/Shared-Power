import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import uuid

from app.models import session
from app.models.tools import Tools
from app.view.app import App
from app.view.gui_engine import app


class ManageTools(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # create a new frame
        tk.Frame.__init__(self, root)

        # grab the user with the specified id to query for his tools
        self.CURRENT_USER = kwargs['user_id']

        title_label = Label(self, text="View Tools", font=(self.FONT, self.TITLE_SIZE)).pack(side='top')
        create_button = Button(self, text="Create Tool", command=lambda: self.getToolDetails("new"))
        edit_button = Button(self, text="Edit Tool", command=lambda: self.getToolDetails("edit"))
        delete_button = Button(self, text="Delete Tool", command=self.confirmDelete).pack(anchor='w')
        back_button = Button(self, text="Back", command=App.go_back).pack(anchor='w')

        self.createTable()
        self.loadTable()

    def removeTool(self):
        id = self.treeview.item(self.treeview.selection(), "text")

        session.delete(session.query(Tools).filter_by(id=id).first())
        session.commit()

        self.treeview.delete(*self.treeview.get_children())
        self.loadTable()

    def confirmDelete(self):
        confirm_window = Tk()
        confirm_label = Label(confirm_window, text="Are you sure you want\nto delete this tool?")
        yes_button = Button(confirm_window, text="Yes", command=self.removeTool)
        no_button = Button(confirm_window, text="No", command=lambda: confirm_window.destroy())

        confirm_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        no_button.grid(row=2, column=1, padx=10, pady=10)
        yes_button.grid(row=2, column=2, padx=10, pady=10)
        confirm_window.mainloop()

    def createTool(self, entry_list):
        newTool= Tools(id=uuid.uuid4().hex,
                       name=entry_list[0],
                       description=entry_list[1].get(),
                       daily_price=entry_list[2].get(),
                       half_day_price=entry_list[3].get(),
                       delivery_cost=entry_list[4].get(),
                       owner_id=self.CURRENT_USER)
        session.add(newTool)
        session.commit()

    def updateTool(self, entry_list):
        tool_id = self.treeview.item(self.treeview.selection(), "text")
        tool = session.query(Tools).filter(id == tool_id).first()
        tool.name = entry_list[0].get()
        tool.description = entry_list[1].get()
        tool.daily_price = entry_list[2].get()
        tool.half_day_price = entry_list[3].get()
        tool.delivery_cost = entry_list[4].get()
        session.commit()

    def getToolDetails(self, newORedit):
        def submit(newORedit):
            if newORedit == "new":
                self.createTool(entry_list)
            else:
                self.updateTool(entry_list)

        new_tool_window = Tk()
        entry_list = []
        back_button = Button(new_tool_window= Tk(), text="Back", command=lambda: app.switch_frame(ManageTools(app, "user")))
        submit_button = Button(new_tool_window= Tk(), text="Submit", command=lambda: submit(newORedit))
        back_button.grid(row=1, column=1, padx=10, pady=5)
        submit_button.grid(row=2, column=1, padx=10, pady=5)

        name_label = Label(new_tool_window, text="Tool Name:").grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="s"+"w")
        name_entry = Entry(new_tool_window).grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="n"+"w")
        entry_list.append(name_entry)

        description_label = Label(new_tool_window, text="Tool Description:").grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="s"+"w")
        description_entry = Entry(new_tool_window).grid(row=6, column=1, columnspan=2, padx=10, pady=10, sticky="n"+"w")
        entry_list.append(description_entry)

        daily_price_label = Label(new_tool_window, text="Day Hire Price:").grid(row=3, column=3, columnspan=2, padx=10, pady=10, sticky="s"+"e")
        daily_price_entry = Entry(new_tool_window).grid(row=4, column=3, columnspan=2, padx=10, pady=10, sticky="n"+"e")
        entry_list.append(daily_price_entry)

        half_day_price_label = Label(new_tool_window, text="Half Day Price:").grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="s"+"e")
        half_day_price_entry = Entry(new_tool_window).grid(row=6, column=3, columnspan=2, padx=10, pady=10, sticky="n"+"e")
        entry_list.append(half_day_price_entry)

        delivery_cost_label = Label(new_tool_window, text="Delivery Cost:").grid(row=7, column=1, columnspan=2, padx=10, pady=10, sticky="s"+"e")
        delivery_cost_entry = Entry(new_tool_window).grid(row=8, column=3, columnspan=2, padx=10, pady=10, sticky="n"+"e")
        entry_list.append(delivery_cost_entry)

        new_tool_window.mainloop()


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
            self.treeview.insert('', 'end', text=tool.id, values=(tool.name, tool.description, tool.daily_price +
                                                                  " GBP", tool.half_day_price + " GBP"))
