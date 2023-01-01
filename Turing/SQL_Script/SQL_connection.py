import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KHADIJA\SQLEXPRESS;'
                      'Database=ERP_DB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM tbl_employee')

for i in cursor:
    print(i)
