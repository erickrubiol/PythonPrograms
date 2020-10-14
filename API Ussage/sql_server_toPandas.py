import pandas as pd
import pyodbc 

server = 'localhost,1433' 
database = 'AdventureWorks' 
username = 'SA' 
password = 'eKwr_2715' 

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server+';DATABASE='+database+';UID='+username+';PWD=' + password)

sql = "SELECT * FROM DimGeography"
data = pd.read_sql(sql,cnxn)

print( data.head() )