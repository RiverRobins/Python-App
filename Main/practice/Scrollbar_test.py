from tkinter import *

root = Tk()

f = Frame(root)
f.pack()

scrollbar = Scrollbar(f)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(f, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END, "item " + str(line))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()
