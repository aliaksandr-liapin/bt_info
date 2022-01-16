import requests, bs4
import time

def check_by_addr_new(address, privKey):
    addr = address

    # Single address
    single_addr_url = 'https://blockchain.info/rawaddr/'

    resp = requests.get(f'{single_addr_url}{addr}')
    json_resp = resp.json()
    check_result = json_resp['n_tx']
    
    return check_result, address, privKey

def check_by_addr(address, privKey):
    url = f'https://www.blockchain.com/btc/address/{address}'
    
    time.sleep(0.8)
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Stopped, code: {res.status_code}')
        return None, None, None
        
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    raw_data = soup.select('span[class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"]')
    print(res.status_code)
    check_result = raw_data[0].getText()
    check_result = check_result.split('.')[0]
    
    return check_result, address, privKey