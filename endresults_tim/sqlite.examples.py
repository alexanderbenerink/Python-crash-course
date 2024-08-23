import sqlite3

# Create a connection to the database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        cur = conn.cursor()
        
        with open('create_table.sql', 'rb') as q_file:
            q = q_file.read().decode('utf-8')
            cur.execute(q)
        
        cur.execute("INSERT INTO rekeningen_TimBolhoeve (id, rekeninghouder, rekeningnummer, saldo) VALUES (1, 'Tim Bolhoeve', 'NL01RABO0123456789', 1000.00);")
        ex = cur.execute("SELECT * FROM rekeningen_TimBolhoeve;")
        print(ex.fetchall())        
        
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()
            print(f"Connection to {db_file} closed")
            
if __name__ == "__main__":
    create_connection("pythonsqlite.db")