import sqlite3

conn = sqlite3.connect('StudentDetails.db')

cur = conn.cursor()

# Create a table and assign one of the field as the primary key
cur.execute('''CREATE TABLE Details (StdCode INTEGER PRIMARY KEY,
                                    StdName TEXT,
                                    _class TEXT,
                                    Age INTEGER,
                                    Gender TEXT)''')

print('Table Details Successfully created.')
conn.commit()

cur.close()
conn.close()





