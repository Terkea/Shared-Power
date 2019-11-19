from tkinter import Frame, Label, Entry, Button


class Login:
    # constructor method
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.email_label = Label(frame, text="Email").grid(row=0, column=0)
        self.password_label = Label(frame, text="Password").grid(row=1, column=0)

        self.email = Entry(frame).grid(row=0, column=1)
        self.password = Entry(frame).grid(row=1, column=1)

        self.login_button = Button(frame, text="Login", command=self.redirect_app).grid(row=2, column=0)
        self.register_button = Button(frame, text="Create account", command=self.redirect_register).grid(row=2,
                                                                                                         column=1)

    def redirect_app(self):
        print("app")

    def redirect_register(self):
        print("register")