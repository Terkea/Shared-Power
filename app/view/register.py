import tkinter as tk
from tkinter import Frame, Label, Entry, Button


class Register(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # window size
        root.geometry('600x400')

        tk.Label(self, text="Register page").pack(side="top", fill="x", pady=5)
        # idk why but for some reason if you import this at the top of the file it will crash
        # I spent like 2 hours trying to fix this, so better don't touch it!!!
        from app.view.login import Login
        tk.Button(self, text="Go back to login page",
                  command=lambda: root.switch_frame(Login)).pack()
