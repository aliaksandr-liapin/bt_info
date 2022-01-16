import connect_db as connect

connection, cursor = connect.getDbConnect()
cursor.execute("DROP TABLE IF EXISTS balances")


connection.commit()