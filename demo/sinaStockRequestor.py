import requests as rq
import sys
import json
import pdb
import time

_config={
            'url':'http://hq.sinajs.cn/list='
	}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}


def getStockCurrent(stock):
    url=_config['url']+stock
    print('begin request data from:'+url)
    starttime=time.time()
    response=rq.get(url,headers=headers)
    timespent=time.time()-starttime
    if response.status_code==200:
        print('get data successfully after %.4fs' % timespent)
    else:
        print('get data failed,response status code is %s' % response.status_code)

    return getPureData(response.text)

def getPureData(data):
    lines=data.split('\n')
    result=[]
    for line in lines:
        if len(line)==0:
            break

        splitData=line.split('"')

        if len(splitData)==3:
            newStr=splitData[0][11:19]+","+splitData[1]
            result.append(newStr)
        else:
            print('data content format error')

    return result

if __name__=='__main__':
    getStockCurrent(sys.argv[1])
