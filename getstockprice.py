import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def getData(symbol):
    url = f'https://www.google.com/finance/quote/{symbol}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    stock = {'stockName' : soup.find('div', {'class':'zzDege'}).text,
    'price' : soup.find('div', {'class': 'YMlKec fxKbKc'}).text,
    'change' : soup.find('div', {'class': 'JwB6zf'}).text,}
    
    return stock

# print(getData('RELIANCE:NSE'))
# print(getData('TATASTEEL:NSE'))
# print(getData('HDFCBANK:NSE'))
# print(getData('GTLINFRA:NSE'))

watchlist = ['RELIANCE:NSE', 'TATASTEEL:NSE', 'HDFCBANK:NSE', 'GTLINFRA:NSE', 'WIPRO:NSE', 'TCS:NSE']
stockData = []

for item in watchlist:
    stockData.append(getData(item))
    print("Getting", item)

# print(stockData)
 
with open('stockData.json', 'w') as f:
    json.dump(stockData, f)

print('fin.')