import sqlite3

conn = sqlite3.connect('StudentDetails.db')

cur = conn.cursor()

items = [(1001, 'Sonam Dorji', 'X A', 16, 'Male'),
         (1002, 'Karma Choden', 'VI B', 12, 'Female'),
         (1003, 'Thinley Wangmo', 'VIII A', 14,'Female'),
         (1004, 'Sonam Tshering','II C', 8, 'Male')]

query = 'INSERT INTO Details (StdCode, StdName, _class, Age, Gender) VALUES (?,?,?,?,?)'

cur.executemany(query,items)

conn.commit()

cur.execute('SELECT * FROM Details')

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()





