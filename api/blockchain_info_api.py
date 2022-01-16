import requests

test_addr = '1NiNja1bUmhSoTXozBRBEtR8LeF9TGbZBN'

# Single address
single_addr_url = 'https://blockchain.info/rawaddr/'

resp = requests.get(f'{single_addr_url}{test_addr}')
json_resp = resp.json()
print(json_resp['n_tx'])