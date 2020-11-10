# import tkinter as Tk
# from tk import *
from tkinter import *
from tkinter import messagebox

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

from pytube import *

target = ""


def getTarget():
    global target
    target = u_input.get()

    if str.strip(target) == "":
        return

    yt = YouTube(target)

    print(StreamQuery.filter(only_audio=True, file_extension="mp4"))

    # if messagebox.askyesno("Confirm", text=f"URL for {yt.title} by {yt.author} was entered. Is this the right video"):
        # yt.streams.



root = Tk()

u_input = Entry(root)
u_input.pack()
label = Label(root, text="Enter a URL here:")
label.pack()

enter = Button(root, text="Enter", command=getTarget)
enter.pack()

root.bind("<Return>", getTarget)

root.mainloop()
