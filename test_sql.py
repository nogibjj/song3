import sqlite3 as sql

# set up connection to the database
conn = sql.connect("test.db")
cur = conn.cursor()
