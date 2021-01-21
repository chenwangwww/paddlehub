import requests
from bs4 import BeautifulSoup
from dbCtr import ctr
from funcs import listToStr

rooturl = 'http://www.cn56.net.cn/diming/'

def insertFullData(tb, data):
    for item in data:
        result = {
            'name': item.get_text(),
            'link': item.get('href'),
        }
        ctr.insertData(tb, result)

def crtb(tb, datas):
    ctr.createTb(tb)
    for data in datas:
        insertFullData(tb, data)

def crawlUrl(suburl):
    url = rooturl + suburl
    strhtml = requests.get(url)
    strhtml.encoding = 'gbk'
    soup = BeautifulSoup(strhtml.text, 'lxml')
    search_list = soup.select('#page_left > div.wrpn > a')
    search_name = listToStr(search_list, '_')
    
    if len(search_list) == 1:
        selecter = '#page_left > table:nth-child(4) > tr > td:nth-child(1) > strong > a'
    else:
        selecter = '#page_left > div.infotree > table > tr > td:nth-child(1) > strong > a'
    data = soup.select(selecter)
    if len(data) > 0 and len(search_list) <= 2:
        print(search_name)
        crtb(search_name, [data])
        for item in data:
            subtempurl = item.get('href').split('/')[-1]
            crawlUrl(subtempurl)


# strhtml = requests.get(rooturl)
# strhtml.encoding = 'gbk'
# soup = BeautifulSoup(strhtml.text, 'lxml')
# search_name = '中国'

# selecter1 = 'body > div:nth-child(6) > div.w650 > div > li:nth-child(1) > a'
# data1 = soup.select(selecter1)
# selecter2 = 'body > div:nth-child(6) > div.w650 > div > li > b > a'
# data2 = soup.select(selecter2)

#如果不存在，创建数据表
# ctr.createTb(search_name)

#往数据表插入数据
# for item in data1:
#     result = {
#         'name': item.get_text(),
#         'link': item.get('href'),
#     }
#     ctr.insertData(search_name, result)

# for item in data2:
#     result = {
#         'name': item.get_text(),
#         'link': item.get('href'),
#     }
#     ctr.insertData(search_name, result)

queryData = ctr.queryData('中国')

for search_item in queryData:
    _, suburl = search_item
    suburl = suburl.split('/')[-1]
    crawlUrl(suburl)
