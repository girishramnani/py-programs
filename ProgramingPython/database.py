import sqlite3
conn = sqlite3.connect('questions')
curs = conn.cursor()
tbl = 'create table people (name char(30),job char(10),pay int(4))'
curs.execute('insert into people VALUES (?,?,?)',('bob','dev',5000))
print(curs.rowcount)
# curs.execute(tbl)

