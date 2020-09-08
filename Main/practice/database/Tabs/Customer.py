from database.People import cur
from database.People import root
from database.People import db

import Creds as creds
import mysql.connector
# from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import datetime


class Customers:
    # def __init__(self):

    def searchCustomers(self, n=False):
        if not n:
            cur.execute("SELECT * FROM customers")
            res = cur.fetchall()
            print("Results: ================================")
            for i in range(len(res)):
                print(res[i])
            print("=========================================")
            return res
            # return cur.fetchall()

        cur.execute(
            "SELECT * FROM customers WHERE first_name LIKE '%{}%' OR last_name LIKE '%{}%' OR id LIKE '%{}% OR notes LIKE '%{}%".format(
                n, n, n, n))
        global results
        results = cur.fetchall()
        # for i in range(len(res)):
        #     print(res[i])
        return cur.fetchall()

    def openCustomers(self):
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
        sex_l = tk.Label(sex, text="Enter sex(M, F, or N/A): ")
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
        rep_l = tk.Label(rep, text="Select a representative")
        rep_l.pack()

        cur.execute(
            "SELECT representatives.id AS rep_id, employees.first_name, employees.last_name FROM employees JOIN representatives ON employees.id = representatives.emp_id;")
        reps = cur.fetchall()

        rep_var = tk.StringVar(cw)
        rep_var.set(reps[0])

        rep_selected = reps[0][0]
        locals()

        def setRep(n):
            locals()
            temp = str.split("(#")
            rep_selected = temp[-1][0:-2]

        rep_m = tk.OptionMenu(rep, rep_var, reps)
        rep_m.pack()

        def new_cust():
            errs = []
            try:
                locals()
                if str.strip(first_e.get()) == "":
                    errs.append("First Name")
                if str.strip(last_e.get()) == "":
                    errs.append("Last Name")
                if str.strip(dob_e.get()) == "":
                    errs.append("Date of Birth")
                if str.strip(sex_e.get()) == "" or str.strip(sex_e.get()) is None:
                    errs.append("Sex")
                elif str.strip(sex_e.get()) != "M" or str.strip(sex_e.get()) != "F" or str.strip(sex_e.get()) != "N/A":
                    errs.append("Valid Sex(M, F, or N/A) '" + str.strip(sex_e.get()) + "' is not valid sex")
                if len(errs) == 0:
                    cur.execute(
                        "INSERT INTO customers(first_name, last_name, dob, sex, notes, rep_id) VALUES ('%s', '%s', %s, '%s', %s, %s);" % (
                            first_e.get(), last_e.get(), dob_e, sex_e.get(), notes_e.get("1.0", tk.END),
                            str(rep_selected)))
                    db.commit()
            except:
                print("errs amount: " + str(len(errs)))
                print(errs)
                messagebox.showwarning("Error processing date", "Please enter date format in YY-MM-DD or YYYY-MM-DD")
            if len(errs) > 0:
                err_str = ""
                i = 0
                while i < len(errs):
                    err_str += errs[i]
                    if len(errs) > 2 and i < len(errs) - 1:
                        err_str += ", "
                    else:
                        err_str += " "
                    if i == len(errs) - 2 and len(errs) >= 1:
                        err_str += "and "
                    i += 1
                messagebox.showwarning("Error processing values", "Please enter values for " + err_str)
            first_e.delete(0, 'end')
            last_e.delete(0, 'end')
            dob_e.delete(0, 'end')
            sex_e.delete(0, 'end')
            notes_e.delete('1.0', tk.END)

        submit = tk.Button(enter_new, text="Sumbit", command=new_cust)
        submit.pack()

        cust_search = tk.Frame(cw)
        cust_search.pack()
        cust_search_l = tk.Label(cust_search, text="Search:")
        cust_search_l.pack()
        cust_search_e = tk.Entry(cust_search)
        cust_search_e.pack()
        cust_search_b = tk.Button(cust_search, text="Enter",
                                  command=lambda: self.searchCustomers(str.strip(cust_search_e.get())))
        cust_search_b.pack()

        cust_res_con = tk.Frame(cw)
        cust_res_con.pack()

        cust_search = tk.Frame(cw)
        cust_search.pack()
        cust_search_l = tk.Label(cust_search, text="Search:")
        cust_search_l.pack()
        cust_search_e = tk.Entry(cust_search)
        cust_search_e.pack()
        cust_search_b = tk.Button(cust_search, text="Enter",
                                  command=lambda: self.searchCustomers(str.strip(cust_search_e.get())))
        cust_search_b.pack()

        cust_res_con = tk.Frame(cw)
        cust_res_con.pack()

        results = []
        scrollbar = tk.Scrollbar(cust_res_con)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        customers = tk.Listbox(root, yscrollcommand=scrollbar.set)
        customers.pack(side=tk.LEFT, fill=tk.BOTH)
        cur.execute("SELECT * FROM CUSTOMERS")
        for i in cur.fetchall():
            temp = tk.Label(customers, text=str(results.append(i)))
            temp.pack()

        scrollbar.config(command=customers.yview)

        cw.lift()
        cw.protocol("WM_DELETE_WINDOW", db.commit())


