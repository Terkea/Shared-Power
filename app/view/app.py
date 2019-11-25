import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class App(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # window size
        root.geometry('600x400')

        tk.Label(self, text="app page").pack(side="top", fill="x", pady=5)
