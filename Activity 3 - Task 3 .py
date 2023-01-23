import sqlite3

conn = sqlite3.connect('StockRegister.db')

cur = conn.cursor()

# Execute a selec statement to retrieve all records from the table
cur.execute('SELECT * FROM Stocks')

#fetch all rows of data
rows = cur.fetchall()

# Iterate through the rows and print out the table
for row in rows:
    print(row)

cur.close()
conn.close()




