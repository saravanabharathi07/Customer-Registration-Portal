import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sarosi007",
    database="studentdb"
)
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS(
ID INT AUTO_INCREMENT PRIMARY KEY,
NAME VARCHAR(30),
AGE INT)''')

cursor.execute("INSERT INTO STUDENTS(NAME,AGE) VALUES(%s,%s)",("SARO",22))

conn.commit()
cursor.execute("SELECT * FROM STUDENTS")
for row in cursor.fetchall():
    print(row)
conn.close()
cursor.close()
