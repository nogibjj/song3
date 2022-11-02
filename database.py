import sqlite3 as sql
import string
import random

# create database
conn = sql.connect("database.db")

# query database
query = """CREATE TABLE IF NOT EXISTS test (
    col1 INTEGER PRIMARY KEY AUTOINCREMENT,
    col2 VARCHAR(200) NOT NULL,
    col3 TEXT default "")"""
cur = conn.cursor()
cur.execute(query)
conn.commit()

# add data to database
for i in range(1000):
    query = "INSERT INTO test (col2, col3) VALUES (?, ?)"
    rnd = "".join([random.choice(string.ascii_letters+string.digits) for i in range(10)])
    print(rnd)
    cur.execute(query, (i, rnd))

conn.commit()