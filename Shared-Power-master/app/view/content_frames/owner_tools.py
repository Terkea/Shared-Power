import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import uuid
from sqlalchemy import exc

from app.models import session
from app.models.tools import Tools


class OwnerTools(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # create a new frame
        tk.Frame.__init__(self, root)

        # grab the user with the specified id to query for his tools
        self.CURRENT_USER = kwargs['user_id']

        label = Label(self, text="View Tools", font=(self.FONT, self.TITLE_SIZE)).pack(side='top')
        expand_button = Button(self, text="Expand Tool", command=self.expandTool).pack(anchor='w')
        create_button = Button(self, text="Add Tool", command=lambda: self.getToolDetails("new", False)).pack(anchor='w')
        remove_button = Button(self, text="Remove Tool", command=self.confirmDelete).pack(anchor='w')
        edit_button = Button(self, text="Edit Tool", command=lambda: self.getToolDetails("edit", False)).pack(anchor='w')

        self.createTable()
        self.loadTable()

    def expandTool(self):
        def edit():
            expand_window.destroy()
            self.getToolDetails("edit",False)

        tool_id = self.treeview.item(self.treeview.selection(), "text")
        tool = session.query(Tools).filter_by(id=tool_id).first()


        expand_window = Tk()
        expand_window.geometry("250x300")

        back_button = Button(expand_window, text="Back", command=lambda: expand_window.destroy())
        back_button.grid(row=1, column=1, padx=10, pady=5, sticky="E")
        edit_button = Button(expand_window, text="Edit", command=edit)
        edit_button.grid(row=2, column=1, padx=10, pady=5, sticky="E")

        name_title = Label(expand_window, text="Tool Name:").grid(row=3, column=1, padx=5, pady=5, sticky="E")
        name_value = Label(expand_window, text=tool.name).grid(row=3, column=2, padx=5, pady=5, sticky="W")

        description_title = Label(expand_window, text="Tool Description:").grid(row=4, column=1, padx=5, pady=5, sticky="N")
        description_value = Message(expand_window, text=tool.description, width=75).grid(row=4, column=2, padx=5, pady=5, sticky="W")

        daily_price_title = Label(expand_window, text="Day Hire Price:").grid(row=5, column=1, padx=5, pady=5, sticky="E")
        daily_price_value = Label(expand_window, text=tool.daily_price).grid(row=5, column=2, padx=5, pady=5, sticky="W")

        half_price_title = Label(expand_window, text="Half Day Hire Price:").grid(row=6, column=1, padx=5, pady=5, sticky="E")
        half_price_value = Label(expand_window, text=tool.half_day_price).grid(row=6, column=2, padx=5, pady=5, sticky="W")

        delivery_cost_title = Label(expand_window, text="Delivery Charge:").grid(row=7, column=1, padx=5, pady=5, sticky="E")
        delivery_cost_value = Label(expand_window, text=tool.delivery_cost).grid(row=7, column=2, padx=5, pady=5, sticky="W")

        expand_window.mainloop()

    def createTool(self, tool_details):
        try:
            newTool= Tools(id=uuid.uuid4().hex,
                           name=tool_details[0],
                           description=tool_details[1],
                           daily_price=tool_details[2],
                           half_day_price=tool_details[3],
                           delivery_cost=tool_details[4],
                           availability=True,
                           owner_id=self.CURRENT_USER)
            session.add(newTool)
            session.commit()
            self.loadTable()
        except exc.IntegrityError:
            self.getToolDetails("new", True)

    def removeTool(self, confirm_window):
        id = self.treeview.item(self.treeview.selection(), "text")

        session.delete(session.query(Tools).filter_by(id=id).first())
        session.commit()
        confirm_window.destroy()

        self.treeview.delete(*self.treeview.get_children())
        self.loadTable()

    def updateTool(self, tool_details):
        tool_id = self.treeview.item(self.treeview.selection(), "text")
        tool = session.query(Tools).filter_by(id=tool_id).first()
        tool.name = tool_details[0]
        tool.description = tool_details[1]
        tool.daily_price = tool_details[2]
        tool.half_day_price  = tool_details[3]
        tool.delivery_cost = tool_details[4]
        tool.availability = True
        session.commit()

        self.loadTable()

    def confirmDelete(self):
        id = self.treeview.item(self.treeview.selection(), "text")
        if id == "":
            pass
        else:
            confirm_window = Tk()
            confirm_label = Label(confirm_window, text="Are you sure you want\nto delete this tool?")
            yes_button = Button(confirm_window, text="Yes", command=lambda: self.removeTool(confirm_window))
            no_button = Button(confirm_window, text="No", command=lambda: confirm_window.destroy())

            confirm_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
            no_button.grid(row=2, column=1, padx=10, pady=10)
            yes_button.grid(row=2, column=2, padx=10, pady=10)
            confirm_window.mainloop()

    def getToolDetails(self, newORedit, error):
        new_tool_window = Tk()
        entry_list = []

        def submit():
            tool_details = []
            for entry in entry_list:
                if entry.get() == "":
                    new_tool_window.destroy()
                    self.getToolDetails(newORedit, True)
                else:
                    tool_details.append(entry.get())

            new_tool_window.destroy()
            if newORedit == "new":
                self.createTool(tool_details)
            else:
                self.updateTool(tool_details)


        submit_button = Button(new_tool_window, text="Submit", command=submit)
        submit_button.grid(row=1, column=1, padx=10, pady=5)
        error_label = Label(new_tool_window, text="Invalid details, try again")
        if error:
            error_label.grid(row=2, column=1, padx=10, pady=5)

        name_label = Label(new_tool_window, text="Tool Name:")\
            .grid(row=3, column=1, columnspan=2, padx=15, pady=5, sticky="s"+"w")
        name_entry = Entry(new_tool_window)
        entry_list.append(name_entry)
        name_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="n"+"w")

        description_label = Label(new_tool_window, text="Tool Description:")\
            .grid(row=5, column=1, columnspan=2, padx=15, pady=5, sticky="s"+"w")
        description_entry = Entry(new_tool_window)
        entry_list.append(description_entry)
        description_entry.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="n"+"w")

        daily_price_label = Label(new_tool_window, text="Day Hire Price:")\
            .grid(row=3, column=3, columnspan=2, padx=15, pady=5, sticky="s"+"w")
        daily_price_entry = Entry(new_tool_window)
        entry_list.append(daily_price_entry)
        daily_price_entry.grid(row=4, column=3, columnspan=2, padx=10, pady=5, sticky="n")

        half_day_price_label = Label(new_tool_window, text="Half Day Price:")\
            .grid(row=5, column=3, columnspan=2, padx=15, pady=5, sticky="s"+"w")
        half_day_price_entry = Entry(new_tool_window)
        entry_list.append(half_day_price_entry)
        half_day_price_entry.grid(row=6, column=3, columnspan=2, padx=10, pady=5, sticky="n")

        delivery_cost_label = Label(new_tool_window, text="Delivery Cost:")\
            .grid(row=7, column=3, columnspan=2, padx=15, pady=5, sticky="s"+"w")
        delivery_cost_entry = Entry(new_tool_window)
        entry_list.append(delivery_cost_entry)
        delivery_cost_entry.grid(row=8, column=3, columnspan=2, padx=10, pady=5, sticky="n")

        #availability_label = Label(new_tool_window, text="Is the tool\navailable to order?")\
        #   .grid(row=7, column=1, columnspan=2, padx=15, pady=5, sticky="s"+"w")
        #_availability = BooleanVar
        #available_yes = tk.Radiobutton(new_tool_window, text="Yes", value=1, variable=_availability)\
        #    .grid(row=8, column=1, padx=5, pady=5)
        #available_no = tk.Radiobutton(new_tool_window, text="No", value=2, variable=_availability)\
        #    .grid(row=8, column=2, padx=5, pady=5)
        #entry_list.append(_availability)

        new_tool_window.mainloop()
        self.loadTable()

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
        # get the user tools and store them into this list
        # could use list comprehension to keep the syntax prettier but IDK how to do that with sql
        # alchemy and I got no time to spend researching that
        _user_tools = []
        for tool in session.query(Tools).filter(Tools.owner_id == self.CURRENT_USER):
            _user_tools.append(tool)

        self.treeview.delete(*self.treeview.get_children())

        for tool in _user_tools:
            self.treeview.insert('', 'end', text=tool.id,
                                 values=(tool.name,
                                 tool.description, tool.daily_price + " GBP",
                                         tool.half_day_price + " GBP", tool.delivery_cost + " GBP"))
