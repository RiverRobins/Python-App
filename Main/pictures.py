from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()

images = []

for n in os.listdir("imgs"):
    if n != ".DS_Store":
        try:
            images.append(ImageTk.PhotoImage(Image.open(n)))
        finally:
            print("file: " + n + " can't be opened.")

l = Label(image=images[0])
l.pack()

root.mainloop()
