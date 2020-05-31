import Creds as creds
import mysql.connector

db = mysql.connector.connect(host="localhost", user=creds.mySql_user, passwd=creds.mySql_password)
cur = db.cursor()

cur.execute("CREATE TABLE people (id BIG_INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR 255, last_name VARCHAR 255), age INTEGER, sex ENUM('M', 'F', 'N/A') DEFAULT('N/A')")

