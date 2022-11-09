import sqlite3 as sql

# set up connection to the database
conn = sql.connect("baseball.sqlite")
cur = conn.cursor()
def test():
    cur.execute("SELECT * FROM pitching WHERE playerID == 'ryuhy01'")
    rows = cur.fetchall()
    assert rows[0][0] == 42453
