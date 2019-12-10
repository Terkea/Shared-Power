import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class Welcome(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        # create a new frame
        tk.Frame.__init__(self, root, background= 'blue')
        welcome_label = Label(self, text='Welcome Page')
        welcome_label.grid(column=0, row=0)