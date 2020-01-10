import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END

from app.models import session
from app.models.tools import Tools


class CreateTool(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        self.FONT = 'Helvetica'
        self.TITLE_SIZE = 24

        # create a new frame
        tk.Frame.__init__(self, root)

        self.root = root
        self.CURRENT_USER = kwargs['user_id']

        label = Label(self, text="Create new tool", font=(self.FONT, self.TITLE_SIZE)).grid(row =0, column=0)

        # Labels
        self.name_label = Label(self, text="Name", font=(self.FONT, 12))
        self.description_label = Label(self, text="Description", font=(self.FONT, 12))
        self.daily_price_label = Label(self, text="Daily price", font=(self.FONT, 12))
        self.half_day_price_label = Label(self, text="Half day price", font=(self.FONT, 12))
        self.delivery_price_label = Label(self, text="Delivery price", font=(self.FONT, 12))

        self.name_label.grid(row=1, column=0)
        self.description_label.grid(row=2, column=0)
        self.daily_price_label.grid(row=3, column=0)
        self.half_day_price_label.grid(row=4, column=0)
        self.delivery_price_label.grid(row=5, column=0)

        # Inputs
        self.name_input = Entry(self, font=(self.FONT, 12))
        self.description_input = tk.Text(self, height=10, width=20, font=(self.FONT, 12))
        self.daily_price_input = Entry(self, font=(self.FONT, 12))
        self.half_day_price_input = Entry(self, font=(self.FONT, 12))
        self.delivery_price_input = Entry(self, font=(self.FONT, 12))

        self.name_input.grid(row=1, column=1)
        self.description_input.grid(row=2, column=1)
        self.daily_price_input.grid(row=3, column=1)
        self.half_day_price_input.grid(row=4, column=1)
        self.delivery_price_input.grid(row=5, column=1)

        self.create_tool_button = Button(self, text="Create tool", command= self.create_tool).grid(row=6, column=0)

        self.error_label = Label(self, text="", fg="red")
        self.error_label.grid(row=6, column=1)

    def create_tool(self):
        # validate the data
        validators = True

        all_inputs = [
            self.name_input.get(),
            self.description_input.get('1.0', END),
            self.daily_price_input.get(),
            self.half_day_price_input.get(),
            self.delivery_price_input.get()
        ]

        for field in all_inputs:
            if field == "":
                self.error_label.config(text="Please fill all fields")
                validators = False

        if validators:
            new_tool = Tools()
            new_tool.name = self.name_input.get()
            new_tool.description = self.description_input.get('1.0', END)
            new_tool.daily_price = self.daily_price_input.get()
            new_tool.half_day_price = self.half_day_price_input.get()
            new_tool.delivery_cost = self.delivery_price_input.get()
            new_tool.owner_id = self.CURRENT_USER
            new_tool.availability = True

            session.add(new_tool)
            session.commit()

            self.error_label.config(text="New tool successfully added", fg="green")