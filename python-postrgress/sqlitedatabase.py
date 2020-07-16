import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(connection):
   connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
   connection.commit()

def add_entry(connection, content, date):
    connection.execute("INSERT INTO entries VALUES (?, ?);", (content, date))
    connection.commit()

def get_entries(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM entries;")
    entries = []
    for row in cursor:
        entries.append(row)
    cursor.close()
    return entries


