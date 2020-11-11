import psycopg2
import psycopg2.extras
import json
from typing import Iterator, Optional
import io

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


# object that feeds off an iterator, and provides a file-like interface
class StringIteratorIO(io.TextIOBase):
    def __init__(self, iter: Iterator[str]):
        self._iter = iter
        self._buff = ''

    def readable(self) -> bool:
        return True

    def _read1(self, n: Optional[int] = None) -> str:
        while not self._buff:
            try:
                self._buff = next(self._iter)
            except StopIteration:
                break
        ret = self._buff[:n]
        self._buff = self._buff[len(ret):]
        return ret

    def read(self, n: Optional[int] = None) -> str:
        line = []
        if n is None or n < 0:
            while True:
                m = self._read1()
                if not m:
                    break
                line.append(m)
        else:
            while n > 0:
                m = self._read1(n)
                if not m:
                    break
                n -= len(m)
                line.append(m)
        return ''.join(line)


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


def clean_csv_value(value) -> str:
    if value is None:
        return r'\N'
    return str(value).replace('\n', '\\n')


# Copy data to psql
def copy_string_iterator(connection, data, size: int = 8192) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)
        obj_string_iterator = StringIteratorIO((
            '|'.join(map(clean_csv_value, (
                obj['Name'],
                obj['Version'],
                obj['Install'],
                obj['Kernel'],
                obj['Owner']
            ))) + '\n'
            for obj in data
        ))
        cursor.copy_from(obj_string_iterator, 'staging_distros', sep='|', size=size)


copy_string_iterator(connection, iter(data), size=1024)

# close the communication with the PostgreSQL
connection.close()
f.close()