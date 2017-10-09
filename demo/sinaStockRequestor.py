import requests as rq
import sys
import json

_config={
            'url':'http://hq.sinajs.cn/list='
	}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}


def getStockCurrent(stock):
    url=_config['url']+stock
    print('begin request data from:'+url)
    response=rq.get(url,headers=headers)
    if response.status_code=='200':
        print('get data successfully') 
    print(getPureData(response.text))

def getPureData(data):
    splitData=data.split('"')
    if len(splitData)==3:
        return splitData[1]
    else:
        print('data content format error')
        return ''

if __name__=='__main__':
    getStockCurrent(sys.argv[1])
