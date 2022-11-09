import sqlite3 as sql

# set up connection to the database
conn = sql.connect("baseball.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM pitching WHERE playerID == 'ryuhy01'")
rows = cur.fetchall()
for row in rows:
    print(row)
