import requests, bs4
import time
import re

DEV_STATUS = True

basic_url = 'https://blockchainsql.io'

def read_tx_from_file():
    if DEV_STATUS: f = open('./results/addr_tx_list_test.txt', 'r')
    else: f = open('./results/addr_tx_list_prod.txt', 'r')
        
    lines = f.readlines()
    tx_list = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        tx_list.append(trimmed_line)
        
    return tx_list

def read_addr_from_file():
    if DEV_STATUS: f = open('./results/matched_test.txt', 'r')
    else: f = open('./results/matched_prod.txt', 'r')
        
    lines = f.readlines()
    tx_list = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        tx_list.append(trimmed_line)
        
    return tx_list

def check_transactions_by_addr(address):
    url = f'https://blockchainsql.io/explorer/address/{address}'
    
    time.sleep(0.8)
    res = requests.get(url)
    
    if res.status_code != 200:
        print(f'Stopped, code: {res.status_code}')
        return None, None, None
        
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    links = soup.findAll('a', href=re.compile('^/explorer/transaction/'))
    
    return links

def check_addr_by_transaction(transaction):
    addr_url = f'{basic_url}{transaction}'
    
    time.sleep(0.8)
    res = requests.get(addr_url)
    print(res.status_code)
    
    if res.status_code != 200:
        print(f'Stopped, code: {res.status_code}')
        return None, None, None

    soup2 = bs4.BeautifulSoup(res.text, features="html.parser")
    links = soup2.findAll('a', href=re.compile('^/explorer/address/'))
    for link in links:
        print(link)
    
    return links


