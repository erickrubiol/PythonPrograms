# How to load flat files to a Pandas Dataframe 

import pandas as pd:

column_names = ['Col1', 'Col2', 'Col3']

# Load 1000 rows and some columns of the data to dataframe 
data = pd.read_csv("file.tsv", usecols = column_names, nrows=1000,sep="\t")

# Process a file in chunks
column_names = ['Name', 'Adress', 'Zipcode']
data_chunk = pd.read_csv('file.csv',
                        nrows = 5000,
                        skiprows= 1000,
                        header = None,
                        names= column_names)


# Handling errors and missing data
