import requests, bs4
import time
import re

# 1. read address from the file
def read_addr_from_file():
    f = open('hashes.txt', 'r')
    lines = f.readlines()
    address_list = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        address_list.append(trimmed_line)
        
    return address_list

def read_trans_from_file():
    f = open('addr_tx_test.txt', 'r')
    lines = f.readlines()
    tx_list = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        tx_list.append(trimmed_line)
        
    return tx_list

basic_url = 'https://blockchainsql.io/'
addr_info = set(read_addr_from_file())
trans_data_list = open('addr_trans_list.txt', 'a')

# 2. Get address data 
def check_transactions_by_addr(address):
    # url = f'https://www.blockchain.com/btc/address/{address}'

    url = f'https://blockchainsql.io/explorer/address/{address}'
    
    time.sleep(0.8)
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Stopped, code: {res.status_code}')
        return None, None, None
        
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    links = soup.findAll('a', href=re.compile('^/explorer/transaction/'))
    print('--------------------------------')
    for link in links:
        trans_data_list.write(f'{link}\n')
    
    addr_data = address

    return addr_data

def check_addr_by_transaction(transaction):
    addr_url = f'{basic_url}{transaction}'
    soup2 = bs4.BeautifulSoup(res.text, features="html.parser")
    links = soup2.findAll('a', href=re.compile('^/explorer/address/'))
    print('--------------------------------')
    for link in links:
        print(link.text)
        # trans_data_list.write(f'{link.text}\n')
    

# 3. Write data into file
for addr in addr_info:
    time.sleep(.5)
    data = check_transactions_by_addr(addr)
    print(data)
    # addr_data_list.write(f'{data}\n')
    
trans_data_list.close()



