from tkinter import *
import os

from PIL import ImageTk, Image

imgPath = os.getcwd() + "/imgs/"

root = Tk()
c = Canvas(root)
c.pack()
scroll = Scrollbar(c, orient="vertical", command=c.yview)
scroll.grid(column=1)

c.config(yscrollcommand=scroll.set)

images = []

for n in os.listdir("imgs"):
    if n == ".DS_Store":
        continue
    # try:
    images.append(ImageTk.PhotoImage(Image.open(imgPath + n)))
    # finally:
    #     print("file: " + n + " can't be opened.")

mainpic = Label(c, image=images[0])
mainpic.grid(row=0, column=0, columnspan=2)

back = Button(c, text="<")
forword = Button(c, text=">")

back.grid(row=3, column=0)
forword.grid(row=3, column=1)

root.mainloop()
