import sqlite3
import datetime

now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite-version : ', sqlite3.sqlite_version)