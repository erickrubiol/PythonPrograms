import psycopg2
import psycopg2.extras
import json

# connect to the PostgreSQL server
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test",
    user="postgres",
    password="password")

# Every command will take effect immediately
connection.autocommit = True


# Load JSON data
file = 'd:\\OneDrive\\git\\Datasets\\distros.json'
f = open(file)
data = json.load(f)


# Create table
def create_staging_table(cursor) -> None:
    cursor.execute("""
        DROP TABLE IF EXISTS staging_distros;
        CREATE UNLOGGED TABLE staging_distros (
            name                TEXT,
            version             TEXT,
            install             TEXT,
            kernel              DECIMAL,
            owner               TEXT
        );
    """)


# to reduce memory consumption we try to avoid storing data 
# in-memory by using an iterator instead of a list
def insert_execute_values_iterator(
    connection,
    distros,
    page_size: int = 100,
) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)
        psycopg2.extras.execute_values(cursor, """
            INSERT INTO staging_distros VALUES %s;
        """, ((
            distro['Name'],
            distro['Version'],
            distro['Install'],
            distro['Kernel'],
            distro['Owner']
        ) for distro in distros), page_size=page_size)


insert_execute_values_iterator(connection, iter(data), page_size=1000)

# close the communication with the PostgreSQL
connection.close()
f.close()