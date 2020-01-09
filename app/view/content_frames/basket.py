import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from app.models import session
from app.models.booking import Booking
from app.models.checkout import Checkout
from app.models.tools import Tools
from app.models.users import Users


class Basket(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # this is for testing purposes only
        # grab the user with the specified id to query for his bookings
        self.CURRENT_USER = session.query(Users).filter_by(id=kwargs['user_id']).first()

        # create a new frame
        tk.Frame.__init__(self, root)
        label = Label(self, text="Basket", font=(self.FONT, self.TITLE_SIZE)).pack(side='top')
        delete_button = Button(self, text="Delete item", command=self.delete_item).pack(anchor='w')
        confirm_button = Button(self, text="Confirm order", command=self.checkout_items).pack(anchor='w')
        self.createTable()
        self.loadTable()


    def checkout_items(self):
        print('hit')
        user_items = session.query(Checkout).filter(Checkout.user_id == self.CURRENT_USER.id)
        for item in user_items:
            new_booking = Booking(booked_date=item.booked_date, duration_of_booking=item.duration_of_booking,
                                  tool_id=item.tool_id, user_id=item.user_id, delivery=item.delivery)
            session.add(new_booking)

            session.delete(item)
            session.commit()

        self.treeview.delete(*self.treeview.get_children())
        self.loadTable()


    def delete_item(self):
        id = self.treeview.item(self.treeview.selection(), "text")

        session.delete(session.query(Checkout).filter_by(id=id).first())
        session.commit()

        self.treeview.delete(*self.treeview.get_children())
        self.loadTable()

    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('tool_name', 'duration_of_booking', 'cost', 'delivery')

        tv.heading("#0", text='ID', anchor='w')
        tv.column("#0", anchor="w", width=10)

        tv.heading('tool_name', text='Tool name')
        tv.column('tool_name', anchor='center', width=100)

        tv.heading('duration_of_booking', text='Duration of booking')
        tv.column('duration_of_booking', anchor='center', width=100)

        tv.heading('cost', text='Cost')
        tv.column('cost', anchor='center', width=100)

        tv.heading('delivery', text='Delivery')
        tv.column('delivery', anchor='center', width=100)

        tv.pack(fill=BOTH, expand=1)
        self.treeview = tv

    def loadTable(self):
        _user_items = []
        user_items = session.query(Checkout).filter(Checkout.user_id == self.CURRENT_USER.id)

        # join the tables
        for item in user_items:
            tool = session.query(Tools).filter_by(id=item.tool_id).first()

            data = {
                "id": item.id,
                "booked_date": item.booked_date,
                "duration_of_booking": item.duration_of_booking,
                "tool_id": item.tool_id,
                "user_id": item.user_id,
                "delivery": item.delivery,
                "tool_name": tool.name,
                "tool_daily_price": tool.daily_price,
                "tool_half_day_price": tool.half_day_price
            }

            if '.' in item.duration_of_booking:
                data['cost'] = (int(item.duration_of_booking[:item.duration_of_booking.find('.')]) *
                                float(tool.daily_price)
                                + float(tool.half_day_price))
            else:
                data['cost'] = (int(item.duration_of_booking) * float(tool.daily_price))

            if item.delivery == True:
                data['cost'] += float(tool.delivery_cost)


            _user_items.append(data)

        for item in _user_items:
            self.treeview.insert('', 'end', text=item['id'],
                                 values=(item['tool_name'],
                                 item['duration_of_booking'], item['cost'], item['delivery']))