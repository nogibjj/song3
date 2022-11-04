import sqlite3 as sql

# check sqlite version
print("sqlite3.version : ", sql.version)
print("sqlite3.sqlite-version : ", sql.sqlite_version)

# set up connection to the database
conn = sql.connect("test.db")
cur = conn.cursor()

# create table
table = cur.execute(
    """ CREATE TABLE employee(
    id INT PRIMARY KEY,
    name CHAR(25),
    salary CHAR(25),
    joining_date DATE
);
"""
)

# insert data
cur.execute(
    "INSERT INTO employee (id, name, salary, joining_date) VALUES (1001, 'David', 50000, '1-08-2019')"
)
cur.execute(
    "INSERT INTO employee (id, name, salary, joining_date) VALUES (1002, 'Sally', 80000, '3-09-2020')"
)
cur.execute(
    "INSERT INTO employee (id, name, salary, joining_date) VALUES (1003, 'Lucy', 90000, '8-08-2020')"
)
cur.execute(
    "INSERT INTO employee (id, name, salary, joining_date) VALUES (1004, 'Chris', 100000, '9-09-2020')"
)
cur.execute(
    "INSERT INTO employee (id, name, salary, joining_date) VALUES (1005, 'Bob', 111000, '10-05-2019')"
)

# query the table
cur.execute("SELECT * FROM employee ORDER BY name")
table = cur.fetchall()
print("\n [+] Querying the data \n")

for i in table:
    print(i)
print("\n [+] Successfully connected to the database")

conn.commit()
