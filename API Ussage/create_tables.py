import pyodbc
import 

# Connection parameters
driver = 'ODBC Driver 17 for SQL Server'
server = 'localhost,1433' 
database = 'AdventureWorksDW2017' 
username = 'sa'
password = 'eKwr2715' 


def create_database():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = cnxn.cursor()
    
    # create sparkify database with UTF8 encoding
    cursor.execute("IF OBJECT_ID('dbo.Sales', 'U') IS NULL \
    CREATE TABLE [dbo].[Sales](\
    [Region] [varchar](50) ,\
    [Country] [varchar](50) ,\
    [ItemType] [varchar](50) NULL,\
    [SalesChannel] [varchar](50) NULL,\
    [OrderPriority] [varchar](50) NULL,\
    [OrderDate]  datetime,\
    [OrderID] bigint NULL,\
    [ShipDate] datetime,\
    [UnitsSold]  float,\
    [UnitPrice] float,\
    [UnitCost] float,\
    [TotalRevenue] float,\
    [TotalCost]  float,\
    [TotalProfit] float\
    )")
    cnxn.commit()

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn

def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()