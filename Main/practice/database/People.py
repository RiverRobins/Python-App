import Creds as creds
import mysql.connector
# from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import datetime

from database.Tabs import Customer
from database.Tabs.Customer import Customers


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

# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer1", "last", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer2", "last", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer3", "aerg", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer4", "grtege", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer5", "name", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer6", "ronaldwashingtonrosthchild", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer7", "gertrude", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer8", "chad", "1992-08-21", "N/A", "Insert notes here", "2"))
# cur.execute("INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % ("customer9", "AntiCom", "1992-08-21", "N/A", "Insert notes here", "2"))


cw = None

def closeTab(n):
    if messagebox.askokcancel("Quit", "Do you want to exit" + n + " ?"):
        cw.destroy()

def openEmployees():
    global cw
    cw = tk.Toplevel(root)
    cw.geometry("300x300")
    cw.title("Customers")

    enter_new = tk.Frame(cw, bg="#aaaa22")
    enter_new.pack()

    first = tk.Frame(enter_new)
    first.pack()
    first_l = tk.Label(first, text="Enter first name: ")
    first_l.pack()
    first_e = tk.Entry(first)
    first_e.pack()

    last = tk.Frame(enter_new)
    last.pack()
    last_l = tk.Label(last, text="Enter last name: ")
    last_l.pack()
    last_e = tk.Entry(last)
    last_e.pack()

    dob = tk.Frame(enter_new)
    dob.pack()
    dob_l = tk.Label(dob, text="Enter date of birth: ")
    dob_l.pack()
    dob_e = tk.Entry(dob)
    dob_e.pack()

    sex = tk.Frame(enter_new)
    sex.pack()
    sex_l = tk.Label(sex, text="Enter date sex(M, F, or N/A): ")
    sex_l.pack()
    sex_e = tk.Entry(sex)
    sex_e.pack()

    notes = tk.Frame(enter_new)
    notes.pack()
    notes_l = tk.Label(notes, text="Notes: ")
    notes_l.pack()
    notes_e = tk.Text(notes, height=4)
    notes_e.pack()

    rep = tk.Frame(enter_new)
    rep.pack()
    # rep_l = tk.Label(rep, text="Select a representative")
    # rep_l.pack()

    # cur.execute("SELECT representatives.id AS rep_id, employees.first_name, employees.last_name FROM employees JOIN representatives ON employees.id = representatives.emp_id;")
    # reps = cur.fetchall()
    #
    # rep_var = tk.StringVar(cw)
    # rep_var.set(reps[0])
    #
    # rep_selected = reps[0][0]
    # locals()

    # def setRep(n):
    #     locals()
    #     temp = str.split("(#")
    #     rep_selected = temp[-1][0:-2]

    # rep_m = tk.OptionMenu(rep, rep_var, reps)
    # rep_m.pack()

    # submit = tk.Button(enter_new, text="Sumbit", command=new_cust)
    # submit.pack()

    results = []
    scrollbar = tk.Scrollbar(cust_res_con)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    customers = tk.Listbox(root, yscrollcommand=scrollbar.set)
    customers.pack(side=tk.LEFT, fill=tk.BOTH)
    cur.execute("SELECT * FROM employees")
    for i in cur.fetchall():
        temp = tk.Label(customers, text=str(results.append(i)))
        temp.pack()

    scrollbar.config(command=customers.yview)

    def exit():
        global cw
        db.commit()
        cw = None

    cw.lift()
    cw.protocol("WM_DELETE_WINDOW", exit())


root = tk.Tk()
theme = Theme()

cust_button = tk.Button(root, text="Customers", command=Customers.openCustomers).pack()
emp_button = tk.Button(root, text="Employees", command=openEmployees()).pack()

root.mainloop()
db.close()
