import sqlite3

#connect to the database
conn = sqlite3.connect('StockRegister.db')

#Create a cursor object
cur = conn.cursor()

#create the table and the fields
cur.execute('''CREATE TABLE Stocks (StockNo INTEGER,
                                    StockName TEXT,
                                    Quantity INTEGER,
                                    PricePerItem INTEGER)''')

print('Table Stocks Successfully created.')
conn.commit()

cur.close()
conn.close()


