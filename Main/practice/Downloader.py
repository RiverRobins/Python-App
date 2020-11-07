# import tkinter as Tk
# from tk import *
from tkinter import *
from tkinter import messagebox

from pytube import *

target = ""


def getTarget():
    global target
    target = u_input.get()

    messagebox.showinfo(text=f"{target} was entered.")


root = Tk()

u_input = Entry(root)
u_input.pack()
label = Label(u_input, text="Enter a URL here")
label.pack()

enter = Button(root, text="Enter", command=getTarget)
enter.pack()

root.bind("<Return>", getTarget)

root.mainloop()
