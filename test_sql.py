import sqlite3 as sql

# set up connection to the database
conn = sql.connect("test.db")
cur = conn.cursor()

# check sqlite version
print("sqlite3.version : ", sql.version)
print("sqlite3.sqlite-version : ", sql.sqlite_version)
