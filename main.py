import hashlib
from itertools import count
from bitcoinaddress import Wallet
import multiprocessing



def read_addr_from_file():
    f = open('addresses_0-200k.txt', 'r')
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

# 1. read orig_btc_addr from file
btc_addr_list = set(read_addr_from_file())
count = 1

matched_addr = open('matched.txt', 'a')

for btc_addr in btc_addr_list:
    
    # 2 make a sha256 from btc_addr
    hashed_btc_addr = string_to_hash256(btc_addr)

    # 5. generate wallet info by sha256
    wallet_info = get_wallet_info(hashed_btc_addr)
    
    if wallet_info['pubaddr1'] in btc_addr_list:
        matched_addr.write(f'Found match. File-{btc_addr} <> Hash-{wallet_info["pubaddr1"]} -> Priv_Key {hashed_btc_addr} \n')
    else:
        print(count)
        count += 1
        
matched_addr.close()