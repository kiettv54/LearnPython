import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ABTT-20190809TW\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('''
                INSERT INTO TestDB.dbo.Person (Name, Age, City)
                VALUES
                ('Bob',55,'Montreal'),
                ('Jenny',66,'Boston')
                ''')
conn.commit()
cursor.execute('SELECT * FROM Person')
for row in cursor:
	print(row)

