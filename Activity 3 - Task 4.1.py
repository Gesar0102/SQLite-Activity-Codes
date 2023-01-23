import sqlite3

conn = sqlite3.connect('StockRegister.db')

cur = conn.cursor()

# Execute a selec statement to retrieve records with condition
cur.execute('SELECT * FROM Stocks where StockNo = 102')

#fetch all rows of data
rows = cur.fetchall()

# Iterate through the rows and print out the table
for row in rows:
    print(row)

cur.close()
conn.close()



