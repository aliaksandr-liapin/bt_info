import sqlite3
import hashlib
from bitcoinaddress import Wallet

DB_PATH = '/home/aliapin/Downloads/github/bt_info/btc.db'

orig_addr_list = []
btc_addr_list = []
wallet_info_list = {}

# error log file
error_log = open('error.txt', 'a')

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
cursor.execute("SELECT orig_addr FROM balances").fetchall()
rows = cursor.fetchall()
orig_addr_list = [row['orig_addr'] for row in rows]

# 2. get list of addresses from file / btc_addr
btc_addr_list = read_addr_from_file()

# 3. convert btc_addr to sha256
for btc_addr in btc_addr_list:
    
    # if btc_addr from the file exists in DB -> skip it
    if btc_addr in orig_addr_list:
        error_log.write(f'{btc_addr} already exists in DB\n')
        print(f'! {btc_addr} already exists in DB')
        continue
    
    # 4 make a sha256 from btc_addr
    hashed_btc_addr = string_to_hash256(btc_addr)

    # 5. generate wallet info by sha256
    wallet_info = get_wallet_info(hashed_btc_addr)

    # 6. data upload to db
        
    cursor.execute("""
            INSERT INTO balances (
            orig_addr,
            orig_addr_sha256,
            priv_key_hex,
            priv_key_wif,
            priv_key_wif_compr, 
            pub_key, 
            pub_key_compr,
            pub_addr,   
            pub_addr_compr,   
            pub_addr_3,  
            pub_addr_bc1_p2wpkh,    
            pub_addr_bc1_p2wsh) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (btc_addr,
                    hashed_btc_addr,
                    hashed_btc_addr,
                    wallet_info['wif'],
                    wallet_info['wifc'],
                    wallet_info['pubkey'],
                    wallet_info['pubkeyc'],
                    wallet_info['pubaddr1'],
                    wallet_info['pubaddr1c'],
                    wallet_info['pubaddr3'],
                    wallet_info['pubaddrbc1_P2WPKH'],
                    wallet_info['pubaddrbc1_P2WSH']
            ))
    
    print(f'{btc_addr} was added into DB')
    
connection.commit()