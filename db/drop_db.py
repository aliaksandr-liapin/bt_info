import sqlite3

DB_PATH = '/home/aliapin/Downloads/github/bt_info/btc.db'

def getDbConnect():
    connect = sqlite3.connect(DB_PATH)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    
    return connect, cursor

connection, cursor = getDbConnect()
cursor.execute("DROP TABLE IF EXISTS balances")


connection.commit()
connection.close()