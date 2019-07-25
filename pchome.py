import requests
from bs4 import BeautifulSoup

res = requests.get('http://pchome.megatime.com.tw/stock/sto2/ock0/sid2330.html',
                   headers={'Referer':'http://pchome.megatime.com.tw/stock/sto3/ock1/sid6505.html'})
res.encoding="utf-8"
html = BeautifulSoup(res.text)
print(html)