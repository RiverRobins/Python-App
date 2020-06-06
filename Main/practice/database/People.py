import Creds as creds
import mysql.connector
from tkinter import *

db = mysql.connector.connect(host="localhost", user=creds.mySql_user, passwd=creds.mySql_password, database="people")
cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS people")

cur.execute("CREATE TABLE IF NOT EXISTS customers ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255),"
            "dob DATE,"
            "sex ENUM('M', 'F', 'N/A') DEFAULT 'N/A',"
            "notes TEXT"
            "rep_id BIGINT UNSIGNED"
            "PRIMARY KEY (id),"
            "FOREIGN KEY (rep_id) REFERENCES representatives (id)"
            ");"
            "CREATE TABLE IF NOT EXISTS employees ("
            "id BIGINT UNSIGNED AUTO_INCREMENT"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255),"
            "dob DATE,"
            "sex ENUM('M', 'F', 'N/A') DEFAULT 'N/A',"
            "salary INT UNSIGNED"
            "notes TEXT,"
            "hire_date DATE,"
            "end_date DATE DEFAULT NULL"
            ");"
            "CREATE TABLE IF NOT EXISTS representatives("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "emp_id BIGINT UNSIGNED AUTO_INCREMENT,"
            "manager_id BIGINT UNSIGNED AUTO_INCREMENT,"
            "specialty VARCHAR(255),"
            "PRIMARY KEY id,"
            "FOREIGN KEY emp_id REFERENCES employees (id),"
            "FOREIGN KEY manager_id REFERENCES managers (id)"
            ");"
            "CREATE TABLE IF NOT EXISTS specialties ("
            "id BIGINT UNSIGNED AUTO_INCREMENT,"
            "title VARCHAR(255),"
            "desc TEXT,"
            ");")

root = Tk()


class enter_new:
    # first = None
    # last = None
    # age = None
    # sex = None

    def __init__(self, n):
        self.first = Entry(n)
        self.last = Entry(n)
        self.age = Entry(n)
        self.sex = Entry(n)
        self.first.pack()
        self.last.pack()
        self.age.pack()
        self.sex.pack()

    def clear(self):
        self.first.delete(0, -1)
        self.last.delete(0, -1)
        self.age.delete(0, -1)
        self.sex.delete(0, -1)


def add():
    global addLabel
    cur.execute("INSERT INTO customers(first_name, last_name, age, sex) VALUES ('%s', '%s', %s, '%s');" % (addLabel.first.get(), addLabel.last.get(), addLabel.age.get(), addLabel.sex.get()))
    db.commit()
    addLabel.clear()


mainbar = Label(root).pack()

create = Label(mainbar).pack()
createText = Label(create, text="Add").pack()
addLabel = enter_new(create)
add_button = Button(create, text="Submit", command=add).pack()

show = Label(root).pack()

results = []


def format_customer(n):
    return


def showall():
    cur.execute("SELECT * FROM customers")
    for i in cur.fetchall():
        results.append(Label(show, text=format_customer(i)).pack())


show_button = Button(root, text="Refresh", command=showall).pack()

showall()

root.mainloop()
db.close()
