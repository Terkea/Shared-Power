import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class View_Profile(tk.Frame):

    def __init__(self, root):
        # create a new frame
        tk.Frame.__init__(self, root, background= 'green')
        welcome_label = Label(self, text='Hello, User')
        welcome_label.grid(column=0, row=0)