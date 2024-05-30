import sqlite3

conn = sqlite3.connect('student.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     grade REAL
)
''')

cursor.execute('''
INSERT INTO students (name, grade)
VALUES ('Masha', 162.5), ('Misha', 180.9), ('Sasha', 192.4)
''')

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()