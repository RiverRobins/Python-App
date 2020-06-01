import Creds as creds
import mysql
import mysql.connector

db = mysql.connector.connect(host="localhost", user=creds.mySql_user, passwd=creds.mySql_password, database="people")
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers ("
            "id BIGINT AUTO_INCREMENT PRIMARY KEY,"
            "first_name VARCHAR(255),"
            "last_name VARCHAR(255),"
            "age INT,"
            "sex ENUM('M', 'F', 'N/A') DEFAULT 'N/A');")

