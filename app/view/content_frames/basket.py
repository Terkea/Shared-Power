import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class Basket(tk.Frame):

    def __init__(self, root):
        # create a new frame
        tk.Frame.__init__(self, root, background= 'red')
        welcome_label = Label(self, text='Basket')
        welcome_label.grid(column=0, row=0)