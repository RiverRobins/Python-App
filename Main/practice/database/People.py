import Creds as creds
import mysql.connector
from tkinter import *

db = mysql.connector.connect(host="localhost", user=creds.mySql_user, passwd=creds.mySql_password)
cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS people")

db.config(database="people")

cur.execute("CREATE TABLE IF NOT EXISTS customers ("
            "id BIGINT AUTO_INCREMENT PRIMARY KEY,"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255),"
            "age INT,"
            "sex ENUM('M', 'F', 'N/A') DEFAULT 'N/A');")

root = Tk()


class enter_new:
    first = None
    last = None
    age = None
    sex = None

    def __init__(self, n):
        self.first = Entry(n)
        self.last = Entry(n)
        self.age = Entry(n)
        self.sex = Entry(n)


mainbar = Label(root).pack()

create = Label(mainbar).pack()
createText = Label(create, text="Add").pack()
add = enter_new(create)


root.mainloop()
