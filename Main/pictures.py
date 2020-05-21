from tkinter import *
import os

from PIL import ImageTk, Image

imgPath = os.getcwd() + "/imgs/"

root = Tk()

currentImg = 0

c = Canvas(root)
c.pack()
scroll = Scrollbar(c, orient="vertical", command=c.yview)
scroll.pack(side=RIGHT, fill=BOTH)

c.config(yscrollcommand=scroll.set)

images = []

for n in os.listdir("imgs"):
    if n == ".DS_Store":
        continue
    images.append(ImageTk.PhotoImage(Image.open(imgPath + n).resize((500, 500))))

mainpic = Label(c, image=images[0])
mainpic.pack()

buttons = Label(c)
buttons.pack()


def change_img(n):
    return


back = Button(buttons, text="<", command=lambda: change_img(-1))
forword = Button(buttons, text=">", command=lambda: change_img(1))

back.grid(row=3, column=0)
forword.grid(row=3, column=1)

root.mainloop()
