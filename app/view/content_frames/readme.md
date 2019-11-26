## Description
This folder contains all the content frames which will be displayed on the right side of the main frame

To make it easier for everybody to work on the project I split them into standalone classes to avoid any inconveniences

To create a new frame just follow this template

```python3
class Tools(tk.Frame):

    def __init__(self, root):
        # create a new frame
        tk.Frame.__init__(self, root, background= 'orange')
        welcome_label = Label(self, text='Tools')
        welcome_label.grid(column=0, row=0)
```

To bind the new frame with a method you'll need a swap method like the one we're using in app.switch_frame
```python3
    def switch_frame(self, frame):
        if self.content_frame is not frame:
            self.content_frame.grid_forget()
            self.content_frame = frame
            self.content_frame.grid(column=1, row=0, sticky='nswe')
```

To trigger this on events I used 
```python3
command=lambda: self.switch_frame(Tools(self))
```