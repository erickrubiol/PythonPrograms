import pyodbc
import pandas as pd

# Connection parameters
driver = 'ODBC Driver 17 for SQL Server'
server = 'localhost,1433' 
database = 'AdventureWorksDW2017' 
username = 'sa'
password = 'eKwr2715' 


sql = "SELECT * FROM DimGeography"
data = pd.read_sql(sql,cnxn)


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
   [LoadDatetime] datetime\
)")
cnxn.commit()


#Bulk Insert to the new table
cursor.execute("BULK INSERT Sales \
FROM '/home/1500000_Sales_Records.csv' \
WITH (FIRSTROW = 2,\
      FIELDTERMINATOR = ',',\
      ROWTERMINATOR = '\n',\
      BATCHSIZE = 250000\
);")
cnxn.commit()


def process_file(cur, filepath):

    # open song file
    df = pd.read_json(filepath, lines=True)

    for value in df.values:
        artist_id, artist_latitude, artist_location, artist_longitude, artist_name, duration, num_songs, song_id, title, year = value

        # insert artist record
        artist_data = [artist_id, artist_name, artist_location, artist_longitude, artist_latitude]
        cur.execute(artist_table_insert, artist_data)

        # insert song record
        song_data = [song_id, title, artist_id, year, duration]
        cur.execute(song_table_insert, song_data)



def main():
    cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = cnxn.cursor()

    process_data(cur, cnxn, filepath='data/song_data', func=process_song_file)
    process_data(cur, cnxn, filepath='data/log_data', func=process_log_file)

    cnxn.close()


if __name__ == "__main__":
    main()