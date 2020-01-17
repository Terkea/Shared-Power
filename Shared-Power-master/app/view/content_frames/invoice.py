import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from tkinter.ttk import Treeview
from datetime import date, timedelta, datetime

from app.models import session
from app.models.booking import Booking
from app.models.returns import Returns
from app.models.tools import Tools
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

        beginning_date = (date.today().replace(day=1) - timedelta(days=1)).replace(day=1)

        for _returns in session.query(Returns).filter(Returns.return_date <= beginning_date.strftime('%Y-%m-%d')):
            invoice = []
            _booking = session.query(Booking).filter(Booking.id == Returns.booking_id).first()
            _tool = session.query(Tools).filter(Tools.id == Booking.tool_id).first()
            _owner = session.query(Users).filter(Users.id == Tools.owner_id).first()
            invoice.append(_tool.name)
            invoice.append(_booking.user_id)
            invoice.append(_owner.id)

            cost = _booking.duration_of_booking*2*_tool.half_day_price
            if _returns.date > _booking.booked_date + timedelta(days=float(_booking.duration_of_booking)):
                late_days = _returns.date - (_booking.booked_date + timedelta(days=float(_booking.duration_of_booking)))
                late_fees = _tool.daily_price*late_days.days
                cost += late_fees
            invoice.append(cost)
            _user_invoices.append(invoice)

        for invoice in _user_invoices:
            self.treeview.insert('', 'end', values=(invoice[0], invoice[1],
                                                    invoice[2], invoice[3] + " GBP"))
