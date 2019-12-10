import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class Tools(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        # create a new frame
        tk.Frame.__init__(self, root, background= 'orange')
        welcome_label = Label(self, text='Tools')
        welcome_label.grid(column=0, row=0)