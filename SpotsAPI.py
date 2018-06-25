import requests
import time


urlRoot = 'https://www.okex.com/api/v1/'

def getSpotPrices(symbol):
    url = urlRoot + 'ticker.do?' + 'symbol=' + symbol
    r = requests.get(url)
    data = r.content
    return data

def getMarketDepth(symbol,size): # 1<size<200
    url = urlRoot + 'depth.do?' + '&symbol=' + symbol + '&size=' + size
    r = requests.get(url)
    data = r.content
    return data

def getTradeRecently(symbol,since): #get 600 pieces of data from since tid
    url = urlRoot + 'trades.do?' + 'symbol=' + symbol + '&since=' + since
    r = requests.get(url)
    data = r.content
    return data

def getCandlestick(symbol,type,size,since): # type = 1min/3min/5min/15min/30min/1day/3day/1week/1hour/2hour/4hour/6hour/12hour
    url = urlRoot + 'kline.do?' + 'symbol=' + symbol + '&type=' + type + '&size=' + size + '&since=' + since
    r = requests.get(url)
    data = r.content
    return data


i = 1

while (1):
    time.sleep(3)
    print(getMarketDepth('ltc_btc','200'))
    print(i)
    i = i + 1





