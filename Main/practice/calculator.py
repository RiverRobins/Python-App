from tkinter import *

prev = []
op = ""


def clear():
    prev.clear()
    entry.delete(0, END)


def up():
    prev.append(entry.get())
    entry.delete(0, END)


def number(n):
    entry.insert(END, n)


def add():
    up()
    global op
    op = "add"


def sub():
    up()
    global op
    op = "sub"


def mult():
    up()
    global op
    op = "mult"


def div():
    up()
    global op
    op = "div"


def do():
    global op
    up()
    if op == "add":
        entry.insert(END, str(int(prev[0]) + int(prev[1])))
    elif op == "sub":
        entry.insert(END, str(int(prev[0]) - int(prev[1])))
    elif op == "div":
        entry.insert(END, str(int(prev[0]) / int(prev[1])))
    elif op == "mult":
        entry.insert(END, str(int(prev[0]) * int(prev[1])))
    else:
        entry.insert(END, "No operator selected")
        clear()


root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

numbers = []
numbers.append(Button(root, text="1", padx=40, pady=20, command=lambda: number("1")))
numbers.append(Button(root, text="2", padx=40, pady=20, command=lambda: number("2")))
numbers.append(Button(root, text="3", padx=40, pady=20, command=lambda: number("3")))
numbers.append(Button(root, text="4", padx=40, pady=20, command=lambda: number("4")))
numbers.append(Button(root, text="5", padx=40, pady=20, command=lambda: number("5")))
numbers.append(Button(root, text="6", padx=40, pady=20, command=lambda: number("6")))
numbers.append(Button(root, text="7", padx=40, pady=20, command=lambda: number("7")))
numbers.append(Button(root, text="8", padx=40, pady=20, command=lambda: number("8")))
numbers.append(Button(root, text="9", padx=40, pady=20, command=lambda: number("9")))
numbers.append(Button(root, text="0", padx=40, pady=20, command=lambda: number("0")))

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

addition = Button(root, text="+", padx=40, pady=20, command=lambda: add())
subtraction = Button(root, text="-", padx=40, pady=20, command=lambda: sub())
multi = Button(root, text="*", padx=40, pady=20, command=lambda: mult())
divi = Button(root, text="/", padx=40, pady=20, command=lambda: div())

addition.grid(row=7, column=0)
subtraction.grid(row=7, column=1)
multi.grid(row=7, column=2)
divi.grid(row=8, column=0)


clear = Button(root, text="clear", padx=30, pady=20, command=clear)
enter = Button(root, text="enter", padx=29, pady=20, command=do)

clear.grid(row=6, column=2)
enter.grid(row=6, column=0)

root.mainloop()
