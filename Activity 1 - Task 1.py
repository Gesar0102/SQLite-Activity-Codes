import sqlite3

#Create or connect to the database
conn = sqlite3.connect('EmployeeDetails.db')

#Create a cursor object
cur = conn.cursor()

#Create the table
cur.execute('''CREATE TABLE Details (Emp_ID INTEGER PRIMARY KEY,
                                    Emp_Name STRING,
                                    Age INTEGER,
                                    Gender STRING,
                                    SALARY INTEGER)''')

#Define the list of data to be added
employees = [(101, 'Karma Dorji', 39, 'Male', 42000),
             (102, 'Sonam Wangmo', 42, 'Female', 54000),
             (103, 'Tshering Lhamo', 30, 'Female', 30000),
             (104, 'Karma Dorji', 39, 'Male', 43000),
             (105, 'Purna Rai', 23, 'Male', 32000)]

#Define SQL Query
query = 'INSERT INTO Details (Emp_ID, Emp_Name, Age, Gender, Salary) VALUES (?,?,?,?,?)'

#Execute the query multiple times with different parameter values
cur.executemany(query,employees)

#Commit the transaction
conn.commit()

#SELECT Query to retrieve all the adta from the table
cur.execute('SELECT * FROM Details')

#fetch all the rows in the table
rs = cur.fetchall()

#iterate through the rows and print the data
for r in rs:
    print(r)

#close the cursor and connection    
cur.close()
conn.close()





