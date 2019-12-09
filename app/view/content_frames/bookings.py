import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class Bookings(tk.Frame):


    def __init__(self, root):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # create a new frame
        tk.Frame.__init__(self, root)
        label = Label(self, text="Bookings", font=(self.FONT, self.TITLE_SIZE)).pack(side='top')
        return_button = Button(self, text="Return tool").pack(anchor='w')
        report_button = Button(self, text="Report tool").pack(anchor='e')
        self.createTable()
        self.loadTable()



    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('return_date', 'cost', 'delivery')

        tv.heading("#0", text='Booked date', anchor='w')
        tv.column("#0", anchor="w")

        tv.heading('return_date', text='Due return date')
        tv.column('return_date', anchor='center', width=100)

        tv.heading('cost', text='Cost')
        tv.column('cost', anchor='center', width=100)

        tv.heading('delivery', text='Delivery/Collection')
        tv.column('delivery', anchor='center', width=100)

        tv.pack(fill=BOTH, expand=1)
        self.treeview = tv


    def loadTable(self):
        for i in range(100):
            self.treeview.insert('', 'end', text=f"Date {i}", values=('Return', 'cost', 'yes'))
