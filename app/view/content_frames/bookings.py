import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta


from app.models import session
from app.models.booking import Booking
from app.models.returns import Returns
from app.models.tools import Tools
from app.models.users import Users


class Bookings(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # this is for testing purposes only
        # grab the user with the specified id to query for his bookings
        self.CURRENT_USER = session.query(Users).filter_by(id=kwargs['user_id']).first()

        # create a new frame
        tk.Frame.__init__(self, root)


        self.title_label = Label(self, text="Bookings", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.pack(side='top')

        self.return_button = Button(self, text="Return tool", command=self.return_tool_frame)
        self.return_button.pack(anchor='w')

        self.report_button = Button(self, text="Report tool")
        self.report_button.pack(anchor='w')

        self.createTable()
        self.loadTable()

    def return_tool_frame(self):
        # grab the booking id to use it later
        self.booking_id = self.treeview.item(self.treeview.selection(), "text")

        # first of all we have to destroy all widgets within the frame
        self.title_label.destroy()
        self.return_button.destroy()
        self.report_button.destroy()
        self.treeview.destroy()

        # repopulate the window with the appropiate widgets
        self.title_label = Label(self, text="Return tool", font=(self.FONT, self.TITLE_SIZE))
        self.title_label.pack(side='top')

        self.subtitle = Label(self, text="Please write a few words to describe the tool condition")
        self.subtitle.pack()
        
        self.feedback = tk.Text(self, height=10, width=20, font=(self.FONT, 12))
        self.feedback.pack(fill=tk.BOTH)
        
        self.return_tool_button = Button(self, command=self.return_tool, text="Return tool")
        self.return_tool_button.pack()

        self.error_label = Label(self, text="")
        self.error_label.pack()

    def return_tool(self):
        if not self.feedback.get('1.0', END) == "":
            self.error_label.config(text="Please fill all fields")
        return_tool = Returns(returned=True, booking_id=self.booking_id, tool_condition=self.feedback.get('1.0', END))

        session.add(return_tool)
        session.commit()

        self.error_label.config(text="Item returned successfully")

    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('tool_name', 'booked_date', 'return_date', 'cost', 'delivery')

        tv.heading("#0", text='ID', anchor='w')
        tv.column("#0", anchor="w", width=10)

        tv.heading('tool_name', text='Tool name')
        tv.column('tool_name', anchor='center', width=100)

        tv.heading('booked_date', text='Booked date')
        tv.column('booked_date', anchor='center', width=100)

        tv.heading('return_date', text='Due return date')
        tv.column('return_date', anchor='center', width=100)

        tv.heading('cost', text='Cost')
        tv.column('cost', anchor='center', width=100)

        tv.heading('delivery', text='Delivery')
        tv.column('delivery', anchor='center', width=100)

        tv.pack(fill=tk.BOTH, expand=1)
        self.treeview = tv


    def loadTable(self):
        _user_bookings = []
        # could use list comprehension to keep the syntax prettier but IDK how to do that with sql
        # alchemy and I got no time to spend researching that
        user_bookings = session.query(Booking).filter(Booking.user_id == self.CURRENT_USER.id)

        # join the tables
        for book in user_bookings:
            tool = session.query(Tools).filter_by(id=book.tool_id).first()

            data = {
                "id": book.id,
                "booked_date": book.booked_date,
                "duration_of_booking": book.duration_of_booking,
                "tool_id": book.tool_id,
                "user_id": book.user_id,
                "delivery": book.delivery,
                "tool_name": tool.name,
                "tool_daily_price": tool.daily_price,
                "tool_half_day_price": tool.half_day_price,
            }

            # if the customer books a tool for x days + half day we write in in db as x.5
            # here we calculate the price
            if '.' in book.duration_of_booking:
                data['cost'] = (int(book.duration_of_booking[:book.duration_of_booking.find('.')]) *
                                float(tool.daily_price)
                                + float(tool.half_day_price))
            else:
                data['cost'] = (int(book.duration_of_booking) * float(tool.daily_price))

            try:
                return_date = session.query(Returns).filter_by(booking_id=book.id).first()
                if return_date.returned == True:
                    data['return_date'] = "Returned"
            except:
                data['return_date'] = datetime.strptime(book.booked_date, '%Y-%m-%d') +\
                                      timedelta(round(float(book.duration_of_booking)))

            if book.delivery == True:
                data['cost'] += float(tool.delivery_cost)


            _user_bookings.append(data)

        for booking in _user_bookings:
            self.treeview.insert('', 'end', text=booking['id'],
                                 values=(booking['tool_name'],
                                 booking['booked_date'], booking['return_date'], booking['cost'], booking['delivery']))
