import sqlite3

# set up connection to the database
conn = sqlite3.connect("sample.db")
cur = conn.cursor()

# create table
table = cur.execute(""" CREATE TABLE employee(
    id INT PRIMARY KEY,
    name CHAR(25),
    salary CHAR(25),
    joining_date DATE
);
""")
print("\n [+] The table has been created Successfully ")

# insert data
cur.execute("INSERT INTO employee (id, name, salary, joining_date) VALUES (1001, 'David', 50000, '1-08-2019')")
cur.execute("INSERT INTO employee (id, name, salary, joining_date) VALUES (1002, 'Sally', 80000, '3-09-2020')")
cur.execute("INSERT INTO employee (id, name, salary, joining_date) VALUES (1003, 'Lucy', 90000, '8-08-2020')")
cur.execute("INSERT INTO employee (id, name, salary, joining_date) VALUES (1004, 'Chris', 100000, '9-09-2020')")
cur.execute("INSERT INTO employee (id, name, salary, joining_date) VALUES (1005, 'Bob', 111000, '10-05-2019')")
print("\n [+] The Data has been inserted Successfully ")

# query the table
cur.execute("SELECT id,name FROM employee")
table = cur.fetchall()
for i in table:
    print(i)
print("\n [+] Successfully connected to the database")