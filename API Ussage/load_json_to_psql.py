import psycopg2
import json

# connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test",
    user="postgres",
    password="password")

# create a cursor
cur = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')


# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)


# close the communication with the PostgreSQL
cur.close()



'''
file = 'd:\\OneDrive\\git\\Datasets\\distros.json'

f = open(file)

data = json.load(f)



# Delete a field from the data
for i in data:
    i.pop('Owner', None)
    print(i)


f.close()
'''




'''
@profile
def insert_execute_values_iterator(connection, beers: Iterator[Dict[str, Any]]) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)
        psycopg2.extras.execute_values(cursor, """
            INSERT INTO staging_beers VALUES %s;
        """, ((
            beer['id'],
            beer['name'],
            beer['tagline'],
            parse_first_brewed(beer['first_brewed']),
            beer['description'],
            beer['image_url'],
            beer['abv'],
            beer['ibu'],
            beer['target_fg'],
            beer['target_og'],
            beer['ebc'],
            beer['srm'],
            beer['ph'],
            beer['attenuation_level'],
            beer['brewers_tips'],
            beer['contributed_by'],
            beer['volume']['value'],
        ) for beer in beers))
'''