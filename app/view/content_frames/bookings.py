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
        self.createTable()
        self.loadTable()



    def createTable(self):
        tv = Treeview(self)
        tv.pack(side='left')
        vsb = Scrollbar(self, orient="vertical", command=tv.yview)
        vsb.pack(side='right', fill='y')

        tv.configure(yscrollcommand=vsb.set)

        tv['columns'] = ('starttime', 'endtime', 'status')
        tv.heading("#0", text='Sources', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='Start Time')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='End Time')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='Status')
        tv.column('status', anchor='center', width=100)
        tv.pack(fill=BOTH, expand=1)
        self.treeview = tv


    def loadTable(self):
        for i in range(100):
            self.treeview.insert('', 'end', text=f"First {i}", values=('10:00',
                                                                  '10:10', 'Ok'))
