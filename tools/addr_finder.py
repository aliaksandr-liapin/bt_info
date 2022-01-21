import hashlib
from bitcoinaddress import Wallet

DEV_STATUS = False

def read_addr_from_file():
    if DEV_STATUS:
        f = open('./source/addr_list_test.txt', 'r', encoding="utf8")
    else:
        f = open('./source/addr_list_prod.txt', 'r',  encoding="utf8")
        
    lines = f.readlines()
    hashes = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        hashes.append(trimmed_line)
        
    return hashes

def string_to_hash256(btc_addr):
    result = hashlib.sha256(btc_addr.encode())

    return result.hexdigest()

def get_wallet_info(btc_addr_hash):
    
    wallet_info = {}
    wallet = Wallet(btc_addr_hash)
    # print(wallet.key.__dict__)
    # wallet_info['wif'] = wallet.key.__dict__['mainnet'].__dict__['wif']
    # wallet_info['wifc'] = wallet.key.__dict__['mainnet'].__dict__['wifc']
    # wallet_info['pubkey'] = wallet.address.__dict__['pubkey']
    # wallet_info['pubkeyc'] = wallet.address.__dict__['pubkeyc']
    wallet_info['pubaddr1'] = wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
    wallet_info['pubaddr1c'] = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
    wallet_info['pubaddr3'] = wallet.address.__dict__['mainnet'].__dict__['pubaddr3']
    wallet_info['pubaddrbc1_P2WPKH'] = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH']
    wallet_info['pubaddrbc1_P2WSH'] = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH']
    
    return wallet_info