

import sqlite3

conn = sqlite3.connect('StockRegister.db')

cur = conn.cursor()

#define list of data to be addedd 
items = [(101, 'Dell Laptop',30,40000),
         (102, 'MacBook Pro',10,120000),
         (102,'Dell Laptop',25, 55000),
         (104,'Acer Laptop',30, 40000)]

#define sql query to add the data into the table
query = 'INSERT INTO Stocks (StockNo, StockName, Quantity, PricePerItem) VALUES (?,?,?,?)'

#Execute the query multiple times with different parameter values
cur.executemany(query, items)

conn.commit()

print('Data successfully added to the table.')
cur.close()
conn.close()




