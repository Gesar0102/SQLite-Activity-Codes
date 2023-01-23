import sqlite3

conn = sqlite3.connect('StudentDetails.db')

cur = conn.cursor()

# Execute the UPDATE statement
cur.execute("UPDATE Details SET StdName='Thinley Lhamo' WHERE StdCode=1003")

# Save the changes
conn.commit()

print('Data value updated successfully')

cur.execute('SELECT * FROM Details')

rows = cur.fetchall()

for row in rows:
    print(row)
    
cur.close()
conn.close()





