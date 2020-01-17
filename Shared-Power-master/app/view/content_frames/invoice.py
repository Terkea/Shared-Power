import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from tkinter.ttk import Treeview
from datetime import date, timedelta

from app.models import session
from app.models.returns import Returns
from app.models.booking import Booking


class Invoice(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        self.CURRENT_USER = kwargs['user_id']

        # create a new frame
        tk.Frame.__init__(self, root)

        self.title_label = Label(self, text="Invoices", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.pack(side='top')

        self.createTable()
        self.loadTable()

    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = tk.Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('tool_name', 'customer_id', 'owner_id', 'total_cost')

        tv.heading('tool_name', text='Tool Name')
        tv.column('tool_name', anchor='center', width=100)

        tv.heading('customer_id', text='Customer ID')
        tv.column('customer_id', anchor='center', width=100)

        tv.heading('owner_id', text='Owner ID')
        tv.column('owner_id', anchor='center', width=100)

        tv.heading('total_cost', text='Total Cost')
        tv.column('total_cost', anchor='center', width=50)

        tv.pack(fill=tk.BOTH, expand=1)
        self.treeview = tv

    def loadTable(self):
        _user_invoices = []
        beginning_date = date.today().replace(day=1) - timedelta(month=1)


        _returns = session.query(Returns).filter(date <= beginning_date)

        if '.' in book.duration_of_booking:
            data['cost'] = (int(book.duration_of_booking[:book.duration_of_booking.find('.')]) *
                            float(tool.daily_price)
                            + float(tool.half_day_price))
        else:
            data['cost'] = (int(book.duration_of_booking) * float(tool.daily_price))




        for invoice in _user_invoices:
            self.treeview.insert('', 'end', values=(invoice['tool_name'], invoice['customer_id'],
                                                    invoice['owner_id'], invoice['total_cost'] + " GBP"))