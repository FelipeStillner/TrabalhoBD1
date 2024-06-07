import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
sql_file = open("create.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)
sql_file = open("insert.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)
