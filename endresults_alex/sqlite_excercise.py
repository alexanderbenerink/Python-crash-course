import sqlite3

def monolithFunctionHAHAHA():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS rekeningen
            (id SERIAL PRIMARY KEY, 
            rekeninghouder text NOT NULL,
            rekeningnummer text NOT NULL,
            saldo real)
        '''
    )
    cursor.execute("INSERT INTO rekeningen VALUES (1, 'Alexander', 'NL01 BANK 2345 6789 10', 0.69)")
    
    cursor.execute("SELECT * FROM rekeningen")

    print(cursor.fetchall())

    connection.commit()
    connection.close()

monolithFunctionHAHAHA()