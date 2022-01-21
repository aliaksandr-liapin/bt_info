from tools import trans_checker as t_checker

DEV_STATUS = True

if DEV_STATUS:
    matched_transaction = open('./results/addr_tx_list_test.txt', 'a')
else:
    matched_transaction = open('./results/addr_tx_list_prod.txt', 'a')
    
matched_addr = set(t_checker.read_addr_from_file())

for m_addr in matched_addr:
    tx_list = t_checker.check_transactions_by_addr(m_addr)
    
    for tx in tx_list:
        matched_transaction.write(f'{tx}\n')



# def check_addr_by_transaction(transaction):
#     addr_url = f'{basic_url}{transaction}'
#     soup2 = bs4.BeautifulSoup(res.text, features="html.parser")
#     links = soup2.findAll('a', href=re.compile('^/explorer/address/'))
#     print('--------------------------------')
#     for link in links:
#         print(link.text)
#         # trans_data_list.write(f'{link.text}\n')
    
matched_transaction.close()



