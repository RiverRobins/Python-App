from tkinter import *

root = Tk()


def hello():
    l = Label(root, text="Hello World!")
    l.pack()
    # b1.state = "disabled"


b1 = Button(root, command=hello, text="Button!")
b1.pack()


root.mainloop()
