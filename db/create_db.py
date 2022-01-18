import sqlite3

DB_PATH = '/home/aliapin/Downloads/github/bt_info/btc.db'

def getDbConnect():
    connect = sqlite3.connect(DB_PATH)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    
    return connect, cursor

connection, cursor = getDbConnect()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS balances (
        orig_addr PRIMARY KEY,
        orig_addr_sha256 TEXT NOT NULL UNIQUE,
        priv_key_hex TEXT NOT NULL UNIQUE,
        priv_key_wif TEXT NOT NULL UNIQUE,
        priv_key_wif_compr TEXT NOT NULL UNIQUE, 
        pub_key TEXT NOT NULL UNIQUE, 
        pub_key_compr TEXT NOT NULL UNIQUE,
        pub_addr TEXT NOT NULL UNIQUE,   
        pub_addr_compr TEXT NOT NULL UNIQUE,   
        pub_addr_3 TEXT NOT NULL UNIQUE,  
        pub_addr_bc1_p2wpkh TEXT NOT NULL,    
        pub_addr_bc1_p2wsh TEXT NOT NULL)     
""")

connection.commit()
connection.close()