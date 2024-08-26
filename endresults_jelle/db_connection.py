import sqlite3

def connect() -> sqlite3.Cursor:
    conn = sqlite3.connect("test.db")
    print('Connected to database: test.db')

    return conn.cursor()

def close(cur: sqlite3.Cursor) -> None:
    cur.close()
    print('Database connection closed')

def create_table(cur: sqlite3.Cursor) -> None:
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS rekeningen
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  rekeninghouder text NOT NULL,
                  rekeningnummer text NOT NULL,
                  saldo real)'''
    )

def insert_records(cur: sqlite3.Cursor, table: str) -> None:
    cur.execute(f"""INSERT INTO {table}(rekeninghouder, rekeningnummer, saldo) VALUES (
            'J.W. Groothuysen', 'NL00 RABO 0123 1212 12', 999),
            ('G. BLUTH', 'AM00 RABO 0123 1212 12', 0),
            ('S. FISHER', 'NSA00 RABO 0123 1212 12', 15000)
        """)

    res = cur.execute(f'SELECT * FROM {table}')
    records = res.fetchall()
    print(records)


if __name__=="__main__":
    # Create the database and get a connection
    cursor = connect()
    
    # Create the table with rows 
    create_table(cur=cursor)

    # Insert new records
    insert_records(cur=cursor, table='rekeningen')

    # Close database connection
    close(cur=cursor)


