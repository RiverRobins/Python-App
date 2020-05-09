from tkinter import *

prev = []

root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def number(n):
    prev.append(n)

numbers = []
i = 1
while i < 10:
    numbers.append(Button(root, text=str(i), padx=40, pady=20, command=lambda: number(i)))
    i += 1
numbers.append(Button(root, text="", padx=40, pady=20, command=lambda: number(0)))

numbers[0].grid(row=3, column=0)
numbers[1].grid(row=3, column=1)
numbers[2].grid(row=3, column=2)
numbers[3].grid(row=4, column=0)
numbers[4].grid(row=4, column=1)
numbers[5].grid(row=4, column=2)
numbers[6].grid(row=5, column=0)
numbers[7].grid(row=5, column=1)
numbers[8].grid(row=5, column=2)
numbers[9].grid(row=6, column=1)

root.mainloop()
