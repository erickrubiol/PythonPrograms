import pandas as pd
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

driver = 'ODBC Driver 17 for SQL Server'
server = 'localhost,1433' 
database = 'AdventureWorksDW2017' 
username = 'sa'
password = 'eKwr2715' 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost,1433;DATABASE=AdventureWorks;UID=SA;PWD=eKwr_2715')
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM DimGeography")
for row in cursor.fetchall():
    print(row)