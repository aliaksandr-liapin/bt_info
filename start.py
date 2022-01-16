import sqlite3
import hashlib
from bitcoinaddress import Wallet

DB_PATH = '/home/aliapin/Downloads/github/bt_info/btc.db'

orig_addr_list = []
btc_addr_list = []
wallet_info_list = {}

def getDbConnect():
    connect = sqlite3.connect(DB_PATH)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    
    return connect, cursor

def read_addr_from_file():
    f = open('hash.txt', 'r')
    lines = f.readlines()
    hashes = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        hashes.append(trimmed_line)
        
    return hashes

def string_to_hash256(btc_addr):
    
    #encode() converts the string into bytes to be accepted by the hash function.
    result = hashlib.sha256(btc_addr.encode())

    #hexidigest() returns the encoded data in hexadecimal format
    return result.hexdigest()

def get_wallet_info(btc_addr_hash):
    
    wallet_info = {}
    # wallet info generator (by private key/sha256)
    wallet = Wallet(btc_addr_hash)
    # print(wallet.key.__dict__)
    wallet_info['wif'] = wallet.key.__dict__['mainnet'].__dict__['wif']
    wallet_info['wifc'] = wallet.key.__dict__['mainnet'].__dict__['wifc']
    wallet_info['pubkey'] = wallet.address.__dict__['pubkey']
    wallet_info['pubkeyc'] = wallet.address.__dict__['pubkeyc']
    wallet_info['pubaddr1'] = wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
    wallet_info['pubaddr1c'] = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
    wallet_info['pubaddr3'] = wallet.address.__dict__['mainnet'].__dict__['pubaddr3']
    wallet_info['pubaddrbc1_P2WPKH'] = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH']
    wallet_info['pubaddrbc1_P2WSH'] = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH']
    
    return wallet_info


connection, cursor = getDbConnect()

# 1. get list of addresses from db / orig_addr
orig_addr_list = cursor.execute("SELECT orig_addr FROM balances").fetchall()

# 2. get list of addresses from file / btc_addr
btc_addr_list = read_addr_from_file()

# 3. convert btc_addr to sha256
for btc_addr in btc_addr_list:
    hashed_btc_addr = string_to_hash256(btc_addr)

    # 4. generate wallet info by sha256
    wallet_info_list = get_wallet_info(hashed_btc_addr)

print(wallet_info_list)

# for address in addresses:
#     stock_dict[symbol['symbol']] = symbol['id']

# list_of_symbols = [symbol['symbol'] for symbol in symbols] 

# for i in range(0, len(list_of_symbols), chunk_size):
#     symbol_chunk = list_of_symbols[i:i+chunk_size]
    
#     # Get daily price data for AAPL over the last 5 trading days.
#     barset = api.get_barset(symbol_chunk, 'day')

#     for symbol in barset:
#         for bar in barset[symbol]:
#             if symbol in stock_dict.keys():
#                 bar_id = stock_dict[symbol]
#             else:
#                 print(f'No stock_id for {symbol} found!')
#                 continue
            
#             cursor.execute(f'INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?)', 
#                         (int(bar_id), bar.t.date(), bar.o, bar.h, bar.l, bar.c, bar.v))
#             print(f'{symbol}: inserted')
#     print(f'{i}->{i+chunk_size}')
    
# connection.commit()