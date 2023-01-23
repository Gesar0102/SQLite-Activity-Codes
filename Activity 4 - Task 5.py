import sqlite3

conn = sqlite3.connect('StudentDetails.db')

cur = conn.cursor()

#Dropping Stocks table 
cur.execute("DROP TABLE Details")

conn.commit()

print("Table dropped successfully ")

cur.close()
conn.close()





