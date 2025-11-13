import sqlite3
conn=sqlite3.connect("mydatabase.db")
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS(
ID INTEGER PRIMARY KEY,
NAME TEXT(20),
AGE INTEGER)''')
data=[
    ('saro',21),
    ('meena',18),
    ('sarosi',23),
    ('balu',20)
]
cursor.executemany("INSERT INTO STUDENTS(NAME,AGE) VALUES(?,?)",data)
conn.commit()
cursor.execute("SELECT * FROM STUDENTS")
rows=cursor.fetchall()
for r in rows:
    print(r)
conn.close()