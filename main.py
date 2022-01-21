from tools import addr_finder as finder

count = 1
found = 0

DEV_STATUS = False

if DEV_STATUS:
    matched_addr = open('./results/matched_test.txt', 'a',  encoding="utf8")
else:
    matched_addr = open('./results/matched_prod.txt', 'a',  encoding="utf8")    

btc_addr_list = set(finder.read_addr_from_file())

for btc_addr in btc_addr_list:
    hashed_btc_addr = finder.string_to_hash256(btc_addr)
    wallet_info = finder.get_wallet_info(hashed_btc_addr)
    
    
    if wallet_info['pubaddr1'] in btc_addr_list:
        matched_addr.write(f'Found (pubaddr1). File-{btc_addr} <> Hash-{wallet_info["pubaddr1"]} -> Priv_Key {hashed_btc_addr} \n')
        found += 1
        
    elif wallet_info['pubaddr1c'] in btc_addr_list:
        matched_addr.write(f'Found (pubaddr1c). File-{btc_addr} <> Hash-{wallet_info["pubaddr1c"]} -> Priv_Key {hashed_btc_addr} \n')
        found += 1
        
    elif wallet_info['pubaddr3'] in btc_addr_list:
        matched_addr.write(f'Found (pubaddr3). File-{btc_addr} <> Hash-{wallet_info["pubaddr3"]} -> Priv_Key {hashed_btc_addr} \n')
        found += 1
        
    elif wallet_info['pubaddrbc1_P2WPKH'] in btc_addr_list:
        matched_addr.write(f'Found (pubaddrbc1_P2WPKH). File-{btc_addr} <> Hash-{wallet_info["pubaddrbc1_P2WPKH"]} -> Priv_Key {hashed_btc_addr} \n')
        found += 1
        
    elif wallet_info['pubaddrbc1_P2WSH'] in btc_addr_list:
        matched_addr.write(f'Found (pubaddrbc1_P2WSH). File-{btc_addr} <> Hash-{wallet_info["pubaddrbc1_P2WSH"]} -> Priv_Key {hashed_btc_addr} \n')
        found += 1
        
    else:
        print(f'[{found}] #{count}')
        count += 1
       
matched_addr.close()




