import Creds as creds
import mysql.connector
# from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import datetime


class Theme:
    text = "#000000"
    background = "FFFFFF"


db = mysql.connector.connect(host="localhost", user=creds.mySql_user, passwd=creds.mySql_password, database="people")
cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS people;")

cur.execute(
            "CREATE TABLE IF NOT EXISTS employees ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255),"
            "dob DATE,"
            "sex ENUM('M', 'F', 'N/A') DEFAULT 'N/A',"
            "salary INT UNSIGNED,"
            "notes TEXT,"
            "hire_date DATE,"
            "end_date DATE DEFAULT NULL,"
            "PRIMARY KEY (id)"
            ");")
cur.execute(
            "CREATE TABLE IF NOT EXISTS specialties ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "title VARCHAR(255),"
            "description TEXT,"
            "PRIMARY KEY (id)"
            ");")
cur.execute(
            "CREATE TABLE IF NOT EXISTS managers ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "emp_id BIGINT UNSIGNED,"
            "specialty_id BIGINT UNSIGNED,"
            "PRIMARY KEY (id),"
            "FOREIGN KEY (emp_id) REFERENCES employees(id) ON DELETE SET NULL,"
            "FOREIGN KEY (specialty_id) REFERENCES specialties(id) ON DELETE SET NULL"
            ");")
cur.execute(
            "CREATE TABLE IF NOT EXISTS representatives("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "emp_id BIGINT UNSIGNED,"
            "manager_id BIGINT UNSIGNED,"
            "specialty_id BIGINT UNSIGNED,"
            "PRIMARY KEY (id),"
            "FOREIGN KEY (emp_id)"
            "   REFERENCES employees(id) ON DELETE SET NULL,"
            "FOREIGN KEY (manager_id)"
            "   REFERENCES managers(id) ON DELETE SET NULL,"
            "FOREIGN KEY (specialty_id) REFERENCES specialties(id) ON DELETE SET NULL"
            ");")
cur.execute("CREATE TABLE IF NOT EXISTS customers ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255),"
            "dob DATE,"
            "sex ENUM('M', 'F', 'N/A') DEFAULT 'N/A',"
            "notes TEXT,"
            "rep_id BIGINT UNSIGNED,"
            "PRIMARY KEY (id),"
            "FOREIGN KEY (rep_id) REFERENCES representatives (id) ON DELETE SET NULL"
            ");")
cur.execute(
            "CREATE TABLE IF NOT EXISTS cases ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "title VARCHAR(255),"
            "issue TEXT,"
            "outcome TEXT,"
            "customer_id BIGINT UNSIGNED,"
            "rep_id BIGINT UNSIGNED,"
            "PRIMARY KEY (id),"
            "FOREIGN KEY (rep_id) REFERENCES representatives(id) ON DELETE SET NULL,"
            "FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL"
            ");")

cw = None
def openCustomers():
    global cw
    cw = tk.Toplevel(root) #root, bg="#aaaa00"
    cw.title("Customers")

    enter_new = tk.Frame(cw).pack()

    test = tk.Label(cw, text="NEW WINDOW TEXT").pack()
    test_f = tk.Frame(cw).pack()
    butt = tk.Button(cw, text="test button").pack()

    first = tk.Frame(enter_new).pack()
    first_l = tk.Label(first, text="Enter first name: ").pack()
    first_e = tk.Entry(first).pack()

    last = tk.Frame(enter_new).pack()
    last_l = tk.Label(last, text="Enter last name: ").pack()
    last_e = tk.Entry(last).pack()

    dob = tk.Frame(enter_new).pack()
    dob_l = tk.Label(dob, text="Enter date of birth: ").pack()
    dob_e = tk.Entry(last).pack()

    results = []
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    customers = tk.Listbox(root, yscrollcommand=scrollbar.set)
    cur.execute("SELECT * FROM CUSTOMERS")
    for i in cur.fetchall():
        tk.Label(cw, text=str(results.append(i)))

    customers.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=customers.yview)

    cw.lift()


root = tk.Tk()
theme = Theme()

# cur.execute("INSERT INTO employees(first_name, last_name, dob, sex, salary, notes, hire_date) VALUES"
#             "('The', 'Founder', '2000-05-25', 'N/A', 1, 'The Founder', '2000-05-25'),"
#             "('Co', 'Founder', '2000-10-04', 'M', 1, 'The Co Founder', '1991-09-21')")
# db.commit()
# cur.execute("INSERT INTO specialties(title, description) VALUES ('Test', 'A dummy specialty that is practically useless')")
# db.commit()
# cur.execute("INSERT INTO managers(emp_id, specialty_id) VALUES (1, 1)")
# db.commit()
# cur.execute("INSERT INTO representatives(emp_id, manager_id, specialty_id) VALUES (2, 1, 1)")
# db.commit()

# "id BIGINT UNSIGNED AUTO_INCREMENT,"
#             "emp_id BIGINT UNSIGNED,"
#             "manager_id BIGINT UNSIGNED,"
#             "specialty_id BIGINT UNSIGNED,"

# class enter_new:
#
#     def __init__(self, n):
#         self.label_first = Label(n, text="Enter first name: ", fg=theme.text).pack()
#         self.first = Entry(n)
#         self.first.pack()
#         self.label_last = Label(n, text="Enter last name: ", fg=theme.text).pack()
#         self.last = Entry(n)
#         self.last.pack()
#         self.label_dob = Label(n, text="Enter date of birth: ", fg=theme.text).pack()
#         self.dob = Entry(n)
#         self.dob.pack()
#         self.label_sex = Label(n, text="Enter sex: ", fg=theme.text).pack()
#         self.sex = Entry(n)
#         self.sex.pack()
#
#
#
#     def clear(self):
#         self.first.delete(0, -1)
#         self.last.delete(0, -1)
#         self.dob.delete(0, -1)
#         self.sex.delete(0, -1)
#
#     def getDate(self):
#         while True:  # 44-44-44
#             if len(self.dob.get()) <= 8:
#                 return datetime.datetime.strptime(self.dob.get(), "%m-%d-%y")
#             elif len(self.dob.get()) >= 9:
#                 return datetime.datetime.strptime(self.dob.get(), "%m-%d-%Y")
#             else:
#                 messagebox.showwarning("Error processing date", "Please enter date format in MM/DD/YY or MM/DD/YYYY")
#
#
#
# def add():
#     global addLabel
#     cur.execute("INSERT INTO customers(first_name, last_name, dob, sex) VALUES ('%s', '%s', %s, '%s');" % (addLabel.first.get(), addLabel.last.get(), addLabel.getDate(), addLabel.sex.get()))
#     db.commit()
#     addLabel.clear()


cust_button = tk.Button(root, text="Customers", command=openCustomers).pack()
# openCustomers()


# def createNewWindow():
#     newWindow = tkinter.Toplevel(root)
#     newWindow.title("New")
#     labelExample = tkinter.Label(newWindow, text = "New Window")
#     buttonExample = tkinter.Button(newWindow, text = "New Window button")
#
#     labelExample.pack()
#     buttonExample.pack()
#
# buttonExample = tkinter.Button(root,
#               text="Create new window",
#               command=createNewWindow)
# buttonExample.pack()


root.mainloop()
db.close()
