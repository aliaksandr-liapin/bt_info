import requests, bs4

url = 'https://www.blockchain.com/btc/address/1BH2hNXX6n8mdkb2Hc3oC32hTAMrP5ZLZd'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text)
raw_data = soup.select('span[class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"]')
print(raw_data[0].getText())