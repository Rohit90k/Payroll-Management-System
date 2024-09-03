import sqlite3
import hashlib
db = sqlite3.connect('SQLite_Python.db')
cursor = db.cursor()
# To Create Table

# cursor.execute("""
# CREATE TABLE Employees (
#     user_id   INTEGER    PRIMARY KEY
#                          UNIQUE
#                          NOT NULL,
#     user_name TEXT (100) NOT NULL
# );
# """)

# To Insert Data
#cursor.execute(" INSERT INTO  Employees VALUES ('3', 'Rajesh Dayaghan Sawant')")

# To Read Data
cursor.execute("UPDATE Employees WHERE 'user id' ='3' ")
s = cursor.fetchall()
print(s)

db.commit()
db.close()

data = [('Aditya Rajesh Sawant',)]
u = str(data[0][0])
print(u)