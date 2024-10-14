import sqlite3

#connect to sqlite
connection = sqlite3.connect("student.db")

#create an cursor object to insert record,create table
cursor = connection.cursor()

#create an table
table_info = """ 
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""
cursor.execute(table_info)

#insert some records
cursor.execute('''Insert Into STUDENT values('Krish','Machinelearning','A')''')
cursor.execute('''Insert Into STUDENT values('Sudharshan','Machinelearning','B')''')
cursor.execute('''Insert Into STUDENT values('Devika','Machinelearning','A')''')
cursor.execute('''Insert Into STUDENT values('Sanjay','DEVOPS','A')''')
cursor.execute('''Insert Into STUDENT values('Adam','DEVOPS','A')''')

#display all the records
print("the inserted records are:")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()    