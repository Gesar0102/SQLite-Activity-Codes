import sqlite3

conn = sqlite3.connect('StudentDetails.db')
cur = conn.cursor()

# Define query to Delete a record
query = 'DELETE FROM Details where StdCode = 1002'

# Execute the query
cur.execute(query)

conn.commit()
print('Record deleted Successfully')

cur.execute('SELECT * FROM Details')
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()


