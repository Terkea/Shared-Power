import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from tkinter.ttk import Treeview

from app.models import session
from app.models.invoices import Invoices
from app.models.users import Users


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

        tv['columns'] = ('month', 'description', 'amount')

        tv.heading("#0", text='ID', anchor='w')
        tv.column("#0", anchor="w", width=10)

        tv.heading('month', text='Month')
        tv.column('month', anchor='center', width=100)

        tv.heading('description', text='Description')
        tv.column('description', anchor='center', width=100)

        tv.heading('amount', text='Amount')
        tv.column('amount', anchor='center', width=100)

        tv.pack(fill=tk.BOTH, expand=1)
        self.treeview = tv

    def loadTable(self):
        _user_invoices = []
        for invoice in session.query(Invoices).filter(Invoices.user_id == self.CURRENT_USER):
            _user_invoices.append(invoice)

        for invoice in _user_invoices:
            self.treeview.insert('', 'end', text=invoice.id,
                                 values=(invoice.month,
                                 invoice.description, invoice.amount + " GBP"))