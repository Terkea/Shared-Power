import tkinter as tk

app = tk.Tk()

app.title("MUIE MA-ta")
app.geometry('1000x500')
app.resizable(False, False)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

menu_frame_users = tk.Frame(app, width=200, background='red')
menu_frame_users.grid_columnconfigure(0, minsize=150)
menu_frame_users.grid_rowconfigure(0, minsize=50)
menu_frame_users.grid_rowconfigure(1, minsize=40)
menu_frame_users.grid_rowconfigure(2, minsize=40)
menu_frame_users.grid_rowconfigure(3, minsize=40)
menu_frame_users.grid_rowconfigure(4, minsize=40)

content_frame = tk.Frame(app, width=800, background='blue')


hello_label = tk.Label(menu_frame_users, text='Hello, User').grid(column=0, row=0, sticky='nswe')
view_profile_button = tk.Button(menu_frame_users, text="View Profile").grid(column=0, row=1, sticky='nswe')
invoices_button = tk.Button(menu_frame_users, text="Invoices").grid(column=0, row=2, sticky='nswe')
bookings_button = tk.Button(menu_frame_users, text="View bookings").grid(column=0, row=3, sticky='nswe')
tools_button = tk.Button(menu_frame_users, text="Search tools").grid(column=0, row=4, sticky='nswe')

test_label = tk.Label(content_frame, text='View profile')
test_label.grid(column=0, row=0, sticky='nswe')

menu_frame_users.grid(column=0, row=0, sticky='nswe')
content_frame.grid(column=1, row=0, sticky='nswe')


app.mainloop()
