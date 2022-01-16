import connect_db

connection, cursor = connect_db.getDbConnect()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS balances (
        orig_addr TEXT PRIMARY KEY,
        orig_addr_sha256 TEXT NOT NULL UNIQUE,
        priv_key_hex TEXT NOT NULL UNIQUE,
        priv_key_wif TEXT NOT NULL UNIQUE,
        priv_key_wif_compr TEXT NOT NULL UNIQUE, 
        pub_key TEXT NOT NULL UNIQUE, 
        pub_key_compr TEXT NOT NULL UNIQUE,
        pub_addr TEXT NOT NULL UNIQUE,   
        pub_addr_compr TEXT NOT NULL UNIQUE,   
        pub_addr_3 TEXT NOT NULL UNIQUE,  
        pub_addr_bc1_p2wpkh TEXT NOT NULL UNIQUE,    
        pub_addr_bc1_p2wsh TEXT NOT NULL UNIQUE)     
""")

connection.commit()