from tools import trans_checker as t_checker

DEV_STATUS = True

if DEV_STATUS:
    matched_new_addr = open('./results/matched_new_test.txt', 'a')
else:
    matched_new_addr = open('./results/matched_new_prod.txt', 'a')
    
tx_list = t_checker.read_tx_from_file()

for tx in tx_list:
    addr_list = t_checker.check_addr_by_transaction(tx)
    
    for addr in addr_list:
        print(addr)
        matched_new_addr.write(f'{addr}\n')

    
matched_new_addr.close()