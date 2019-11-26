import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class Invoices(tk.Frame):

    def __init__(self, root):
        # create a new frame
        tk.Frame.__init__(self, root, background= 'red')
        welcome_label = Label(self, text='Invoices')
        welcome_label.grid(column=0, row=0)