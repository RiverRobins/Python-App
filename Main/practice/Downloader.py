from tkinter import *
from pytube import *

target = ""

root = Tk.tk()

u_input = Tk.Entry(root)
u_input.pack()
label = Tk.Label(u_input, text="Enter a URL here")
label.pack()



root.mainloop()
