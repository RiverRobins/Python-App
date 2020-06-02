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
    first = Entry(root)
    last = Entry(root)
    age = Entry(root)
    sex = Entry(root)


mainbar = Label(root).pack()

create = Label(mainbar).pack()
createText = Label(create, text="Add").pack()



root.mainloop()
